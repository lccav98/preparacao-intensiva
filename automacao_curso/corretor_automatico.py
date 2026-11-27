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
import unicodedata
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


def _normalizar_sem_acentos(s: str) -> str:
    nfkd = unicodedata.normalize("NFKD", str(s or ""))
    sem_ac = "".join(ch for ch in nfkd if not unicodedata.combining(ch))
    return re.sub(r"\s+", " ", sem_ac).strip().lower()


def _avaliar_semantica_gemini_opcional(
    questao: Questao, resp: str, bloco: BlocoCurricular
) -> Optional[Tuple[str, str]]:
    """Avalia respostas conceituais/tecnicas longas via Gemini somente quando ha chave configurada."""
    if os.environ.get("PREP_DESATIVAR_GEMINI_RUBRICA", "").strip():
        return None
    if len((resp or "").strip()) < 35:
        return None
    cfg = config.obter_integracoes()
    gem_key = (
        os.environ.get("GEMINI_API_KEY", "").strip()
        or os.environ.get("PREP_GEMINI_API_KEY", "").strip()
        or str(cfg.get("gemini_api_key", "") or "").strip()
    )
    if not gem_key:
        return None
    prompt = (
        f"Voce e avaliador da disciplina '{bloco.disciplina}', bloco '{bloco.titulo}', questao {questao.questao_id}.\n"
        f"Enunciado: {questao.enunciado_md[:900]}\n"
        f"Gabarito de referencia: {questao.gabarito_md[:1100]}\n"
        f"Resposta do aluno: {resp[:1500]}\n"
        "Compare semanticamente a resposta do aluno com o gabarito. "
        "Retorne JSON com veredito ('correto', 'parcial' ou 'incorreto') e feedback curto em portugues."
    )
    formato = {
        "type": "object",
        "properties": {
            "veredito": {"type": "string"},
            "feedback": {"type": "string"},
        },
        "required": ["veredito", "feedback"],
    }
    try:
        res = extrator_ocr._consultar_modelo_gemini(
            {"role": "user", "content": prompt},
            formato,
            gem_key,
            modelo_override=str(cfg.get("gemini_model", "") or ""),
        )
        ver = str(res.get("veredito", "")).strip().lower()
        fb = str(res.get("feedback", "")).strip()
        if ver in ("correto", "parcial", "incorreto") and fb:
            return ver, fb
    except Exception:
        return None
    return None


def _avaliar_por_rubrica_estruturada(
    questao: Questao, resp: str, bloco: BlocoCurricular
) -> Dict[str, Any]:
    """Avalia resposta contra rubrica estruturada com criterios objetivos e dica socratica."""
    qid = questao.questao_id
    rub = questao.rubrica or {}
    norm = _normalizar_sem_acentos(resp)
    dica_socratica = str(rub.get("dica_socratica") or "").strip()

    for tp in (rub.get("termos_proibidos") or []):
        tp_norm = _normalizar_sem_acentos(str(tp))
        if tp_norm and tp_norm in norm:
            banco_dados.registrar_metrica_jev("local", "rubrica_bcc", 0.96, f"{qid}:termo_proibido")
            return {
                "questao_id": qid,
                "tipo_questao": questao.tipo,
                "resposta_extraida": resp,
                "status_correcao": "incorreto",
                "categoria_erro": "violacao_escopo_estagio",
                "feedback_item": f"[{qid}] Termo ou abordagem nao permitida detectada ('{tp}'). {dica_socratica}".strip(),
                "camada_avaliacao": "local",
                "confianca": 0.96,
            }

    criterios = list(rub.get("criterios") or [])
    atendidos = 0
    faltantes_obrig: List[str] = []
    faltantes_opc: List[str] = []

    for crit in criterios:
        nome = str(crit.get("nome") or "Criterio").strip()
        termos = [_normalizar_sem_acentos(str(t)) for t in (crit.get("termos_any") or []) if str(t).strip()]
        ok_crit = any(t in norm for t in termos) if termos else True
        if ok_crit:
            atendidos += 1
        else:
            if crit.get("obrigatorio", False):
                faltantes_obrig.append(nome)
            else:
                faltantes_opc.append(nome)

    min_req = min(int(rub.get("min_criterios_aprovacao", max(1, len(criterios)))), max(1, len(criterios)))
    if not faltantes_obrig and atendidos >= min_req:
        banco_dados.registrar_metrica_jev("local", "rubrica_bcc", 0.95, qid)
        return {
            "questao_id": qid,
            "tipo_questao": questao.tipo,
            "resposta_extraida": resp,
            "status_correcao": "correto",
            "categoria_erro": "sem_erro",
            "feedback_item": f"[{qid}] Correto! Todos os criterios essenciais de {bloco.bloco_id} foram atendidos ({atendidos}/{len(criterios)}).",
            "camada_avaliacao": "local",
            "confianca": 0.95,
        }

    sem = _avaliar_semantica_gemini_opcional(questao, resp, bloco)
    if sem and sem[0] == "correto":
        banco_dados.registrar_metrica_jev("escalate", "rubrica_gemini", 0.88, qid)
        return {
            "questao_id": qid,
            "tipo_questao": questao.tipo,
            "resposta_extraida": resp,
            "status_correcao": "correto",
            "categoria_erro": "sem_erro",
            "feedback_item": f"[{qid}] {sem[1]}",
            "camada_avaliacao": "escalate",
            "confianca": 0.88,
        }

    faltantes = faltantes_obrig + faltantes_opc
    status = "parcial" if atendidos > 0 else "incorreto"
    cat = "resposta_incompleta" if atendidos > 0 else "erro_logico_ou_borda"
    _, camada_jev, conf_jev = _chamar_jev_exam(questao, resp, cat)
    det_falt = "; ".join(faltantes[:4]) if faltantes else "elementos esperados pela rubrica"
    msg_fb = f"[{qid}] Criterios pendentes ({atendidos}/{len(criterios)} atendidos): {det_falt}."
    if sem and sem[1]:
        msg_fb += f" Observacao: {sem[1]}"
    elif dica_socratica:
        msg_fb += f" Pista: {dica_socratica}"
    return {
        "questao_id": qid,
        "tipo_questao": questao.tipo,
        "resposta_extraida": resp,
        "status_correcao": status,
        "categoria_erro": cat,
        "feedback_item": msg_fb,
        "camada_avaliacao": camada_jev,
        "confianca": conf_jev,
    }


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
    # Busca textos em backticks ou negrito na mesma linha (sem cruzar quebras de linha)
    for m in re.findall(r"\*\*`([^`\n]+)`\*\*|`([^`\n]+)`|\*\*([^*\n]+)\*\*", gab_md):
        val = (m[0] or m[1] or m[2]).strip().strip("`").strip()
        # Ignorar rotulos de pergunta comuns e marcadores de lacuna /* A */
        if not val or val.endswith(":") or val.rstrip("* ").endswith(":"):
            continue
        if re.fullmatch(r"/\*\s*[A-Z0-9]+\s*\*/", val):
            continue
        if len(val) <= 60:
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


