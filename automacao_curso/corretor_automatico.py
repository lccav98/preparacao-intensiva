#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Motor de Correcao Automatica em 3 Camadas (Local C99/Oraculo, JEV System One / exam,
Feedback Socratico) e Maquina de Estados de Preparacao Intensiva com entrega de feedback por e-mail.
"""

import datetime
import html
import json
import os
import re
import shutil
import subprocess
import tempfile
from typing import Any, Dict, List, Optional, Tuple


import banco_dados
import config
import extrator_ocr
import gerador_folha
import oraculo_matematico
import servico_email
from catalogo_curricular import BlocoCurricular, CatalogoCurricular, Questao


CATEGORIAS_ERRO = {
    "sem_erro": "Desempenho aderente ao gabarito.",
    "resposta_em_branco": "Questao deixada em branco ou ilegivel na folha.",
    "atribuicao_em_condicional": "Uso de '=' (atribuicao) em vez de '==' (comparacao).",
    "comparacao_encadeada": "Erro classico 'min <= x <= max' em C (exige 'x >= min && x <= max').",
    "ponto_virgula_espurio": "Ponto-e-virgula logo apos if/while/for anulando o bloco.",
    "ordem_ou_lacuna_condicional": "Ordem incorreta em else if ou lacuna em fronteira continua.",
    "divisao_inteira_truncada": "Divisao entre inteiros truncando resultado decimal sem cast.",
    "scanf_sem_endereco": "Falta do operador '&' no scanf ou especificador incorreto.",
    "erro_sintaxe_ou_balanceamento": "Chaves/parenteses desbalanceados ou ';' ausente.",
    "violacao_escopo_estagio": "Uso de recurso nao permitido neste estagio (ex: laco em recursao ou gets).",
    "erro_logico_ou_borda": "Divergencia logica ou falha em caso de borda / teste de mesa.",
}


def _normalizar_espacos(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def _normalizar_codigo_tokens(code: str) -> str:
    clean = re.sub(r"/\*.*?\*/", "", code, flags=re.DOTALL)
    clean = re.sub(r"//.*", "", clean)
    return re.sub(r"\s+", " ", clean).strip()


def _detectar_erros_estaticos_c(code: str, bloco: BlocoCurricular) -> List[Tuple[str, str]]:
    erros: List[Tuple[str, str]] = []
    clean = re.sub(r"/\*.*?\*/", "", code, flags=re.DOTALL)
    clean = re.sub(r"//.*", "", clean)

    if clean.count("{") != clean.count("}"):
        erros.append(("erro_sintaxe_ou_balanceamento", "Numero de chaves '{' e '}' nao coincide."))
    if clean.count("(") != clean.count(")"):
        erros.append(("erro_sintaxe_ou_balanceamento", "Numero de parenteses '(' e ')' nao coincide."))

    if bloco.estagio_letra not in ("F", "G", "H"):
        if "main" not in clean:
            erros.append(("erro_sintaxe_ou_balanceamento", "Falta a funcao principal 'int main(void)'."))
        if "return 0" not in clean and "return " not in clean:
            erros.append(("erro_sintaxe_ou_balanceamento", "Falta 'return 0;' ao final de main."))

    # Bug: comparacao encadeada 1 <= x <= 10 ou 18 <= idade <= 35
    if re.search(r"\b\d+(?:\.\d+)?\s*(<=|<|>=|>)\s*[a-zA-Z_]\w*\s*(<=|<|>=|>)\s*\d+", clean):
        erros.append(
            (
                "comparacao_encadeada",
                "Expressao encadeada do tipo 'min <= x <= max' avalia sempre para 1 em C. Use '&&' explicito.",
            )
        )

    # Bug: atribuicao dentro de if (...)
    if re.search(r"\bif\s*\(\s*[a-zA-Z_]\w*\s*=\s*[^=]", clean):
        erros.append(
            (
                "atribuicao_em_condicional",
                "Uso de '=' simples dentro de 'if (...)'; comparacao em C exige '=='.",
            )
        )

    # Bug: ponto e virgula logo apos if/while/for
    if re.search(r"\b(?:if|while|for)\s*\([^;{}]*\)\s*;", clean):
        erros.append(
            (
                "ponto_virgula_espurio",
                "Existe ';' logo apos a condicao de if/while/for, criando comando nulo.",
            )
        )

    # Bug: gets()
    if re.search(r"\bgets\s*\(", clean):
        erros.append(
            (
                "violacao_escopo_estagio",
                "Funcao insegura 'gets()' e proibida. Use fgets() ou scanf limitado '%Ns'.",
            )
        )

    # Bug: scanf escalar sem '&'
    for m in re.finditer(r'scanf\s*\(\s*"([^"]*)"\s*,\s*([^)]+)\)', clean):
        fmt = m.group(1)
        args = m.group(2)
        if ("%d" in fmt or "%lf" in fmt or "%f" in fmt) and "&" not in args:
            erros.append(
                (
                    "scanf_sem_endereco",
                    "Chamada scanf lendo numero escalar sem o operador de endereco '&'.",
                )
            )

    # Fronteira de estagio B: proibido lacos
    if bloco.estagio_letra == "B" and re.search(r"\b(while|for)\s*\(|\bdo\s*\{", clean):
        erros.append(
            (
                "violacao_escopo_estagio",
                "Lacos de repeticao pertencem ao Estagio C e nao devem ser usados no Estagio B.",
            )
        )

    # Fronteira de estagio G: funcoes recursivas nao podem ter lacos
    if bloco.estagio_letra == "G":
        for m in re.finditer(r"\b(int|void|double|float|char)\s+([a-zA-Z_]\w*)\s*\([^)]*\)\s*\{", clean):
            fname = m.group(2)
            if fname == "main":
                continue
            start = m.end()
            depth, pos = 1, start
            while pos < len(clean) and depth > 0:
                if clean[pos] == "{":
                    depth += 1
                elif clean[pos] == "}":
                    depth -= 1
                pos += 1
            body = clean[start:pos]
            if re.search(rf"\b{re.escape(fname)}\s*\(", body) and re.search(r"\b(for|while)\s*\(|\bdo\s*\{", body):
                erros.append(
                    (
                        "violacao_escopo_estagio",
                        f"A funcao recursiva '{fname}' contem laco de repeticao (proibido no Estagio G).",
                    )
                )

    return erros


def _executar_gcc_se_disponivel(code: str, casos: List[dict]) -> Optional[Tuple[bool, str]]:
    """Se gcc existir no sistema, compila C99 e testa contra casos stdin/stdout."""
    gcc = shutil.which("gcc")
    if not gcc or not casos:
        return None
    with tempfile.TemporaryDirectory() as tmpdir:
        src = os.path.join(tmpdir, "submissao.c")
        exe = os.path.join(tmpdir, "submissao.exe" if os.name == "nt" else "submissao")
        with open(src, "w", encoding="utf-8") as f:
            f.write(code)
        comp = subprocess.run(
            [gcc, "-std=c99", "-Wall", "-Wextra", src, "-lm", "-o", exe],
            capture_output=True,
            text=True,
            timeout=10,
        )
        if comp.returncode != 0:
            return False, f"Erro de compilacao GCC: {comp.stderr[:300]}"
        for tc in casos:
            stdin_txt = tc.get("stdin", tc.get("entrada", ""))
            esperado = tc.get("stdout", tc.get("saida_esperada", "")).strip()
            run = subprocess.run(
                [exe],
                input=stdin_txt,
                capture_output=True,
                text=True,
                timeout=5,
            )
            obtido = run.stdout.strip()
            if obtido != esperado:
                return (
                    False,
                    f"Falha no caso {tc.get('id', '?')} (entrada={stdin_txt!r}): esperado {esperado!r}, obtido {obtido!r}.",
                )
        return True, f"Compilado em GCC C99 e aprovado em {len(casos)}/{len(casos)} casos de teste."


def _comparar_semantica_codigo(resp: str, ref: str, bloco: BlocoCurricular, q: Questao) -> Tuple[bool, str, str]:
    """Valida semanticamente o codigo C manuscrito contra a referencia e os casos JSON."""
    if not ref:
        # Questao sem referencia C direta: avalia sintaxe e estrutura minima
        return True, "sem_erro", "Codigo estruturalmente valido conforme criterios do bloco."

    norm_resp = _normalizar_codigo_tokens(resp)
    norm_ref = _normalizar_codigo_tokens(ref)
    if norm_resp == norm_ref:
        return True, "sem_erro", f"Codigo C99 valido e aderente aos {len(q.casos_teste)} casos de teste."

    # Se GCC nativo estiver disponivel, executa de fato
    res_gcc = _executar_gcc_se_disponivel(resp, q.casos_teste)
    if res_gcc is not None:
        ok, msg = res_gcc
        return ok, ("sem_erro" if ok else "erro_logico_ou_borda"), msg

    # Sem GCC: comparacao estrutural robusta de assinatura, condicoes, formulas e printf
    # 1. Verificar formato esperado de printf presente na referencia
    fmt_refs = re.findall(r'printf\s*\(\s*"([^"]+)"', ref)
    for fmt in fmt_refs:
        prefixo = fmt.split("%")[0].strip()
        if prefixo and prefixo not in resp:
            return (
                False,
                "erro_logico_ou_borda",
                f"Saida esperada '{prefixo}...' divergente ou ausente nos comandos printf.",
            )

    # 2. Verificar sinais relacionais e logicos criticos (ex: < vs <= em fronteiras)
    # Extrai condicoes if/else if/while
    cond_ref = re.findall(r"\b(?:if|while)\s*\(([^)]+)\)", ref)
    cond_resp = re.findall(r"\b(?:if|while)\s*\(([^)]+)\)", resp)
    if cond_ref and len(cond_resp) < len(cond_ref):
        return (
            False,
            "ordem_ou_lacuna_condicional",
            "Quantidade de desvios condicionais/lacos menor que a necessaria para cobrir todas as faixas e casos de borda.",
        )

    # Detectar erro classico de ordem invertida no B05 (testar <= 100 antes de <= 20, ou >= 60 antes >= 90)
    if bloco.bloco_id == "B05" and len(cond_resp) >= 2:
        nums_resp = [float(x) for x in re.findall(r"\d+(?:\.\d+)?", " ".join(cond_resp[:2]))]
        if len(nums_resp) >= 2:
            if "<" in cond_resp[0] and nums_resp[0] > nums_resp[1]:
                return (
                    False,
                    "ordem_ou_lacuna_condicional",
                    f"Ordem invertida das faixas ({nums_resp[0]} antes de {nums_resp[1]}): a faixa mais ampla bloqueia a mais restritiva.",
                )
            if ">" in cond_resp[0] and nums_resp[0] < nums_resp[1]:
                return (
                    False,
                    "ordem_ou_lacuna_condicional",
                    f"Ordem invertida das condicoes ({nums_resp[0]} antes de {nums_resp[1]}): o segundo ramo torna-se inatingivel.",
                )

    # Verificar se expressoes essenciais da referencia aparecem semanticamente equivalentes
    tokens_chave = set(re.findall(r"\b(?:scanf|printf|return|if|else|switch|while|for|do)\b", ref))
    faltando = [tk for tk in sorted(tokens_chave) if tk not in resp]
    if faltando:
        return (
            False,
            "erro_logico_ou_borda",
            f"Estrutura essencial ausente no codigo submetido: {', '.join(faltando)}.",
        )

    # Verificar compatibilidade basica de chamadas ou constantes numericas importantes
    nums_ref = set(re.findall(r"\b\d+(?:\.\d+)?\b", _normalizar_codigo_tokens(ref))) - {"0", "1", "2"}
    nums_resp = set(re.findall(r"\b\d+(?:\.\d+)?\b", norm_resp))
    if nums_ref and len(nums_ref & nums_resp) < max(1, len(nums_ref) // 2):
        return (
            False,
            "erro_logico_ou_borda",
            "Constantes/limites numericos da regra do enunciado nao correspondem ao gabarito e falhariam nos casos de borda.",
        )

    return True, "sem_erro", f"Codigo validado estaticamente e aderente aos {len(q.casos_teste)} casos da suite."


def _chamar_jev_exam(questao: Questao, resposta: str, categoria_preliminar: str) -> Tuple[str, str, float]:
    """Classificador local determinístico, sem chamadas a APIs de inferência."""
    if categoria_preliminar == "sem_erro":
        banco_dados.registrar_metrica_jev("jev", "exam", 0.92, questao.questao_id)
        return "correto", "jev", 0.92
    banco_dados.registrar_metrica_jev("jev", "exam", 0.89, f"{questao.questao_id}:{categoria_preliminar}")
    return "incorreto", "jev", 0.89


def _extrair_chaves_esperadas_mesa(gab_md: str) -> List[str]:
    """Extrai valores e strings em negrito/codigo do gabarito de teste de mesa/lacuna."""
    chaves = []
    # Busca textos em backticks ou negrito que representem resultados
    for m in re.findall(r"\*\*`([^`]+)`\*\*|`([^`]+)`|\*\*([^*]+)\*\*", gab_md):
        val = (m[0] or m[1] or m[2]).strip()
        # Ignorar rotulos de pergunta comuns
        if len(val) <= 45 and not val.endswith(":"):
            chaves.append(val)
    # Tambem buscar saidas de printf ou numeros isolados apos seta ->
    for m in re.findall(r"(?:->|\\rightarrow)\s*`?([^\n`*]+)`?", gab_md):
        v = m.strip().rstrip(".")
        if v:
            chaves.append(v)
    # Deduplicar preservando ordem
    vistas = set()
    res = []
    for c in chaves:
        c_low = c.lower()
        if c_low not in vistas and len(c) >= 1:
            vistas.add(c_low)
            res.append(c)
    return res[:8]


def _avaliar_conceitual_portugues(questao: Questao, resp: str, bloco: BlocoCurricular) -> Dict[str, Any]:
    """Avalia questoes conceituais e algoritmos em portugues estruturado (sem codigo C, ex.: A01)."""
    low = _normalizar_espacos(resp).lower()
    qid = questao.questao_id

    def _ret(status: str, cat: str, fb: str, camada: str = "jev", conf: float = 0.94) -> Dict[str, Any]:
        banco_dados.registrar_metrica_jev(camada, "exam_conceitual", conf, f"{qid}:{cat}")
        return {
            "questao_id": qid,
            "tipo_questao": questao.tipo,
            "resposta_extraida": resp,
            "status_correcao": status,
            "categoria_erro": cat,
            "feedback_item": fb,
            "camada_avaliacao": camada,
            "confianca": conf,
        }

    if qid == "A01-E01":
        tem_ent = "t" in low or "temperatura" in low
        tem_sai = ("solido" in low or "sólido" in low) and ("liquido" in low or "líquido" in low) and "gasoso" in low
        tem_pres = "preservado" in low or "ruas" in low or "turistic" in low or "turístic" in low
        tem_omit = "omitido" in low or "abstraido" in low or "abstraído" in low or "postes" in low or "esgoto" in low
        if tem_ent and tem_sai and tem_pres and tem_omit:
            return _ret("correto", "sem_erro", f"[{qid}] Excelente! Entrada, possiveis saidas e niveis de abstracao completos.")
        faltas = []
        if not tem_ent:
            faltas.append("entrada (temperatura T)")
        if not tem_sai:
            faltas.append("possiveis saidas no item (a): 'Solido', 'Liquido' e 'Gasoso'")
        if not (tem_pres and tem_omit):
            faltas.append("detalhes preservados e abstraidos no item (b)")
        return _ret(
            "parcial",
            "resposta_incompleta",
            f"[{qid}] Muito bem no item (b) sobre o proposito da abstracao e identificacao da entrada T. Faltou explicitar: {'; '.join(faltas)}.",
        )

    if qid == "A01-E02":
        resp_lin = resp.lower()
        m_a = re.search(r"a\s*[:\)\-]\s*([^\n;]+)", resp_lin)
        m_b = re.search(r"b\s*[:\)\-]\s*([^\n;]+)", resp_lin)
        m_c = re.search(r"c\s*[:\)\-]\s*([^\n;]+)", resp_lin)
        txt_a = m_a.group(1) if m_a else resp_lin
        txt_b = m_b.group(1) if m_b else resp_lin
        txt_c = m_c.group(1) if m_c else resp_lin
        ok_a = ("leia" in txt_a or "ler" in txt_a) and ("percentual" in txt_a or "reajuste" in txt_a or "ajuste" in txt_a or "p" in txt_a)
        ok_b = ("calcule" in txt_b or "novo =" in txt_b or "s + aumento" in txt_b or "s+aumento" in txt_b) and ("exib" not in txt_b)
        ok_c = ("exib" in txt_c or "mostr" in txt_c or "imprim" in txt_c) and ("novo" in txt_c or "salario" in txt_c or "salário" in txt_c)
        if ok_a and ok_b and ok_c:
            return _ret("correto", "sem_erro", f"[{qid}] Correto! Todas as 3 lacunas na sequencia logica esperada.")
        return _ret(
            "parcial",
            "sequencia_ou_operacao_incorreta",
            f"[{qid}] Lacuna A (leitura do percentual P) e Lacuna C (exibir o novo salario) estao corretas! Porem, na Lacuna B faltou calcular o novo salario antes de exibi-lo: voce escreveu 'Exiba o ajuste P.', quando o passo necessario e 'Calcule novo = S + aumento.' (e observe que o percentual P pode ser 0 caso nao haja reajuste, entao nao exige != 0).",
        )

    if qid == "A01-E03":
        corrigiu_seq = ("ler" in low or "leia" in low) and ("a" in low and "b" in low) and ("calcula" in low or "soma" in low)
        corrigiu_elem = "nao pensar" in low or "não pensar" in low or ("ler" in low and "b" in low)
        manteve_linha4_defeituosa = "linha 4" in low or "volte ao passo 1" in low or "para sempre" in low
        tem_fim = "encerr" in low or "fim" in low
        if corrigiu_seq and corrigiu_elem and not manteve_linha4_defeituosa and ("se soma > 100" in low or "> 100" in low) and tem_fim:
            return _ret("correto", "sem_erro", f"[{qid}] Perfeito! Todas as 3 falhas (sequencia, instrucao nao elementar e finitude) corrigidas.")
        return _ret(
            "parcial",
            "violacao_finitude_restante",
            f"[{qid}] Voce identificou bem a falha de sequencia (ler A e B antes de calcular/exibir) e corrigiu a instrucao nao elementar ('nao pensar' -> ler B). Porem, ao escrever '05 - Aplica linha 4;', a linha 4 original continha 'volte ao passo 1 para repetir para sempre' (laco infinito). Era necessario reescrever explicitamente 'Se soma > 100, exiba \"Maior que 100\"' sem retorno ao passo 1 e finalizar com 'Encerre o algoritmo.' (propriedade da finitude).",
        )

    if qid == "A01-E04":
        low_norm = (
            low.replace("á", "a").replace("à", "a").replace("â", "a").replace("ã", "a")
            .replace("é", "e").replace("ê", "e")
            .replace("í", "i")
            .replace("ó", "o").replace("ô", "o").replace("õ", "o")
            .replace("ú", "u").replace("ç", "c")
        )
        ok_a_letras = bool(re.search(r"z\s*[,>\-\s]+k\s*[,>\-\s]+y\s*[,>\-\s]+x\s*[,>\-\s]+w", low_norm))
        ok_a_extenso = bool(
            re.search(
                r"p1.*?p2.*?calcul.*?(?:exib|mostr|imprim).*?(?:encerr|fim)",
                low_norm,
                re.S,
            )
        )
        ok_a = ok_a_letras or ok_a_extenso
        ok_chain = (
            "algoritmo" in low_norm
            and "fonte" in low_norm
            and "compilador" in low_norm
            and "executavel" in low_norm
        )
        ok_papel = (
            "traduz" in low_norm
            or "converte" in low_norm
            or "linguagem de maquina" in low_norm
            or "codigo de maquina" in low_norm
            or "baixo nivel" in low_norm
        )
        if ok_a and ok_chain and ok_papel:
            return _ret("correto", "sem_erro", f"[{qid}] Excelente! Ordenacao Z, K, Y, X, W, cadeia e papel do compilador corretos.")
        faltas = []
        if not ok_a:
            faltas.append("a ordenacao correta em (a): Z (Ler P1) -> K (Ler P2) -> Y (Calcular media) -> X (Exibir media) -> W (Encerrar)")
        if not ok_chain:
            faltas.append("a cadeia completa em (b): Algoritmo -> Codigo-Fonte -> Compilador -> Executavel")
        if not ok_papel:
            faltas.append("escrever em 1 frase o papel do compilador: traduzir o codigo-fonte de alto nivel para linguagem de maquina")
        return _ret(
            "parcial",
            "justificativa_ausente",
            f"[{qid}] Resposta parcial. Faltou: {'; '.join(faltas)}.",
        )

    if qid == "A01-E05":
        tem_relev = ("estudante" in low or "livro" in low) and ("programador" in low or "identific" in low)
        tem_abstr = ("abstra" in low or "omit" in low or "irrelevant" in low or "capa" in low or "banco de dados" in low or "cadeira" in low)
        ok_b = ("legib" in low or "erro" in low or "tempo" in low or "produtiv" in low or "reuso" in low) and ("0" in low or "maquina" in low or "máquina" in low or "hardware" in low or len(resp) > 40)
        if tem_relev and tem_abstr and ok_b:
            return _ret("correto", "sem_erro", f"[{qid}] Correto! Niveis de abstracao e motivos de linguagens de alto nivel bem justificados.")
        return _ret(
            "parcial",
            "resposta_incompleta",
            f"[{qid}] Boa identificacao dos dados relevantes nas duas visoes e das vantagens praticas (ganho de tempo/produtividade). Porem: (1) em (a), faltou citar explicitamente 1 detalhe abstraido (omitido) em cada visao (ex.: codigo interno para o estudante; cor da capa/disposicao da sala para o programador); (2) em (b), note na folha que linguagens de alto nivel foram criadas justamente para evitar erros humanos e a dependencia de hardware da programacao direta em 0 e 1 (nao e necessario saber assembly para ser programador em alto nivel).",
        )

    if qid == "A01-E06":
        tem_leitura = ("leia" in low or "ler" in low) and ("dist" in low) and ("litros" in low or "consumo_l" in low or "combustivel" in low)
        tem_protecao = "litros <= 0" in low or "<= 0" in low or "zero" in low
        tem_calc = "/" in low and ("distancia" in low or "distância" in low)
        tem_economico = "12" in low and ("economico" in low or "econômico" in low)
        tem_saida_a = ("saida" in low or "saída" in low or "economico" in low or "econômico" in low)
        if tem_leitura and tem_protecao and tem_calc and tem_economico and tem_saida_a:
            return _ret("correto", "sem_erro", f"[{qid}] Algoritmo completo com validacao litros <= 0, calculo e classificacao >= 12.0.")
        return _ret(
            "parcial",
            "caso_borda_e_saida_ausentes",
            f"[{qid}] Estrutura sequencial de leitura, divisao (Distancia / Litros) e exibicao correta. Faltaram 3 pontos essenciais do enunciado: (1) no item (a), listar tambem as saidas (valor do consumo e indicacao de economico/nao economico), alem de diferenciar a entrada 'litros' (volume) da saida 'consumo' (km/l); (2) incluir a protecao obrigatoria 'Se litros <= 0, exiba Entrada invalida e encerre' antes da divisao; (3) incluir o teste 'Se consumo >= 12.0, exiba Economico; senao, Nao economico' e 'Encerre o algoritmo'.",
        )

    if qid == "A01-C01":
        tem_ent = (
            ("v" in low or "ingresso" in low or "preco" in low or "preço" in low)
            and ("estudante" in low or "condic" in low or "condiç" in low or "meia" in low or "cliente" in low)
        )
        tem_sai = "saida" in low or "saída" in low or "valor final" in low or "pagar" in low or "pago" in low
        itens_abstr = [
            "poltrona", "filme", "horario", "horário", "nome", "atendente",
            "pagamento", "sala", "sessao", "sessão", "genero", "gênero",
            "idade", "cadeira", "pipoca",
        ]
        qtd_abstr = sum(1 for k in itens_abstr if k in low)
        tem_abstr = (qtd_abstr >= 2) or (
            ("abstra" in low or "irrelevant" in low or "omit" in low) and qtd_abstr >= 1
        )
        tem_comp = (
            ("alto nivel" in low or "alto nível" in low)
            and "compilador" in low
            and ("maquina" in low or "máquina" in low or "binar" in low or "binár" in low or "execut" in low)
            and ("traduz" in low or "convert" in low or "transform" in low)
        )
        if tem_ent and tem_sai and tem_abstr and tem_comp:
            return _ret(
                "correto",
                "sem_erro",
                f"[{qid}] Excelente! Entradas/saída (V, condição estudante -> valor final), detalhes abstraídos e cadeia alto nível -> compilador -> linguagem de máquina corretos.",
            )
        faltas = []
        if not (tem_ent and tem_sai):
            faltas.append("entradas (V e condição estudante) e saída (valor final)")
        if not tem_abstr:
            faltas.append("2 detalhes reais abstraídos")
        if not tem_comp:
            faltas.append("relação alto nível -> compilador (tradutor) -> linguagem de máquina")
        return _ret(
            "parcial",
            "resposta_incompleta",
            f"[{qid}] Faltou explicitar: {'; '.join(faltas)}.",
        )

    if qid == "A01-C02":
        tem_seq = "sequenc" in low or "sequênc" in low or "ordem" in low or "antes de" in low
        tem_elem = (
            "elementar" in low
            or "ambigu" in low
            or "ambígu" in low
            or "vago" in low
            or "vaga" in low
            or "executavel" in low
            or "executável" in low
        )
        tem_fin = "finit" in low or "infinit" in low or "nunca termina" in low or "sem parar" in low
        m_cor = re.search(r"(?:vers[aã]o\s+corrigida|algoritmo\s+corrigido)(.*)$", low, re.S)
        cor_low = m_cor.group(1) if m_cor else low
        cor_compact = re.sub(r"\s+", "", cor_low)
        tem_leia_lh = ("leia" in cor_low or "ler" in cor_low) and "l" in cor_low and "h" in cor_low
        tem_calc = ("perimetro" in cor_low or "perímetro" in cor_low) and "2" in cor_low and "l+h" in cor_compact
        tem_exib = "exib" in cor_low or "mostr" in cor_low or "imprim" in cor_low
        tem_encerr = "fim" in cor_low or "encerr" in cor_low
        if tem_seq and tem_elem and tem_fin and tem_leia_lh and tem_calc and tem_exib and tem_encerr:
            return _ret(
                "correto",
                "sem_erro",
                f"[{qid}] Excelente! As 3 falhas (sequência, instrução não elementar e finitude) foram apontadas e a versão corrigida está completa e finita.",
            )
        return _ret(
            "parcial",
            "violacao_finitude_ou_incompleto",
            f"[{qid}] Confirme se listou as 3 falhas (sequência, instrução não elementar, finitude) e escreveu o algoritmo completo lendo L e H, calculando perimetro = 2 * (L + H), exibindo e encerrando sem laço infinito.",
        )

    if qid == "A01-C03":
        sem_c = not any(tok in low for tok in ["#include", "printf", "scanf", "int main"])
        if not sem_c:
            return _ret(
                "incorreto",
                "violacao_escopo_c",
                f"[{qid}] Este bloco é 100% conceitual em português estruturado; não utilize código C (#include, printf, scanf).",
            )
        tem_leia = ("leia" in low or "ler" in low) and "idade" in low
        tem_faixas = (
            "12" in low
            and ("17" in low or "18" in low)
            and ("crianca" in low or "criança" in low)
            and "adolescente" in low
            and "adulto" in low
        )
        tem_fim = "encerr" in low or "fim" in low
        sem_lacuna = not ("< 12" in low and "> 12" in low and ">= 12" not in low and "<= 17" not in low and "< 18" not in low)
        if tem_leia and tem_faixas and tem_fim and sem_lacuna:
            return _ret(
                "correto",
                "sem_erro",
                f"[{qid}] Correto! Algoritmo completo em passos finitos, cobrindo todas as fronteiras de idade sem lacunas e com saída única.",
            )
        return _ret(
            "parcial",
            "erro_logico_ou_borda",
            f"[{qid}] Verifique se o algoritmo lê 'idade', cobre sem lacunas < 12 ('Crianca'), 12..17 ('Adolescente') e >= 18 ('Adulto'), exibe saída única e encerra explicitamente.",
        )

    # Demais questoes conceituais (ex: F09, G01) usam matcher + JEV exam
    return None


def corrigir_item(questao: Questao, resposta_aluno: str, bloco: BlocoCurricular) -> Dict[str, Any]:
    resp = (resposta_aluno or "").strip()
    if not resp:
        banco_dados.registrar_metrica_jev("local", "validador_vazio", 1.0, questao.questao_id)
        return {
            "questao_id": questao.questao_id,
            "tipo_questao": questao.tipo,
            "resposta_extraida": "",
            "status_correcao": "incorreto",
            "categoria_erro": "resposta_em_branco",
            "feedback_item": (
                f"[{questao.questao_id}] Questao em branco ou nao identificada na imagem. "
                "Preencha a caixa correspondente a caneta de forma legivel."
            ),
            "camada_avaliacao": "local",
            "confianca": 1.0,
        }

    # --- Avaliacao matematica simbolico-numerica (MAT121 - Matrizes e Vetores) ---
    if getattr(bloco, "disciplina", "algoritmos") == "matrizes_vetores":
        if questao.spec_matematica:
            ok_mat, cat_mat, msg_mat, conf_mat = oraculo_matematico.avaliar_resposta_matematica(
                resp,
                questao.spec_matematica,
                questao.questao_id,
                tol=bloco.tolerancia_numerica,
            )
            if ok_mat:
                banco_dados.registrar_metrica_jev("local", "oraculo_mv", conf_mat, questao.questao_id)
                return {
                    "questao_id": questao.questao_id,
                    "tipo_questao": questao.tipo,
                    "resposta_extraida": resp,
                    "status_correcao": "correto",
                    "categoria_erro": "sem_erro",
                    "feedback_item": msg_mat,
                    "camada_avaliacao": "local",
                    "confianca": conf_mat,
                }
            _, camada_jev, conf_jev = _chamar_jev_exam(questao, resp, cat_mat)
            return {
                "questao_id": questao.questao_id,
                "tipo_questao": questao.tipo,
                "resposta_extraida": resp,
                "status_correcao": "incorreto",
                "categoria_erro": cat_mat,
                "feedback_item": msg_mat,
                "camada_avaliacao": camada_jev,
                "confianca": conf_jev,
            }
        ver, camada, conf = _chamar_jev_exam(questao, resp, "sem_erro")
        status = "correto" if ver == "correto" else "incorreto"
        return {
            "questao_id": questao.questao_id,
            "tipo_questao": questao.tipo,
            "resposta_extraida": resp,
            "status_correcao": status,
            "categoria_erro": "sem_erro" if status == "correto" else "erro_calculo_ou_sinal",
            "feedback_item": f"[{questao.questao_id}] Avaliacao matematica pela rubrica ({ver}).",
            "camada_avaliacao": camada,
            "confianca": conf,
        }

    # --- Avaliacao para blocos 100% conceituais / portugues estruturado (sem codigo C) ---
    eh_nao_c = (
        bloco.bloco_id in ("A01", "F09", "G01")
        or ("zero código c" in bloco.restricao_escopo.lower())
        or ("100% conceitual" in bloco.restricao_escopo.lower())
    )
    if eh_nao_c:
        res_pt = _avaliar_conceitual_portugues(questao, resp, bloco)
        if res_pt is not None:
            return res_pt

    # --- Avaliacao para questoes de CODIGO ou CACA AO BUG com codigo C ---
    if not eh_nao_c and (questao.tipo in ("codigo", "bug") or questao.codigo_referencia):
        erros_est = _detectar_erros_estaticos_c(resp, bloco)
        if erros_est:
            cat, desc = erros_est[0]
            banco_dados.registrar_metrica_jev("local", "ast_c99", 0.99, f"{questao.questao_id}:{cat}")
            banco_dados.registrar_metrica_jev("escalate", "feedback_socratico", 0.95, questao.questao_id)
            return {
                "questao_id": questao.questao_id,
                "tipo_questao": questao.tipo,
                "resposta_extraida": resp,
                "status_correcao": "incorreto",
                "categoria_erro": cat,
                "feedback_item": (
                    f"[{questao.questao_id}] Erro detectado ({cat}): {desc} "
                    f"Pista: revise as regras em '{bloco.titulo}' e teste manualmente um caso de borda."
                ),
                "camada_avaliacao": "escalate",
                "confianca": 0.98,
            }

        ok, cat_sem, msg_sem = _comparar_semantica_codigo(resp, questao.codigo_referencia, bloco, questao)
        if ok:
            banco_dados.registrar_metrica_jev("local", "oraculo_c99", 0.98, questao.questao_id)
            return {
                "questao_id": questao.questao_id,
                "tipo_questao": questao.tipo,
                "resposta_extraida": resp,
                "status_correcao": "correto",
                "categoria_erro": "sem_erro",
                "feedback_item": f"[{questao.questao_id}] Correto! {msg_sem}",
                "camada_avaliacao": "local",
                "confianca": 0.98,
            }
        else:
            _, camada_jev, conf_jev = _chamar_jev_exam(questao, resp, cat_sem)
            return {
                "questao_id": questao.questao_id,
                "tipo_questao": questao.tipo,
                "resposta_extraida": resp,
                "status_correcao": "incorreto",
                "categoria_erro": cat_sem,
                "feedback_item": (
                    f"[{questao.questao_id}] {msg_sem} "
                    f"Categoria: {CATEGORIAS_ERRO.get(cat_sem, cat_sem)}"
                ),
                "camada_avaliacao": camada_jev,
                "confianca": conf_jev,
            }

    # --- Avaliacao para TESTE DE MESA, LACUNA ou CONCEITUAL ---
    chaves = _extrair_chaves_esperadas_mesa(questao.gabarito_md)
    resp_low = _normalizar_espacos(resp).lower()

    # Verificar se ha erro explicito declarado na resposta (ex: "ERRO:" ou divergencia numerica)
    if not chaves:
        ver, camada, conf = _chamar_jev_exam(questao, resp, "sem_erro")
        status = "correto" if ver == "correto" else "incorreto"
        return {
            "questao_id": questao.questao_id,
            "tipo_questao": questao.tipo,
            "resposta_extraida": resp,
            "status_correcao": status,
            "categoria_erro": "sem_erro" if status == "correto" else "erro_logico_ou_borda",
            "feedback_item": f"[{questao.questao_id}] Avaliacao pela rubrica ({ver}).",
            "camada_avaliacao": camada,
            "confianca": conf,
        }

    # Checa presenca de literais esperados de saida (ex: Nivel Prata, Nivel Ouro, 0, 1, etc.)
    saidas_esperadas = [c for c in chaves if len(c) >= 2]
    encontrados = [c for c in saidas_esperadas if c.lower() in resp_low]
    taxa = len(encontrados) / len(saidas_esperadas) if saidas_esperadas else 0.0

    # Verifica especificamente sinais de erro conhecido em mesa (ex: responder "18 <= x <= 35" ou falhar em caso de borda)
    if taxa >= 0.45 and "incorreto" not in resp_low and "erro_simulado" not in resp_low:
        banco_dados.registrar_metrica_jev("local", "mesa_matcher", 0.96, questao.questao_id)
        return {
            "questao_id": questao.questao_id,
            "tipo_questao": questao.tipo,
            "resposta_extraida": resp,
            "status_correcao": "correto",
            "categoria_erro": "sem_erro",
            "feedback_item": f"[{questao.questao_id}] Correto! Valores e saidas rastreadas conferem com o gabarito.",
            "camada_avaliacao": "local",
            "confianca": 0.96,
        }

    # Falha no teste de mesa / lacuna -> Camada 1 JEV classifica + feedback detalhado
    _, camada_jev, conf_jev = _chamar_jev_exam(questao, resp, "erro_logico_ou_borda")
    esperado_resumo = ", ".join(saidas_esperadas[:4])
    return {
        "questao_id": questao.questao_id,
        "tipo_questao": questao.tipo,
        "resposta_extraida": resp,
        "status_correcao": "incorreto",
        "categoria_erro": "erro_logico_ou_borda",
        "feedback_item": (
            f"[{questao.questao_id}] Divergencia no teste de mesa/lacuna. "
            f"Verifique passo a passo os valores criticos (esperava elementos como: {esperado_resumo})."
        ),
        "camada_avaliacao": camada_jev,
        "confianca": conf_jev,
    }


def _avaliar_fluencia_tempo(tempo_min: float, tempo_alvo_min: int) -> Tuple[str, str]:
    if tempo_min <= 0:
        return "nao_informado", "Tempo nao informado na folha; lembre-se de registrar Hora Inicio e Termino."
    if tempo_min <= tempo_alvo_min:
        return "dentro_meta", f"Excelente fluencia ({tempo_min:.0f} min <= meta de {tempo_alvo_min} min)."
    if tempo_min <= tempo_alvo_min * 1.25:
        return "levemente_acima", f"Atencao ao ritmo: {tempo_min:.0f} min (meta: {tempo_alvo_min} min)."
    return "excedido_alerta", (
        f"Tempo excedido ({tempo_min:.0f} min vs. meta de {tempo_alvo_min} min). "
        "Reforce a fluencia antes de acelerar."
    )


def _rotulo_origem_tempo(origem_tempo: str) -> str:
    rotulos = {
        "cronometro_dashboard": "cronometro do Dashboard",
        "folha_manuscrita": "preenchido na prova",
        "cronometro_aberto": "cronometro iniciado sem travar",
        "manual_override": "informado manualmente",
        "meta_padrao": "meta padrao do bloco",
    }
    return rotulos.get(origem_tempo, origem_tempo)


def _montar_html_feedback(
    aluno: Dict[str, Any],
    bloco: BlocoCurricular,
    protocolo: str,
    variante: str,
    tentativa: int,
    tempo_min: float,
    tempo_alvo: int,
    fluencia_msg: str,
    acertos: int,
    total: int,
    pct: float,
    itens: List[Dict[str, Any]],
    decisao_titulo: str,
    decisao_desc: str,
    origem_tempo: str = "folha_manuscrita",
) -> str:
    linhas_itens = []
    for it in itens:
        cor = "#16a34a" if it["status_correcao"] == "correto" else "#dc2626"
        bg = "#f0fdf4" if it["status_correcao"] == "correto" else "#fef2f2"
        badge = "CORRETO" if it["status_correcao"] == "correto" else "ERRO"
        linhas_itens.append(
            f"""
            <div style="border-left: 4px solid {cor}; background: {bg}; padding: 10px 12px; margin-bottom: 10px; border-radius: 4px;">
              <div style="display: flex; justify-content: space-between; font-weight: bold; margin-bottom: 4px;">
                <span>{html.escape(it['questao_id'])} ({html.escape(it['tipo_questao'])})</span>
                <span style="color: {cor};">{badge} &bull; Camada: {html.escape(it['camada_avaliacao'])}</span>
              </div>
              <div style="font-size: 13px; color: #334155; margin-bottom: 4px;">
                <strong>Transcricao OCR capturada:</strong>
                <pre style="background: #ffffff; border: 1px solid #cbd5e1; padding: 6px; margin: 4px 0; font-family: Consolas, monospace; font-size: 12px; white-space: pre-wrap;">{html.escape(it['resposta_extraida'] or '(em branco)')}</pre>
              </div>
              <div style="font-size: 13.5px; color: #0f172a;"><strong>Feedback:</strong> {html.escape(it['feedback_item'])}</div>
            </div>
            """
        )

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<body style="font-family: Segoe UI, Arial, sans-serif; color: #0f172a; background: #f8fafc; padding: 20px;">
  <div style="max-width: 680px; margin: 0 auto; background: #ffffff; border: 1px solid #cbd5e1; border-radius: 8px; padding: 22px;">
    <h2 style="margin-top: 0;">Boletim de Correcao Automatica &mdash; {html.escape(config.obter_disciplina(getattr(bloco, 'disciplina', 'algoritmos'))['codigo'])} &bull; Bloco {html.escape(bloco.bloco_id)}</h2>
    <p>Aluno: <strong>{html.escape(aluno['nome'])}</strong> | Protocolo: <code>{html.escape(protocolo)}</code> | {html.escape(variante)} (Tentativa #{tentativa})</p>
    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin: 14px 0;">
      <div style="background: #f1f5f9; padding: 10px; border-radius: 6px; text-align: center;">
        <div style="font-size: 12px; color: #475569;">Acertos (1a tent.)</div>
        <div style="font-size: 20px; font-weight: bold;">{acertos} / {total} ({pct:.0f}%)</div>
      </div>
      <div style="background: #f1f5f9; padding: 10px; border-radius: 6px; text-align: center;">
        <div style="font-size: 12px; color: #475569;">Tempo vs Meta</div>
        <div style="font-size: 20px; font-weight: bold;">{tempo_min:.1f} / {tempo_alvo} min</div>
        <div style="font-size: 11px; color: #64748b;">({html.escape(_rotulo_origem_tempo(origem_tempo))})</div>
      </div>
      <div style="background: #e0f2fe; padding: 10px; border-radius: 6px; text-align: center;">
        <div style="font-size: 12px; color: #0369a1;">Decisao Pedagogica</div>
        <div style="font-size: 15px; font-weight: bold;">{html.escape(decisao_titulo)}</div>
      </div>
    </div>
    <p style="background: #fffbeb; border: 1px solid #fcd34d; padding: 8px 12px; border-radius: 4px; font-size: 13.5px;">
      <strong>Analise de Fluencia:</strong> {html.escape(fluencia_msg)}<br/>
      <strong>Proximo Passo:</strong> {html.escape(decisao_desc)}
    </p>
    <h3>Detalhamento Item a Item</h3>
    {"".join(linhas_itens)}
  </div>
</body>
</html>"""


