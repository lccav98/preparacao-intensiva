#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Catalogo curricular dinamico do Curso de Preparação Intensiva em Algoritmos em C (UTFPR-PG).
Carrega todos os 73 blocos, gabaritos, solucoes C99, casos JSON e o DAG de pre-requisitos.
"""

import json
import os
import re
from dataclasses import dataclass, field
from typing import Dict, List, Optional

import config

ORDEM_BLOCOS: List[str] = []
for _dir, _prefix, _total, _titulo in config.ESTAGIOS_META:
    for _i in range(1, _total + 1):
        ORDEM_BLOCOS.append(f"{_prefix}{_i:02d}")


def ordem_blocos_disciplina(disciplina: str = config.DISCIPLINA_PADRAO) -> List[str]:
    disc = config.obter_disciplina(disciplina)
    ordem: List[str] = []
    for _dir, _prefix, _total, _titulo in disc["estagios_meta"]:
        for _i in range(1, _total + 1):
            ordem.append(f"{_prefix}{_i:02d}")
    return ordem


@dataclass
class Questao:
    questao_id: str
    titulo: str
    tipo: str  # 'mesa', 'lacuna', 'bug', 'codigo', 'conceitual', 'calculo', 'matriz', 'sistema', 'vetor', 'geometria', 'conica'
    modo: str  # 'pratica' | 'checagem'
    opcional: bool
    enunciado_md: str
    gabarito_md: str = ""
    codigo_referencia: str = ""
    casos_teste: List[dict] = field(default_factory=list)
    spec_matematica: Optional[dict] = None
    rubrica: Optional[dict] = None


@dataclass
class BlocoCurricular:
    bloco_id: str
    estagio_dir: str
    estagio_letra: str
    titulo: str
    micro_habilidade: str
    pre_requisitos: List[str]
    tempo_pratica_min: int
    tempo_checagem_min: int
    restricao_escopo: str
    instrucoes_curtas_md: str
    exemplos_md: str
    questoes_pratica: List[Questao] = field(default_factory=list)
    questoes_checagem: List[Questao] = field(default_factory=list)
    tolerancia_numerica: float = 0.01
    disciplina: str = "algoritmos"
    periodo: int = 1
    carga_horaria: int = 60
    material_apoio: List[str] = field(default_factory=list)

    def obter_questoes(self, modo: str = "checagem", incluir_opcionais: bool = False) -> List[Questao]:
        base = self.questoes_checagem if modo == "checagem" else self.questoes_pratica
        if incluir_opcionais:
            return list(base)
        return [q for q in base if not q.opcional]

    def tempo_alvo(self, modo: str = "checagem") -> int:
        return self.tempo_checagem_min if modo == "checagem" else self.tempo_pratica_min


_JSON_PERIODO_CACHE: Dict[str, tuple[float, dict]] = {}


def _carregar_json_periodo(arquivo_json: str) -> dict:
    mtime = os.path.getmtime(arquivo_json) if os.path.isfile(arquivo_json) else -1.0
    cached = _JSON_PERIODO_CACHE.get(arquivo_json)
    if cached and cached[0] == mtime:
        return cached[1]
    with open(arquivo_json, "r", encoding="utf-8") as f:
        data = json.load(f)
    _JSON_PERIODO_CACHE[arquivo_json] = (mtime, data)
    return data


def _carregar_bloco_json(bloco_id: str, disc: dict) -> BlocoCurricular:
    disc_id = disc["id"]
    arq = disc.get("arquivo_json", "")
    if not arq or not os.path.isfile(arq):
        raise FileNotFoundError(f"Arquivo curricular JSON nao encontrado para '{disc_id}': {arq}")
    dados = _carregar_json_periodo(arq)
    blocos_list = ((dados.get("disciplinas") or {}).get(disc_id) or {}).get("blocos") or []
    alvo = None
    for b in blocos_list:
        if str(b.get("bloco_id", "")).strip().upper() == bloco_id:
            alvo = b
            break
    if alvo is None:
        raise KeyError(f"Bloco '{bloco_id}' nao encontrado em '{disc_id}' ({arq})")

    def _conv_questoes(raw_qs: list, modo: str) -> List[Questao]:
        qs: List[Questao] = []
        for q in (raw_qs or []):
            qid = str(q["questao_id"]).strip().upper()
            opc = bool(q.get("opcional", False)) or ("-OP" in qid)
            qs.append(
                Questao(
                    questao_id=qid,
                    titulo=str(q.get("titulo") or qid).strip(),
                    tipo=str(q.get("tipo") or "conceitual").strip().lower(),
                    modo=modo,
                    opcional=opc,
                    enunciado_md=str(q.get("enunciado_md") or "").strip(),
                    gabarito_md=str(q.get("gabarito_md") or "").strip(),
                    codigo_referencia=str(q.get("codigo_referencia") or "").strip(),
                    casos_teste=list(q.get("casos_teste") or []),
                    spec_matematica=q.get("spec_matematica"),
                    rubrica=q.get("rubrica"),
                )
            )
        return qs

    letra = str(alvo.get("estagio_letra") or bloco_id[0]).strip().upper()
    est_meta = [m for m in disc["estagios_meta"] if m[1] == letra]
    est_dir = est_meta[0][0] if est_meta else f"estagio_{letra}"

    return BlocoCurricular(
        bloco_id=bloco_id,
        estagio_dir=os.path.join(disc["curso_dir"], est_dir),
        estagio_letra=letra,
        titulo=str(alvo.get("titulo") or f"Bloco {bloco_id}").strip(),
        micro_habilidade=str(alvo.get("micro_habilidade") or "").strip(),
        pre_requisitos=[str(p).strip().upper() for p in (alvo.get("pre_requisitos") or [])],
        tempo_pratica_min=int(alvo.get("tempo_pratica_min") or 22),
        tempo_checagem_min=int(alvo.get("tempo_checagem_min") or 18),
        restricao_escopo=str(alvo.get("restricao_escopo") or "").strip(),
        instrucoes_curtas_md=str(alvo.get("instrucoes_curtas_md") or "").strip(),
        exemplos_md=str(alvo.get("exemplos_md") or "").strip(),
        questoes_pratica=_conv_questoes(alvo.get("questoes_pratica") or [], "pratica"),
        questoes_checagem=_conv_questoes(alvo.get("questoes_checagem") or [], "checagem"),
        tolerancia_numerica=float(alvo.get("tolerancia_numerica") or 0.01),
        disciplina=disc_id,
        periodo=int(disc.get("periodo", 1)),
        carga_horaria=int(disc.get("carga_horaria", 60)),
        material_apoio=list(disc.get("material_apoio") or []),
    )


def _inferir_tipo_questao(
    titulo: str,
    enunciado: str,
    tem_casos_json: bool,
    disciplina: str = "algoritmos",
    spec_mat: Optional[dict] = None,
) -> str:
    t_low = titulo.lower()
    if disciplina == "matrizes_vetores":
        if spec_mat:
            tr = str(spec_mat.get("tipo_resposta", "")).lower()
            if tr == "matriz":
                return "matriz"
            if tr in ("vetor", "conjunto_vetores"):
                return "vetor"
            if tr in ("plano", "reta"):
                return "geometria"
            if tr == "equacao_algebrica":
                return "conica"
            if tr == "classificacao":
                return "conceitual"
        if any(k in t_low for k in ["matriz", "transposta", "inversa", "determinante"]):
            return "matriz"
        if any(k in t_low for k in ["sistema", "escalonamento", "posto", "gauss"]):
            return "sistema"
        if any(k in t_low for k in ["vetor", "produto", "area", "área", "volume"]):
            return "vetor"
        if any(k in t_low for k in ["reta", "plano", "distancia", "distância"]):
            return "geometria"
        if any(k in t_low for k in ["parabola", "parábola", "elipse", "hiperbole", "hipérbole", "conica", "cônica", "quadrica", "quádrica"]):
            return "conica"
        return "calculo"

    if "caça ao bug" in t_low or "caca ao bug" in t_low or "depuração" in t_low or "corrija" in t_low:
        return "bug"
    if "completar" in t_low or "lacuna" in t_low or "/* a */" in enunciado.lower():
        return "lacuna"
    if "teste de mesa" in t_low or "rastreamento" in t_low or "tabela-verdade" in t_low or "previsão" in t_low or "papel" in t_low:
        return "mesa"
    if tem_casos_json or "programa completo" in t_low or "escrita independente" in t_low or "escreva um programa" in enunciado.lower():
        return "codigo"
    if "conceitual" in t_low or "análise" in t_low or "analise" in t_low:
        return "conceitual"
    return "mesa"


def _extrair_secao(texto: str, inicio_regex: str, fim_regex: str) -> str:
    m_ini = re.search(inicio_regex, texto, re.MULTILINE)
    if not m_ini:
        return ""
    pos_ini = m_ini.end()
    m_fim = re.search(fim_regex, texto[pos_ini:], re.MULTILINE)
    if not m_fim:
        return texto[pos_ini:].strip()
    return texto[pos_ini:pos_ini + m_fim.start()].strip()


def _parse_gabarito_itens(gabarito_txt: str, bloco_id: str) -> Dict[str, str]:
    itens: Dict[str, str] = {}
    padrao = re.compile(rf"^###\s+.*?(`?{re.escape(bloco_id)}-(?:E|C|OP)\d+`?[^\n]*)$", re.MULTILINE)
    matches = list(padrao.finditer(gabarito_txt))
    for idx, m in enumerate(matches):
        qid_m = re.search(rf"({re.escape(bloco_id)}-(?:E|C|OP)\d+)", m.group(1))
        if not qid_m:
            continue
        qid = qid_m.group(1)
        start = m.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(gabarito_txt)
        chunk = gabarito_txt[start:end].strip()
        # Cortar em separador de secao principal (## )
        sec_cut = re.search(r"^##\s+\d+\.", chunk, re.MULTILINE)
        if sec_cut:
            chunk = chunk[:sec_cut.start()].strip()
        itens[qid] = chunk.strip()
    return itens


def _extrair_codigo_c(texto: str) -> str:
    blocos = re.findall(r"```c\s*\n(.*?)```", texto, re.DOTALL)
    return "\n\n".join(b.strip() for b in blocos) if blocos else ""


def _carregar_json_testes(
    testes_dir: str, bloco_id: str
) -> tuple[float, Dict[str, List[dict]], Dict[str, dict]]:
    json_path = os.path.join(testes_dir, f"casos_{bloco_id}.json")
    por_qid: Dict[str, List[dict]] = {}
    specs_mat: Dict[str, dict] = {}
    tol = 0.01
    if not os.path.isfile(json_path):
        return tol, por_qid, specs_mat

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, dict):
        tol = float(data.get("tolerancia_numerica", 0.01))
        casos_map = data.get("casos_por_arquivo", {})
        for arq_nome, lista_casos in casos_map.items():
            # Exemplo: B05_E03_corrigido.c -> B05-E03 | B06_C02.c -> B06-C02
            m = re.search(rf"{re.escape(bloco_id)}[_-]((?:E|C|OP)\d+)", arq_nome)
            if m:
                qid = f"{bloco_id}-{m.group(1)}"
                por_qid[qid] = lista_casos
            elif lista_casos:
                m_id = re.search(rf"({re.escape(bloco_id)}-(?:E|C|OP)\d+)", str(lista_casos[0].get("id", "")))
                if m_id:
                    por_qid[m_id.group(1)] = lista_casos

        questoes_mat = data.get("questoes", {})
        if isinstance(questoes_mat, dict):
            for qid, spec in questoes_mat.items():
                if isinstance(spec, dict):
                    specs_mat[str(qid).upper().strip()] = spec
    elif isinstance(data, list):
        for tc in data:
            m_id = re.search(rf"({re.escape(bloco_id)}-(?:E|C|OP)\d+)", str(tc.get("id", tc.get("exercicio", ""))))
            if m_id:
                por_qid.setdefault(m_id.group(1), []).append(tc)
    return tol, por_qid, specs_mat


def carregar_bloco(
    bloco_id: str,
    disciplina: str = config.DISCIPLINA_PADRAO,
) -> BlocoCurricular:
    disc_id = config.normalizar_disciplina_id(disciplina)
    disc = config.obter_disciplina(disc_id)
    bloco_id = str(bloco_id or "").strip().upper()
    if disc.get("fonte") == "json":
        return _carregar_bloco_json(bloco_id, disc)
    letra = bloco_id[0]
    estagio_meta = [m for m in disc["estagios_meta"] if m[1] == letra]
    if not estagio_meta:
        raise KeyError(f"Estagio desconhecido para bloco '{bloco_id}' na disciplina '{disc_id}'")
    estagio_dir_name = estagio_meta[0][0]
    estagio_dir = os.path.join(disc["curso_dir"], estagio_dir_name)

    bloco_path = os.path.join(estagio_dir, "blocos", f"{bloco_id}_bloco.md")
    gab_path = os.path.join(estagio_dir, "gabaritos", f"{bloco_id}_gabarito.md")
    testes_dir = os.path.join(estagio_dir, "testes")

    with open(bloco_path, "r", encoding="utf-8") as f:
        txt = f.read()

    gab_txt = ""
    if os.path.isfile(gab_path):
        with open(gab_path, "r", encoding="utf-8") as f:
            gab_txt = f.read()

    gab_itens = _parse_gabarito_itens(gab_txt, bloco_id)
    tol, json_por_qid, specs_mat = _carregar_json_testes(testes_dir, bloco_id)

    # Titulo
    m_tit = re.search(r"^#\s+(.+)$", txt, re.MULTILINE)
    titulo = m_tit.group(1).strip() if m_tit else f"Bloco {bloco_id}"

    # Tabela de especificacoes
    m_micro = re.search(r"\|\s*\*\*Micro-habilidade foco\*\*\s*\|\s*(.+?)\s*\|", txt)
    micro = m_micro.group(1).strip() if m_micro else ""

    m_pre = re.search(r"\|\s*\*\*Pré-requisitos?\*\*\s*\|\s*(.+?)\s*\|", txt)
    pre_raw = m_pre.group(1) if m_pre else ""
    pre_reqs = [p for p in re.findall(r"\b([A-H]\d{2})\b", pre_raw) if p != bloco_id]

    m_rest = re.search(r"\|\s*\*\*Restrição de escopo\*\*\s*\|\s*(.+?)\s*\|", txt)
    restricao = m_rest.group(1).strip() if m_rest else ""

    m_tempo = re.search(r"^\|\s*\*\*Tempo estimado[^|]*\|\s*(.+?)\s*\|\s*$", txt, re.MULTILINE)
    tempo_raw = m_tempo.group(1) if m_tempo else ""
    tempos_nums = [int(n) for n in re.findall(r"(\d+)\s*min", tempo_raw)]
    tempo_pratica = tempos_nums[0] if tempos_nums else 22
    m_chk_t = re.search(r"Checagem\s*\([^)]*?(\d+)\s*min", tempo_raw)
    tempo_checagem = int(m_chk_t.group(1)) if m_chk_t else 18

    # Secoes 1 e 2
    inst_md = _extrair_secao(txt, r"^##\s+1\.\s+Instruções\s+Curtas[^\n]*\n", r"^##\s+2\.")
    ex_md = _extrair_secao(txt, r"^##\s+2\.\s+Exemplos\s+Guiados[^\n]*\n", r"^##\s+3\.")

    # Secoes 3 (Pratica) e 4 (Checagem)
    sec3_md = _extrair_secao(txt, r"^##\s+3\.\s+Exercícios[^\n]*\n", r"^##\s+4\.")
    sec4_md = _extrair_secao(txt, r"^##\s+4\.\s+Checagem[^\n]*\n", r"^##\s+5\.")

    def parse_questoes(secao_txt: str, modo: str) -> List[Questao]:
        res: List[Questao] = []
        pad = re.compile(rf"^###\s+.*?(`?{re.escape(bloco_id)}-(?:E|C|OP)\d+`?[^\n]*)$", re.MULTILINE)
        matches = list(pad.finditer(secao_txt))
        for idx, m in enumerate(matches):
            cab = m.group(1).strip()
            qid_m = re.search(rf"({re.escape(bloco_id)}-(?:E|C|OP)\d+)", cab)
            if not qid_m:
                continue
            qid = qid_m.group(1)
            start = m.end()
            end = matches[idx + 1].start() if idx + 1 < len(matches) else len(secao_txt)
            body = secao_txt[start:end].strip()
            body = re.sub(r"\n---\s*$", "", body).strip()
            opcional = "opcional" in cab.lower() or "op" in qid.lower()
            casos = json_por_qid.get(qid, [])
            spec_mat = specs_mat.get(qid.upper())
            gab_item = gab_itens.get(qid, "")
            cod_ref = _extrair_codigo_c(gab_item) if disc_id == "algoritmos" else ""
            tipo = _inferir_tipo_questao(
                cab, body, len(casos) > 0, disciplina=disc_id, spec_mat=spec_mat
            )
            res.append(
                Questao(
                    questao_id=qid,
                    titulo=cab.replace("`", ""),
                    tipo=tipo,
                    modo=modo,
                    opcional=opcional,
                    enunciado_md=body,
                    gabarito_md=gab_item,
                    codigo_referencia=cod_ref,
                    casos_teste=casos,
                    spec_matematica=spec_mat,
                )
            )
        return res

    q_pratica = parse_questoes(sec3_md, "pratica")
    q_checagem = parse_questoes(sec4_md, "checagem")

    return BlocoCurricular(
        bloco_id=bloco_id,
        estagio_dir=estagio_dir,
        estagio_letra=letra,
        titulo=titulo,
        micro_habilidade=micro,
        pre_requisitos=pre_reqs,
        tempo_pratica_min=tempo_pratica,
        tempo_checagem_min=tempo_checagem,
        restricao_escopo=restricao,
        instrucoes_curtas_md=inst_md,
        exemplos_md=ex_md,
        questoes_pratica=q_pratica,
        questoes_checagem=q_checagem,
        tolerancia_numerica=tol,
        disciplina=disc_id,
        periodo=int(disc.get("periodo", 1)),
        carga_horaria=int(disc.get("carga_horaria", 60)),
        material_apoio=list(disc.get("material_apoio") or []),
    )


class CatalogoCurricular:
    """Cache em memoria de todos os blocos curriculares de uma disciplina."""

    def __init__(self, disciplina: str = config.DISCIPLINA_PADRAO):
        self.disciplina = config.normalizar_disciplina_id(disciplina)
        self.ordem_blocos: List[str] = ordem_blocos_disciplina(self.disciplina)
        self.total_blocos: int = len(self.ordem_blocos)
        self._blocos: Dict[str, BlocoCurricular] = {}

    def carregar_todos(self) -> Dict[str, BlocoCurricular]:
        for bid in self.ordem_blocos:
            if bid not in self._blocos:
                self._blocos[bid] = carregar_bloco(bid, disciplina=self.disciplina)
        return self._blocos

    def obter(self, bloco_id: str) -> BlocoCurricular:
        bid = str(bloco_id or "").strip().upper()
        if bid not in self._blocos:
            self._blocos[bid] = carregar_bloco(bid, disciplina=self.disciplina)
        return self._blocos[bid]

    def proximo_bloco(self, bloco_id: str) -> Optional[str]:
        bid = str(bloco_id or "").strip().upper()
        if bid not in self.ordem_blocos:
            return None
        idx = self.ordem_blocos.index(bid)
        return self.ordem_blocos[idx + 1] if idx + 1 < len(self.ordem_blocos) else None

    def bloco_recuo_prerequisito(self, bloco_id: str) -> str:
        """Retorna o bloco pre-requisito principal para investigacao apos 2 falhas."""
        bid = str(bloco_id or "").strip().upper()
        bloco = self.obter(bid)
        if bloco.pre_requisitos:
            return bloco.pre_requisitos[0]
        if bid in self.ordem_blocos:
            idx = self.ordem_blocos.index(bid)
            return self.ordem_blocos[max(0, idx - 1)]
        return self.ordem_blocos[0]

    def resumo_mapa(self) -> List[dict]:
        self.carregar_todos()
        out = []
        for bid in self.ordem_blocos:
            b = self._blocos[bid]
            out.append(
                {
                    "bloco_id": b.bloco_id,
                    "estagio": b.estagio_letra,
                    "titulo": b.titulo,
                    "micro_habilidade": b.micro_habilidade,
                    "pre_requisitos": b.pre_requisitos,
                    "tempo_pratica_min": b.tempo_pratica_min,
                    "tempo_checagem_min": b.tempo_checagem_min,
                    "qtd_pratica": len(b.questoes_pratica),
                    "qtd_checagem": len([q for q in b.questoes_checagem if not q.opcional]),
                }
            )
        return out