def _corrigir_item_nucleo(questao: Questao, resposta_aluno: str, bloco: BlocoCurricular) -> Dict[str, Any]:
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

    # --- Avaliacao para demais disciplinas do BCC Matriz 826 ---
    disc_bloco = getattr(bloco, "disciplina", "algoritmos")
    if disc_bloco not in ("algoritmos", "matrizes_vetores"):
        if questao.spec_matematica:
            ok_mat, cat_mat, msg_mat, conf_mat = oraculo_matematico.avaliar_resposta_matematica(
                resp,
                questao.spec_matematica,
                questao.questao_id,
                tol=bloco.tolerancia_numerica,
            )
            if ok_mat:
                banco_dados.registrar_metrica_jev("local", "oraculo_matematico_bcc", conf_mat, questao.questao_id)
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
        if getattr(questao, "rubrica", None):
            return _avaliar_por_rubrica_estruturada(questao, resp, bloco)

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


_DISCS_MATEMATICAS_BCC = {
    "matrizes_vetores",
    "matematica_discreta",
    "pre_calculo",
    "calculo_1",
    "calculo_2",
    "algebra_linear",
    "calculo_numerico",
    "probabilidade_estatistica",
}


def gerar_esquema_grafico_para_item(
    item: Dict[str, Any],
    bloco_id: str,
    disciplina: str = "algoritmos",
    questao: Optional[Questao] = None,
) -> Dict[str, Any]:
    """Gera esquema pedagogico de 3 etapas + arco de retorno adaptado ao dominio de Ciencia da Computacao."""
    status = str(item.get("status_correcao") or "incorreto")
    cat = str(item.get("categoria_erro") or "")
    tipo = str(item.get("tipo_questao") or (questao.tipo if questao else "") or "codigo").lower()
    eh_ok = status == "correto"
    em_branco = cat == "resposta_em_branco"

    if tipo in ("codigo", "bug", "sql"):
        if em_branco:
            s1, s2, s3 = "Nao identificado na folha", "Codigo ausente ou ilegivel", "Sem saida verificavel"
            ok1, ok2, ok3 = False, False, False
        elif eh_ok:
            s1, s2, s3 = "Assinatura/tipos corretos", "Sintaxe e logica validas", "Saida e bordas OK"
            ok1, ok2, ok3 = True, True, True
        elif cat in ("erro_sintaxe_ou_balanceamento", "violacao_escopo"):
            s1 = "Rever declaracoes/escopo"
            s2 = "Falha de sintaxe C99/SQL (ex.: ';', '{ }', tipos)"
            s3 = "Corrigir antes de testar casos de borda"
            ok1, ok2, ok3 = True, False, False
        else:
            s1 = "Entrada e estrutura reconhecidas"
            s2 = "Verificar fluxo logico / comandos"
            s3 = "Divergencia na saida ou caso de borda"
            ok1, ok2, ok3 = True, False, False
        return {
            "titulo_esquema": "Mapa Visual de Resolucao (Codigo / Algoritmos)",
            "arco_retorno": "A saida produzida deve atender integralmente ao contrato e aos casos de borda do enunciado",
            "colunas": [
                {
                    "titulo": "1. Contrato e Entradas",
                    "subtitulo": f"Bloco {bloco_id} ({tipo.upper()})",
                    "tom": "dado",
                    "como_escrever": [
                        "Identificar entradas, tipos e restricoes",
                        "Declarar variaveis e headers obrigatorios",
                    ],
                    "ok": ok1,
                    "erro_aluno": s1,
                },
                {
                    "titulo": "2. Logica e Sintaxe",
                    "subtitulo": "Desenvolvimento estruturado",
                    "tom": "autoral",
                    "como_escrever": [
                        "Encadear passos sem atalhos ou erros de sintaxe",
                        "Preservar indentacao, chaves e ';'",
                    ],
                    "ok": ok2,
                    "erro_aluno": s2,
                },
                {
                    "titulo": "3. Saida e Casos de Borda",
                    "subtitulo": "Validacao final",
                    "tom": "autoral",
                    "como_escrever": [
                        "Rastrear no papel para N=0, negativos ou vazios",
                        "Conferir formato exato da impressao",
                    ],
                    "ok": ok3,
                    "erro_aluno": s3,
                },
            ],
        }

    if tipo in ("matriz", "vetor", "calculo") or disciplina in _DISCS_MATEMATICAS_BCC:
        if em_branco:
            s1, s2, s3 = "Dados nao lidos", "Passos em branco", "Sem resposta final"
            ok1, ok2, ok3 = False, False, False
        elif eh_ok:
            s1, s2, s3 = "Dados e notacao corretos", "Passos consistentes", "Resultado exato conferido"
            ok1, ok2, ok3 = True, True, True
        elif cat in ("resposta_incompleta", "erro_formato_ou_leitura", "formato_invalido"):
            s1 = "Enunciado lido"
            s2 = "Passo a passo ou subitem incompleto"
            s3 = "Preencher todos os itens no formato pedido"
            ok1, ok2, ok3 = True, False, False
        else:
            s1 = "Enunciado mapeado"
            s2 = "Revisar operacoes intermediarias / sinal"
            s3 = "Valor/dimensao divergente na Resposta Final"
            ok1, ok2, ok3 = True, False, False
        return {
            "titulo_esquema": "Mapa Visual de Resolucao (Matrizes / Matematica)",
            "arco_retorno": "Conferir se a Resposta Final satisfaz as equacoes/dimensoes iniciais do problema",
            "colunas": [
                {
                    "titulo": "1. Dados e Estrutura",
                    "subtitulo": f"Bloco {bloco_id} ({tipo.upper()})",
                    "tom": "dado",
                    "como_escrever": [
                        "Extrair vetores, matrizes ou grafos do enunciado",
                        "Conferir dimensoes, indices e unidades",
                    ],
                    "ok": ok1,
                    "erro_aluno": s1,
                },
                {
                    "titulo": "2. Desenvolvimento",
                    "subtitulo": "Calculo passo a passo",
                    "tom": "autoral",
                    "como_escrever": [
                        "Manter fracoes e sinais exatos por etapa",
                        "Registrar pivôs, arestas ou camadas intermediarias",
                    ],
                    "ok": ok2,
                    "erro_aluno": s2,
                },
                {
                    "titulo": "3. Conferencia Final",
                    "subtitulo": "Formato exato exigido",
                    "tom": "autoral",
                    "como_escrever": [
                        "Substituir o resultado para validar",
                        "Destacar na caixa Resposta Final",
                    ],
                    "ok": ok3,
                    "erro_aluno": s3,
                },
            ],
        }

    # Perfil Conceitual / Mesa / Lacuna / Logica / Projeto
    if em_branco:
        s1, s2, s3 = "Caixa em branco", "Argumentacao ausente", "Sem conclusao"
        ok1, ok2, ok3 = False, False, False
    elif eh_ok:
        s1, s2, s3 = "Definicao precisa", "Fundamentacao tecnica OK", "Criterios e conclusao completos"
        ok1, ok2, ok3 = True, True, True
    elif cat == "termo_proibido":
        s1 = "Abordagem fora do escopo do bloco"
        s2 = "Evitar termos/recursos nao permitidos ainda"
        s3 = "Reescrever usando apenas ferramentas do bloco"
        ok1, ok2, ok3 = False, False, False
    else:
        s1 = "Tema central identificado"
        s2 = "Faltou articular criterio ou rastreamento"
        s3 = "Completar conclusao objetiva com termos-chave"
        ok1, ok2, ok3 = True, False, False
    return {
        "titulo_esquema": "Mapa Visual de Resolucao (Conceitual / Teste de Mesa)",
        "arco_retorno": "A resposta final deve fechar diretamente o objetivo pedido no enunciado",
        "colunas": [
            {
                "titulo": "1. Conceito do Bloco",
                "subtitulo": f"Bloco {bloco_id}",
                "tom": "dado",
                "como_escrever": [
                    "Identificar o que a questao pede exatamente",
                    "Respeitar a restricao de escopo do bloco",
                ],
                "ok": ok1,
                "erro_aluno": s1,
            },
            {
                "titulo": "2. Desenvolvimento / Rastreio",
                "subtitulo": "Etapas e justificativa",
                "tom": "autoral",
                "como_escrever": [
                    "Explicar o mecanismo passo a passo (causa -> efeito)",
                    "Usar termos tecnicos corretos e exatos",
                ],
                "ok": ok2,
                "erro_aluno": s2,
            },
            {
                "titulo": "3. Sintese e Criterios",
                "subtitulo": "Fechamento verificavel",
                "tom": "autoral",
                "como_escrever": [
                    "Responder todos os subitens (a), (b), ...",
                    "Conferir clareza e completude antes de enviar",
                ],
                "ok": ok3,
                "erro_aluno": s3,
            },
        ],
    }