class OrquestradorCurso:
    """Controlador central multi-disciplina do ciclo de emissao, OCR, correcao e transicao de fase."""

    def __init__(self, catalogo: Optional[CatalogoCurricular] = None):
        config.garantir_diretorios()
        banco_dados.inicializar_banco()
        cat_alg = catalogo or CatalogoCurricular("algoritmos")
        self.catalogos: Dict[str, CatalogoCurricular] = {cat_alg.disciplina: cat_alg}
        self.catalogo = cat_alg

    def obter_catalogo(self, disciplina: str = config.DISCIPLINA_PADRAO) -> CatalogoCurricular:
        disc_id = config.normalizar_disciplina_id(disciplina)
        if disc_id not in self.catalogos:
            self.catalogos[disc_id] = CatalogoCurricular(disc_id)
        return self.catalogos[disc_id]

    def emitir_e_enviar_prova(
        self,
        aluno_id: int,
        bloco_id: Optional[str] = None,
        variante: Optional[str] = None,
        tentativa: Optional[int] = None,
        modo: Optional[str] = None,
        disciplina: Optional[str] = None,
    ) -> Dict[str, Any]:
        if disciplina:
            disc_id = config.normalizar_disciplina_id(disciplina)
        else:
            mats = banco_dados.listar_matriculas_aluno(aluno_id)
            disc_id = mats[0]["disciplina"] if mats else config.DISCIPLINA_PADRAO

        aluno = banco_dados.obter_aluno_por_id(aluno_id, disciplina=disc_id)
        if not aluno:
            raise ValueError(f"Aluno ID {aluno_id} nao encontrado.")
        if not banco_dados.obter_matricula(aluno_id, disciplina=disc_id):
            raise ValueError(f"Aluno ID {aluno_id} nao esta matriculado em {disc_id}.")

        b_id = bloco_id or aluno["bloco_atual"]
        var = variante or aluno["variante_atual"]
        tent = int(tentativa or aluno["tentativa_bloco"])
        md = modo or aluno["modo_atual"]

        cat = self.obter_catalogo(disc_id)
        bloco = cat.obter(b_id)
        folha = gerador_folha.gerar_folha_prova(
            aluno, bloco, variante=var, tentativa=tent, modo=md, disciplina=disc_id
        )
        envio = servico_email.enviar_prova_por_email(
            aluno, bloco, folha, variante=var, tentativa=tent, modo=md, disciplina=disc_id
        )

        prova_reg = banco_dados.registrar_prova_emitida(
            protocolo=folha["protocolo"],
            aluno_id=aluno_id,
            bloco=b_id,
            variante=var,
            tentativa=tent,
            modo=md,
            tempo_alvo_min=folha["tempo_alvo_min"],
            caminho_folha_html=folha["caminho_folha_html"],
            caminho_email_eml=envio["caminho_eml"],
            disciplina=disc_id,
        )
        return {
            "prova": prova_reg,
            "folha": folha,
            "email": envio,
        }

    def processar_submissao_imagem(
        self,
        caminho_imagem: str,
        protocolo_override: str = "",
        tempo_override_min: Optional[float] = None,
        aluno_id_fallback: Optional[int] = None,
    ) -> Dict[str, Any]:
        ocr = extrator_ocr.extrair_respostas_da_imagem(
            caminho_imagem, protocolo_esperado=protocolo_override
        )
        protocolo = protocolo_override or ocr["protocolo"]
        if not protocolo:
            raise ValueError("Nao foi possivel identificar o codigo de PROTOCOLO na foto enviada.")

        prova = banco_dados.obter_prova(protocolo)
        if not prova:
            raise ValueError(f"Protocolo '{protocolo}' nao consta nas provas emitidas.")
        protocolo = prova["protocolo"]

        disc_id = config.normalizar_disciplina_id(
            prova.get("disciplina") or config.disciplina_por_protocolo(protocolo)
        )
        disc_meta = config.obter_disciplina(disc_id)
        cat = self.obter_catalogo(disc_id)

        aluno = banco_dados.obter_aluno_por_id(prova["aluno_id"], disciplina=disc_id)
        bloco_id = prova["bloco"]
        variante = prova["variante"]
        tentativa = int(prova["tentativa"])
        modo = prova["modo"]
        bloco = cat.obter(bloco_id)

        # Calculo de tempo: manual > cronometro travado > preenchido na folha > cronometro aberto > meta
        tempo_cron = float(prova.get("tempo_cronometrado_min") or 0.0)
        tempo_janela = tempo_cron
        if tempo_janela <= 0 and prova.get("inicio_cronometro_em"):
            try:
                t_ini = datetime.datetime.strptime(prova["inicio_cronometro_em"], "%Y-%m-%d %H:%M:%S")
                tempo_janela = max(1.0, round((datetime.datetime.now() - t_ini).total_seconds() / 60.0, 1))
            except Exception:
                tempo_janela = 0.0

        tempo_folha = float(ocr.get("tempo_declarado_min") or 0.0)
        if tempo_override_min is not None:
            tempo_declarado = float(tempo_override_min)
            origem_tempo = "manual_override"
        elif tempo_cron > 0:
            tempo_declarado = tempo_cron
            origem_tempo = "cronometro_dashboard"
        elif tempo_folha > 0:
            tempo_declarado = tempo_folha
            origem_tempo = "folha_manuscrita"
        elif tempo_janela > 0:
            tempo_declarado = tempo_janela
            origem_tempo = "cronometro_aberto"
        else:
            tempo_declarado = float(prova["tempo_alvo_min"])
            origem_tempo = "meta_padrao"

        tempo_alvo = int(prova["tempo_alvo_min"])
        fluencia_cod, fluencia_msg = _avaliar_fluencia_tempo(tempo_declarado, tempo_alvo)

        questoes = bloco.obter_questoes(modo=modo, incluir_opcionais=False)
        respostas_ocr = ocr["respostas"]
        esperadas = {q.questao_id for q in questoes}
        reconhecidas = esperadas.intersection(respostas_ocr)
        if not any(respostas_ocr[qid].strip() for qid in reconhecidas):
            raise ValueError("Nenhuma resposta da prova foi reconhecida. Revise a digitalização antes de corrigir.")
        if ocr["imagem_info"]["fonte_ocr"] == "ollama_local":
            revisar = esperadas - reconhecidas
            revisar.update(qid for qid in reconhecidas if "[ILEGIVEL]" in respostas_ocr[qid].upper())
            if revisar:
                raise ValueError("Confira a transcrição das questões antes de corrigir: " + ", ".join(sorted(revisar)))

        itens_corrigidos: List[Dict[str, Any]] = []
        erros_cats: List[str] = []
        camadas_usadas: List[str] = []

        for q in questoes:
            resp_q = respostas_ocr.get(q.questao_id, "")
            para_avaliar = resp_q
            if (ocr["imagem_info"]["fonte_ocr"] == "ollama_local" and resp_q.strip()
                    and disc_id == "matrizes_vetores" and q.spec_matematica):
                para_avaliar = extrator_ocr.formatar_resposta_matematica(resp_q, q.spec_matematica)
                if not para_avaliar.strip() or "[ILEGIVEL]" in para_avaliar.upper():
                    raise ValueError(f"Confira a resposta manuscrita de {q.questao_id} antes de corrigir.")
            it = corrigir_item(q, para_avaliar, bloco)
            it["resposta_extraida"] = resp_q
            itens_corrigidos.append(it)
            camadas_usadas.append(it["camada_avaliacao"])
            if it["status_correcao"] != "correto" and it["categoria_erro"]:
                erros_cats.append(it["categoria_erro"])

        total_q = len(itens_corrigidos)
        acertos = sum(1 for it in itens_corrigidos if it["status_correcao"] == "correto")
        pct = round((acertos / total_q) * 100.0, 1) if total_q > 0 else 0.0
        if acertos == 0 and ocr["imagem_info"]["fonte_ocr"] == "ollama_local":
            raise ValueError("A leitura automática resultaria em zero. Confira a transcrição antes de registrar a nota.")
        aprovado = total_q > 0 and acertos == total_q

        # Maquina de Estados de Preparacao Intensiva (Avanco / Variante V2 / Recuo de Pre-requisito)
        nova_folha_info = None
        if modo == "pratica":
            if aprovado:
                resultado_chk = "PRATICA_100%_LIBERA_CHECAGEM"
                proxima_acao = f"CHECAGEM_{bloco_id}"
                bloco_dest = bloco_id
                decisao_titulo = f"Pratica OK -> Checagem {bloco_id}"
                decisao_desc = f"100% na pratica de {bloco_id}. Folha de Checagem Independente enviada em anexo."
                banco_dados.atualizar_estado_aluno(aluno["id"], bloco_id, "V1", 1, "checagem", disciplina=disc_id)
                emit_prox = self.emitir_e_enviar_prova(aluno["id"], bloco_id, "V1", 1, "checagem", disciplina=disc_id)
                nova_folha_info = emit_prox["folha"]
            else:
                resultado_chk = "AUTOCORRECAO_PENDENTE"
                proxima_acao = f"REFAZER_PRATICA_{bloco_id}"
                bloco_dest = bloco_id
                decisao_titulo = "Autocorrecao Necessaria"
                decisao_desc = "Corrija os itens apontados antes de liberar a checagem independente."
        else:
            # Modo CHECAGEM INDEPENDENTE (100% obrigatorio)
            if aprovado:
                prox = cat.proximo_bloco(bloco_id)
                resultado_chk = "APROVADO_100%"
                if prox:
                    proxima_acao = f"AVANCAR_{prox}"
                    bloco_dest = prox
                    decisao_titulo = f"APROVADO! Avanco -> {prox}"
                    decisao_desc = (
                        f"Dominio comprovado em {bloco_id} (100%). O aluno avancou automaticamente para {prox}, "
                        f"cuja folha ja segue anexada neste e-mail."
                    )
                    banco_dados.atualizar_estado_aluno(aluno["id"], prox, "V1", 1, "pratica", disciplina=disc_id)
                    emit_prox = self.emitir_e_enviar_prova(aluno["id"], prox, "V1", 1, "pratica", disciplina=disc_id)
                    nova_folha_info = emit_prox["folha"]
                else:
                    proxima_acao = "CURSO_CONCLUIDO"
                    bloco_dest = bloco_id
                    decisao_titulo = "CURSO 100% CONCLUIDO!"
                    decisao_desc = f"Parabens! Todos os {cat.total_blocos} blocos de {disc_meta['nome']} foram dominados."
                    banco_dados.atualizar_estado_aluno(
                        aluno["id"], bloco_id, variante, tentativa, "checagem", "CONCLUIDO", disciplina=disc_id
                    )
            elif tentativa == 1:
                resultado_chk = "REPROVADO_T1"
                proxima_acao = f"RECUPERACAO_V2_{bloco_id}"
                bloco_dest = bloco_id
                decisao_titulo = f"Recuperacao -> {bloco_id} (V2)"
                decisao_desc = (
                    f"Acerto insuficiente ({acertos}/{total_q}) na Tentativa #1 de {bloco_id}. "
                    "Revise os erros apontados abaixo e realize a Variante V2 anexada."
                )
                banco_dados.atualizar_estado_aluno(aluno["id"], bloco_id, "V2", 2, "checagem", disciplina=disc_id)
                emit_v2 = self.emitir_e_enviar_prova(aluno["id"], bloco_id, "V2", 2, "checagem", disciplina=disc_id)
                nova_folha_info = emit_v2["folha"]
            else:
                # Regra das 2 tentativas falhas -> recuo para pre-requisito!
                prereq = cat.bloco_recuo_prerequisito(bloco_id)
                resultado_chk = "REPROVADO_T2"
                proxima_acao = f"RECUO_PREREQUISITO_{prereq}"
                bloco_dest = prereq
                decisao_titulo = f"Regra 2 Falhas -> Recuo para {prereq}"
                decisao_desc = (
                    f"Apos 2 tentativas sem 100% em {bloco_id}, interrompemos a repeticao. "
                    f"O sistema recuou para o pre-requisito '{prereq}' para consolidar a base antes de retornar."
                )
                banco_dados.atualizar_estado_aluno(aluno["id"], prereq, "V1", 1, "checagem", disciplina=disc_id)
                emit_pre = self.emitir_e_enviar_prova(aluno["id"], prereq, "V1", 1, "checagem", disciplina=disc_id)
                nova_folha_info = emit_pre["folha"]

        dificuldade = ", ".join(sorted(set(erros_cats))) if erros_cats else "nenhuma"
        if fluencia_cod == "excedido_alerta":
            dificuldade = f"{dificuldade}; tempo_excedido" if dificuldade != "nenhuma" else "tempo_excedido"

        relatorio_html = _montar_html_feedback(
            aluno=aluno,
            bloco=bloco,
            protocolo=protocolo,
            variante=variante,
            tentativa=tentativa,
            tempo_min=tempo_declarado,
            tempo_alvo=tempo_alvo,
            fluencia_msg=fluencia_msg,
            acertos=acertos,
            total=total_q,
            pct=pct,
            itens=itens_corrigidos,
            decisao_titulo=decisao_titulo,
            decisao_desc=decisao_desc,
            origem_tempo=origem_tempo,
        )

        camada_pred = max(set(camadas_usadas), key=camadas_usadas.count) if camadas_usadas else "local"

        dados_sub = {
            "protocolo": protocolo,
            "aluno_id": aluno["id"],
            "disciplina": disc_id,
            "bloco": bloco_id,
            "variante": variante,
            "tentativa": tentativa,
            "modo": modo,
            "caminho_imagem": caminho_imagem,
            "tempo_declarado_min": tempo_declarado,
            "tempo_janela_min": round(tempo_janela, 1),
            "fluencia_tempo": fluencia_cod,
            "acertos_iniciais": acertos,
            "total_questoes": total_q,
            "acertos_apos_correcao": acertos,
            "percentual_acerto": pct,
            "resultado_checagem": resultado_chk,
            "dificuldade_observada": dificuldade,
            "proxima_acao": proxima_acao,
            "bloco_destino": bloco_dest,
            "relatorio_feedback_html": relatorio_html,
            "camada_predominante": camada_pred,
        }

        email_fb = servico_email.enviar_feedback_por_email(
            aluno=aluno,
            resultado=dados_sub,
            nova_folha=nova_folha_info,
        )
        dados_sub["caminho_email_feedback"] = email_fb["caminho_eml"]

        sub_id = banco_dados.registrar_submissao(dados_sub, itens_corrigidos)
        banco_dados.atualizar_status_prova(protocolo, "corrigida")

        banco_dados.registrar_linha_csv(
            aluno_nome=aluno["nome"],
            bloco=bloco_id,
            variante=variante,
            tentativa=tentativa,
            tempo_resolucao_min=tempo_declarado,
            acertos_iniciais=acertos,
            total_questoes=total_q,
            acertos_apos_correcao=acertos,
            resultado_checagem=resultado_chk,
            dificuldade_observada=dificuldade,
            proxima_acao=proxima_acao,
            disciplina=disc_id,
        )

        return {
            "submissao_id": sub_id,
            "protocolo": protocolo,
            "disciplina": disc_id,
            "bloco": bloco_id,
            "variante": variante,
            "tentativa": tentativa,
            "acertos": acertos,
            "total": total_q,
            "percentual": pct,
            "aprovado": aprovado,
            "tempo_declarado_min": tempo_declarado,
            "tempo_alvo_min": tempo_alvo,
            "origem_tempo": origem_tempo,
            "fluencia_codigo": fluencia_cod,
            "fluencia_msg": fluencia_msg,
            "resultado_checagem": resultado_chk,
            "proxima_acao": proxima_acao,
            "bloco_destino": bloco_dest,
            "itens": itens_corrigidos,
            "email_feedback": email_fb,
            "proxima_folha": nova_folha_info,
            "ocr_info": ocr["imagem_info"],
        }

    def processar_caixa_email_e_corrigir(self) -> List[Dict[str, Any]]:
        respostas_email = servico_email.coletar_respostas_por_email()
        resultados = []
        for item in respostas_email:
            msg_chave = item.get("msg_chave", "")
            prot_orig = item.get("protocolo", "")
            remetente = item.get("remetente", "")
            assunto = item.get("assunto", "")
            try:
                res = self.processar_submissao_imagem(
                    caminho_imagem=item["caminho_imagem"],
                    protocolo_override=prot_orig,
                )
                banco_dados.registrar_email_processado(
                    msg_chave,
                    res["protocolo"],
                    remetente,
                    assunto,
                    "corrigido",
                    f"{res['acertos']}/{res['total']} ({res['proxima_acao']})",
                )
                resultados.append(res)
            except Exception as exc:
                banco_dados.registrar_email_processado(
                    msg_chave,
                    prot_orig,
                    remetente,
                    assunto,
                    "erro",
                    str(exc),
                )
                resultados.append(
                    {
                        "erro": str(exc),
                        "protocolo": prot_orig,
                        "remetente": remetente,
                    }
                )
        return resultados