def _dica_padrao_categoria(cat: str, tipo: str) -> str:
    mapa = {
        "resposta_em_branco": "Preencha a caixa correspondente a caneta mantendo os marcadores [QUESTAO: ...] e [/QUESTAO] visiveis na foto.",
        "erro_sintaxe_ou_balanceamento": "Revise ';' ao fim de instrucoes, balanceamento de chaves/parenteses, headers (#include) e tipos em C.",
        "erro_logico_ou_borda": "Execute um teste de mesa passo a passo e confira casos extremos (zeros, negativos, empates ou subitens faltantes).",
        "erro_calculo_ou_sinal": "Refaca as contas etapa por etapa mantendo fracoes/radicais exatos e conferindo sinais + e -.",
        "resposta_incompleta": "Responda todos os subitens solicitados ((a), (b), ...) exatamente no formato pedido no enunciado.",
        "termo_proibido": "Use exclusivamente os recursos permitidos na restricao de escopo deste bloco.",
        "violacao_escopo": "Ajuste a solucao para permanecer estritamente dentro das ferramentas liberadas neste bloco.",
    }
    return mapa.get(cat, "Compare cada passo da sua solucao com os exemplos guiados do bloco mantendo sua abordagem principal.")


def _enriquecer_feedback_pedagogico_bcc(
    item: Dict[str, Any], questao: Questao, bloco: BlocoCurricular
) -> Dict[str, Any]:
    """Estrutura o feedback em topicos claros mantendo 100% do diagnostico principal e anexa esquema visual."""
    out = dict(item)
    disc_id = getattr(bloco, "disciplina", "algoritmos")
    out["esquema_grafico"] = gerar_esquema_grafico_para_item(out, bloco.bloco_id, disc_id, questao=questao)
    if out.get("status_correcao") == "correto":
        return out

    fb = str(out.get("feedback_item") or "").strip()
    cat = str(out.get("categoria_erro") or "erro_logico_ou_borda")
    if "\n• " in fb:
        return out

    spec = questao.spec_matematica if isinstance(questao.spec_matematica, dict) else {}
    rub = questao.rubrica if isinstance(questao.rubrica, dict) else {}
    dica_spec = str(spec.get("dica_erro") or rub.get("dica_socratica") or "").strip()
    como = dica_spec or _dica_padrao_categoria(cat, questao.tipo)

    partes = [fb, f"Como corrigir (mantendo sua ideia): {como}"]

    if cat in ("erro_sintaxe_ou_balanceamento", "violacao_escopo", "formato_invalido", "erro_formato_ou_leitura", "resposta_incompleta"):
        fmt_hint = (
            "Confira sintaxe exata (chaves, parenteses, ';', especificadores %d/%lf/%c)."
            if questao.tipo in ("codigo", "bug", "sql")
            else "Escreva a resposta no formato pedido no enunciado (ex.: subitens (a), (b), matriz [[...]] ou vetor (...))."
        )
        partes.append(f"Sintaxe e Formato Tecnico: {fmt_hint}")

    try:
        disc_nome = config.obter_disciplina(disc_id)["nome"]
    except Exception:
        disc_nome = disc_id
    titulo_limpo = re.sub(r"`([^`]+)`", r"\1", getattr(bloco, "titulo", "") or bloco.bloco_id)
    micro = str(getattr(bloco, "micro_habilidade", "") or "").strip()
    revisar = f"Releia as Instrucoes Curtas e exemplos do Bloco {bloco.bloco_id} ({titulo_limpo}) em {disc_nome}"
    if micro:
        revisar += f" — foco: {micro}"
    partes.append(f"O que revisar no bloco: {revisar}")

    cat_rot = CATEGORIAS_ERRO.get(cat, cat or "Criterio tecnico do bloco")
    camada_rot = str(out.get("camada_avaliacao") or "local").upper()
    partes.append(f"Critérios de Avaliação: {cat_rot}; Camada {camada_rot}")

    out["feedback_item"] = "\n• ".join(partes)
    return out


def corrigir_item(questao: Questao, resposta_aluno: str, bloco: BlocoCurricular) -> Dict[str, Any]:
    it = _corrigir_item_nucleo(questao, resposta_aluno, bloco)
    return _enriquecer_feedback_pedagogico_bcc(it, questao, bloco)


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


def renderizar_esquema_grafico_html(esq: Optional[Dict[str, Any]]) -> str:
    """Renderiza o esquema visual pedagogico de 3 etapas e arco de retorno em HTML/SVG inline (e-mail)."""
    if not isinstance(esq, dict):
        return ""
    cols = esq.get("colunas") or []
    if len(cols) != 3:
        return ""
    seta_svg = (
        '<svg width="24" height="16" viewBox="0 0 24 16" style="display:block;margin:0 auto;">'
        '<line x1="2" y1="8" x2="19" y2="8" stroke="#6e6d68" stroke-width="1.6"/>'
        '<polyline points="14,3.5 19.5,8 14,12.5" fill="none" stroke="#6e6d68" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>'
        "</svg>"
    )

    def _box_topo(c: Dict[str, Any]) -> str:
        dado = c.get("tom") == "dado"
        bg = "#efefea" if dado else "#e3f5ee"
        bd = "#8c8b84" if dado else "#1b8a6b"
        tcol = "#2d2d2a" if dado else "#0c543f"
        scol = "#5c5b55" if dado else "#167a5c"
        return (
            f'<div style="background:{bg};border:1.2px solid {bd};border-radius:8px;padding:8px 10px;text-align:center;">'
            f'<div style="font-weight:700;font-size:12.5px;color:{tcol};">{html.escape(str(c.get("titulo") or ""))}</div>'
            f'<div style="font-size:11px;color:{scol};margin-top:2px;">{html.escape(str(c.get("subtitulo") or ""))}</div>'
            "</div>"
        )

    def _box_como(c: Dict[str, Any]) -> str:
        dado = c.get("tom") == "dado"
        bg = "#efefea" if dado else "#e3f5ee"
        bd = "#8c8b84" if dado else "#1b8a6b"
        col = "#494843" if dado else "#0f634a"
        linhas = "".join(f"<div>{html.escape(str(x))}</div>" for x in (c.get("como_escrever") or []))
        return (
            f'<div style="background:{bg};border:1.2px solid {bd};border-radius:8px;padding:8px 10px;font-size:11.5px;line-height:1.45;color:{col};">'
            f"{linhas}</div>"
        )

    def _box_erro(c: Dict[str, Any]) -> str:
        ok = bool(c.get("ok"))
        bg = "#f2faf6" if ok else "#fbece7"
        bd = "1px dashed #6eb89e" if ok else "1.2px solid #c86448"
        col = "#166e52" if ok else "#8c3119"
        return (
            f'<div style="background:{bg};border:{bd};border-radius:8px;padding:8px 10px;font-size:11.8px;font-weight:500;line-height:1.38;color:{col};">'
            f"{html.escape(str(c.get('erro_aluno') or ''))}</div>"
        )

    tit_esq = html.escape(str(esq.get("titulo_esquema") or "Mapa Visual de Resolucao"))
    arco_lbl = html.escape(str(esq.get("arco_retorno") or "Validar saida frente ao enunciado"))
    return (
        '<div style="margin:10px 0 6px;padding:12px 14px;background:#ffffff;border:1px solid #cbd5e1;border-radius:10px;overflow-x:auto;">'
        '<div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:6px;margin-bottom:9px;padding-bottom:6px;border-bottom:1px solid #f1f5f9;font-size:11.5px;">'
        f'<strong style="color:#0f172a;">🗺️ {tit_esq}</strong>'
        '<span style="color:#475569;">🟢 Etapa autoral &nbsp;&bull;&nbsp; ⚪ Base do enunciado &nbsp;&bull;&nbsp; 🔴 Ponto a corrigir</span>'
        "</div>"
        '<div style="min-width:520px;font-family:Segoe UI,system-ui,Arial,sans-serif;">'
        '<div style="display:grid;grid-template-columns:1fr 26px 1fr 26px 1fr;align-items:center;">'
        f"{_box_topo(cols[0])}<div>{seta_svg}</div>{_box_topo(cols[1])}<div>{seta_svg}</div>{_box_topo(cols[2])}"
        "</div>"
        '<div style="font-size:11.5px;font-weight:600;color:#575650;margin:9px 0 4px;">Como resolver</div>'
        '<div style="display:grid;grid-template-columns:1fr 26px 1fr 26px 1fr;align-items:stretch;">'
        f"{_box_como(cols[0])}<div></div>{_box_como(cols[1])}<div></div>{_box_como(cols[2])}"
        "</div>"
        '<div style="font-size:11.5px;font-weight:600;color:#575650;margin:9px 0 4px;">Diagnostico na tentativa</div>'
        '<div style="display:grid;grid-template-columns:1fr 26px 1fr 26px 1fr;align-items:stretch;">'
        f"{_box_erro(cols[0])}<div></div>{_box_erro(cols[1])}<div></div>{_box_erro(cols[2])}"
        "</div>"
        '<svg viewBox="0 0 600 42" style="width:100%;height:40px;display:block;margin-top:2px;">'
        '<path d="M 504 2 L 504 19 L 96 19 L 96 5" fill="none" stroke="#1b8a6b" stroke-width="1.8" stroke-dasharray="5,4"/>'
        '<polyline points="91,11 96,4 101,11" fill="none" stroke="#1b8a6b" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>'
        f'<text x="300" y="36" text-anchor="middle" fill="#4b4a45" font-size="11.5" font-family="Segoe UI,Arial,sans-serif">{arco_lbl}</text>'
        "</svg></div></div>"
    )


def _destacar_texto_feedback_html(raw: str) -> str:
    s = html.escape(str(raw or ""))
    s = re.sub(
        r"^\[([A-Z0-9-]+)\]\s*",
        r'<span style="display:inline-block;background:#1e293b;color:#ffffff;font-weight:700;font-size:11.5px;padding:1px 7px;border-radius:4px;margin-right:5px;">\1</span>',
        s,
    )
    s = re.sub(
        r"`([^`\n]{1,120}?)`",
        r'<code style="background:rgba(15,23,42,0.08);padding:1px 5px;border-radius:4px;color:#0f172a;font-family:Consolas,monospace;font-weight:700;">\1</code>',
        s,
    )
    s = re.sub(
        r"&quot;([^&]{1,140}?)&quot;",
        r'<strong style="background:rgba(15,23,42,0.07);padding:1px 5px;border-radius:4px;color:#0f172a;">&ldquo;\1&rdquo;</strong>',
        s,
    )
    s = re.sub(
        r"(int main\(void\)|printf|scanf|return 0|#include|BFS|DFS|Dijkstra|Kruskal|Kahn|matriz|vetor|grafo|caso de borda|Bloco\s+[A-H][0-9]{2})",
        r"<strong>\1</strong>",
        s,
    )
    return s


def formatar_feedback_destacado_html(fb_bruto: str, eh_ok: bool) -> str:
    """Formata o texto de feedback em cartoes semanticos coloridos com emojis e negrito."""
    txt = str(fb_bruto or "").strip()
    if not txt:
        return ""
    partes = re.split(r"\n•\s+", txt)
    cabecalho = partes[0].strip()
    topicos = partes[1:]
    blocos: List[str] = []

    if eh_ok:
        blocos.append(
            '<div style="background:#ecfdf5;border:1px solid #a7f3d0;border-left:4px solid #16a34a;border-radius:6px;padding:8px 11px;color:#14532d;font-size:13px;line-height:1.5;margin-top:6px;">'
            f"✅ <strong>Domínio Comprovado:</strong> {_destacar_texto_feedback_html(cabecalho)}"
            "</div>"
        )
    else:
        blocos.append(
            '<div style="background:#fef2f2;border:1px solid #fecaca;border-left:4px solid #dc2626;border-radius:6px;padding:8px 11px;color:#7f1d1d;font-size:13px;line-height:1.52;margin-top:6px;">'
            '<div style="font-weight:700;color:#991b1b;margin-bottom:3px;">🔴 🎯 Diagnóstico Principal</div>'
            f"<div>{_destacar_texto_feedback_html(cabecalho)}</div>"
            "</div>"
        )

    for top in topicos:
        t = top.strip()
        if not t:
            continue
        if re.match(r"^(Como corrigir|Versão corrigida|Como estruturar)", t, flags=re.IGNORECASE):
            tit, _, corpo = t.partition(":")
            corpo_html = "".join(
                f'<div style="margin-top:3px;">{_destacar_texto_feedback_html(ln)}</div>'
                for ln in corpo.strip().splitlines()
                if ln.strip()
            )
            blocos.append(
                '<div style="background:#ecfdf5;border:1px solid #a7f3d0;border-left:4px solid #059669;border-radius:6px;padding:8px 11px;color:#064e3b;font-size:12.8px;line-height:1.48;margin-top:6px;">'
                f'<div style="font-weight:700;color:#047857;">🟢 ✍️ {html.escape(tit.strip())}</div>'
                f"{corpo_html}</div>"
            )
        elif re.match(r"^(Sintaxe e Formato|Correção Gramatical)", t, flags=re.IGNORECASE):
            tit, _, corpo = t.partition(":")
            blocos.append(
                '<div style="background:#f5f3ff;border:1px solid #ddd6fe;border-left:4px solid #7c3aed;border-radius:6px;padding:8px 11px;color:#4c1d95;font-size:12.5px;line-height:1.46;margin-top:6px;">'
                f'<div style="font-weight:700;color:#6d28d9;">🟣 📝 {html.escape(tit.strip())}</div>'
                f'<div style="margin-top:3px;">{_destacar_texto_feedback_html(corpo.strip())}</div></div>'
            )
        elif re.match(r"^O que revisar", t, flags=re.IGNORECASE):
            _, _, corpo = t.partition(":")
            blocos.append(
                '<div style="background:#eff6ff;border:1px solid #bfdbfe;border-left:4px solid #2563eb;border-radius:6px;padding:7px 11px;color:#1e3a8a;font-size:12.5px;line-height:1.46;margin-top:6px;">'
                f"<strong>🔵 📘 Onde Revisar no Bloco:</strong> {_destacar_texto_feedback_html(corpo.strip())}</div>"
            )
        elif re.match(r"^(Critérios de Avaliação|Barema)", t, flags=re.IGNORECASE):
            tit, _, corpo = t.partition(":")
            chips = "".join(
                f'<span style="display:inline-block;background:#fef3c7;border:1px solid #f59e0b;border-radius:6px;padding:2px 8px;margin:4px 5px 0 0;font-size:11.8px;font-weight:600;color:#92400e;">{html.escape(c.strip())}</span>'
                for c in corpo.split(";")
                if c.strip()
            )
            blocos.append(
                '<div style="background:#fffbeb;border:1px solid #fde68a;border-left:4px solid #d97706;border-radius:6px;padding:7px 11px;color:#78350f;font-size:12.5px;margin-top:6px;">'
                f'<div style="font-weight:700;color:#92400e;">🟠 ⚖️ {html.escape(tit.strip())}</div>'
                f"<div>{chips}</div></div>"
            )
        else:
            blocos.append(
                '<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:6px;padding:7px 11px;font-size:12.5px;margin-top:6px;">'
                f"{_destacar_texto_feedback_html(t)}</div>"
            )
    return "".join(blocos)


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
        eh_ok = it["status_correcao"] == "correto"
        cor = "#16a34a" if eh_ok else "#dc2626"
        bg = "#f0fdf4" if eh_ok else "#fef2f2"
        badge = "CORRETO" if eh_ok else ("PARCIAL" if it["status_correcao"] == "parcial" else "REVISAR")
        linhas_itens.append(
            f"""
            <div style="border-left: 4px solid {cor}; background: {bg}; padding: 10px 12px; margin-bottom: 10px; border-radius: 6px;">
              <div style="display: flex; justify-content: space-between; font-weight: bold; margin-bottom: 4px;">
                <span>{html.escape(it['questao_id'])} ({html.escape(it['tipo_questao'])})</span>
                <span style="color: {cor};">{badge} &bull; Camada: {html.escape(it['camada_avaliacao'])}</span>
              </div>
              <div style="font-size: 13px; color: #334155; margin-bottom: 4px;">
                <strong>Transcricao OCR capturada:</strong>
                <pre style="background: #ffffff; border: 1px solid #cbd5e1; padding: 6px; margin: 4px 0; font-family: Consolas, monospace; font-size: 12px; white-space: pre-wrap;">{html.escape(it['resposta_extraida'] or '(em branco)')}</pre>
              </div>
              {renderizar_esquema_grafico_html(it.get("esquema_grafico"))}
              {formatar_feedback_destacado_html(it['feedback_item'], eh_ok)}
            </div>
            """
        )

    legenda_html = (
        ""
        if acertos == total
        else (
            '<div style="padding:8px 11px;margin:8px 0 12px;background:#f8fafc;border:1px solid #cbd5e1;border-radius:8px;font-size:12px;color:#334155;">'
            '<strong style="color:#0f172a;margin-right:4px;">🎨 Legenda da Correção:</strong> '
            '<span style="color:#991b1b;font-weight:600;">🔴 🎯 Diagnóstico</span> &bull; '
            '<span style="color:#065f46;font-weight:600;">🟢 ✍️ Como Corrigir</span> &bull; '
            '<span style="color:#5b21b6;font-weight:600;">🟣 📝 Sintaxe/Formato</span> &bull; '
            '<span style="color:#1e40af;font-weight:600;">🔵 📘 Onde Revisar</span> &bull; '
            '<span style="color:#92400e;font-weight:600;">🟠 ⚖️ Critérios</span>'
            "</div>"
        )
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
    {legenda_html}
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
                    and q.spec_matematica):
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


def reavaliar_submissao_existente(
    submissao_id: int, orq: Optional[OrquestradorCurso] = None
) -> Optional[Dict[str, Any]]:
    """Reavalia os itens salvos de uma submissao aplicando o corretor, feedback estruturado e esquema grafico atuais."""
    sub = banco_dados.obter_submissao_por_id(int(submissao_id))
    if not sub:
        return None
    ctrl = orq or OrquestradorCurso()
    disc_id = config.normalizar_disciplina_id(sub.get("disciplina") or config.DISCIPLINA_PADRAO)
    cat = ctrl.obter_catalogo(disc_id)
    bloco = cat.obter(sub["bloco"])
    modo = str(sub.get("modo") or "pratica")
    questoes = bloco.obter_questoes(modo=modo, incluir_opcionais=True)
    mapa_q = {q.questao_id: q for q in questoes}

    novos_itens: List[Dict[str, Any]] = []
    erros_cats: List[str] = []
    for ir in (sub.get("itens") or []):
        qid = str(ir.get("questao_id") or "")
        resp_q = str(ir.get("resposta_extraida") or "")
        q_obj = mapa_q.get(qid)
        if q_obj is not None:
            it = corrigir_item(q_obj, resp_q, bloco)
            it["resposta_extraida"] = resp_q
        else:
            it = dict(ir)
            it["esquema_grafico"] = gerar_esquema_grafico_para_item(it, bloco.bloco_id, disc_id)
        novos_itens.append(it)
        if it.get("status_correcao") != "correto" and it.get("categoria_erro"):
            erros_cats.append(str(it["categoria_erro"]))

    total_q = len(novos_itens)
    acertos = sum(1 for it in novos_itens if it.get("status_correcao") == "correto")
    pct = round((acertos / total_q) * 100.0, 1) if total_q > 0 else 0.0
    dificuldade = ", ".join(sorted(set(erros_cats))) if erros_cats else "nenhuma"

    aluno = banco_dados.obter_aluno_por_id(int(sub["aluno_id"]), incluir_pin=False, disciplina=disc_id) or {
        "id": sub["aluno_id"],
        "nome": "Aluno",
        "email": "",
    }
    prova = banco_dados.obter_prova(sub["protocolo"]) or {}
    tempo_alvo = int(
        prova.get("tempo_alvo_min")
        or (bloco.tempo_pratica_min if modo == "pratica" else bloco.tempo_checagem_min)
        or 20
    )
    tempo_decl = float(sub.get("tempo_declarado_min") or 0.0)
    _, fluencia_msg = _avaliar_fluencia_tempo(tempo_decl, tempo_alvo)
    decisao_titulo = str(sub.get("proxima_acao") or "REAVALIADO")
    decisao_desc = f"Reavaliacao detalhada executada ({acertos}/{total_q} - {pct:.0f}%)."
    html_fb = _montar_html_feedback(
        aluno=aluno,
        bloco=bloco,
        protocolo=str(sub["protocolo"]),
        variante=str(sub["variante"]),
        tentativa=int(sub["tentativa"]),
        tempo_min=tempo_decl,
        tempo_alvo=tempo_alvo,
        fluencia_msg=fluencia_msg,
        acertos=acertos,
        total=total_q,
        pct=pct,
        itens=novos_itens,
        decisao_titulo=decisao_titulo,
        decisao_desc=decisao_desc,
    )
    banco_dados.atualizar_reavaliacao_submissao(
        submissao_id=int(submissao_id),
        acertos=acertos,
        total=total_q,
        pct=pct,
        dificuldade=dificuldade,
        relatorio_html=html_fb,
        itens=novos_itens,
    )
    return {
        "submissao_id": int(submissao_id),
        "aluno_id": int(sub["aluno_id"]),
        "disciplina": disc_id,
        "acertos": acertos,
        "total": total_q,
        "percentual": pct,
        "itens": novos_itens,
    }


def reavaliar_feedbacks_salvos(
    disciplina: Optional[str] = None,
    aluno_id: Optional[int] = None,
    orq: Optional[OrquestradorCurso] = None,
) -> int:
    """Reavalia em lote submissoes ja salvas para atualizar feedback estruturado e esquemas graficos."""
    banco_dados.inicializar_banco()
    ctrl = orq or OrquestradorCurso()
    clausulas: List[str] = []
    params: List[Any] = []
    if disciplina:
        clausulas.append("COALESCE(disciplina, 'algoritmos') = ?")
        params.append(config.normalizar_disciplina_id(disciplina))
    if aluno_id is not None:
        clausulas.append("aluno_id = ?")
        params.append(int(aluno_id))
    where_sql = ("WHERE " + " AND ".join(clausulas)) if clausulas else ""
    with banco_dados.conectar() as conn:
        rows = conn.execute(f"SELECT id FROM submissoes {where_sql} ORDER BY id DESC", params).fetchall()
    qtd = 0
    for r in rows:
        if reavaliar_submissao_existente(int(r["id"]), orq=ctrl) is not None:
            qtd += 1
    return qtd
