#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador da Folha de Prova A4 Imprimivel (HTML/CSS @media print) com protocolo OCR,
campos de controle de tempo, renderizacao matematica offline para MAT121
e caixas delimitadas para escrita manuscrita.
"""

import hashlib
import html
import os
import re
import time
from typing import Any, Dict, List

import markdown

import config
from catalogo_curricular import BlocoCurricular, Questao


def gerar_protocolo(
    aluno_id: int,
    bloco_id: str,
    variante: str,
    tentativa: int,
    modo: str,
    disciplina: str = "algoritmos",
) -> str:
    disc = config.obter_disciplina(disciplina)
    pref = disc["prefixo_protocolo"]
    seed = f"{disc['id']}-{aluno_id}-{bloco_id}-{variante}-T{tentativa}-{modo}-{time.time_ns()}"
    suf = hashlib.sha1(seed.encode("utf-8")).hexdigest()[:6].upper()
    return f"{pref}-{bloco_id}-{variante}-T{tentativa}-{suf}"


_LATEX_SIMBOLOS = [
    (r"\\operatorname\{sen\}", "sen"),
    (r"\\operatorname\{([a-zA-Z]+)\}", r"\1"),
    (r"\\mathbb\{R\}", "ℝ"),
    (r"\\mathbb\{N\}", "ℕ"),
    (r"\\mathbb\{Z\}", "ℤ"),
    (r"\\imath", "i"),
    (r"\\jmath", "j"),
    (r"\\alpha", "α"),
    (r"\\beta", "β"),
    (r"\\gamma", "γ"),
    (r"\\theta", "θ"),
    (r"\\phi", "φ"),
    (r"\\lambda", "λ"),
    (r"\\mu", "μ"),
    (r"\\pi", "π"),
    (r"\\Delta", "Δ"),
    (r"\\Sigma", "Σ"),
    (r"\\varepsilon", "ε"),
    (r"\\cdot", " · "),
    (r"\\times", " × "),
    (r"\\perp", " ⊥ "),
    (r"\\parallel", " ∥ "),
    (r"\\nparallel", " ∦ "),
    (r"\\notin", " ∉ "),
    (r"\\in", " ∈ "),
    (r"\\neq", " ≠ "),
    (r"\\leq", " ≤ "),
    (r"\\geq", " ≥ "),
    (r"\\equiv", " ≡ "),
    (r"\\sim", " ~ "),
    (r"\\pm", "±"),
    (r"\\Longleftrightarrow|\\Leftrightarrow", " ⇔ "),
    (r"\\Longrightarrow|\\Rightarrow|\\implies", " ⇒ "),
    (r"\\rightarrow|\\to", " → "),
    (r"\\leftarrow", " ← "),
    (r"\\leftrightarrow|\\iff", " ↔ "),
    (r"\\land|\\wedge", " ∧ "),
    (r"\\lor|\\vee", " ∨ "),
    (r"\\lnot|\\neg", "¬"),
    (r"\\forall", "∀"),
    (r"\\exists", "∃"),
    (r"\\subseteq", " ⊆ "),
    (r"\\subset", " ⊂ "),
    (r"\\supseteq", " ⊇ "),
    (r"\\cup", " ∪ "),
    (r"\\cap", " ∩ "),
    (r"\\setminus", " ∖ "),
    (r"\\vdash", " ⊢ "),
    (r"\\models", " ⊨ "),
    (r"\\approx", " ≈ "),
    (r"\\cong", " ≅ "),
    (r"\\propto", " ∝ "),
    (r"\\sum", "∑"),
    (r"\\prod", "∏"),
    (r"\\int", "∫"),
    (r"\\lim", "lim"),
    (r"\\partial", "∂"),
    (r"\\nabla", "∇"),
    (r"\\Theta", "Θ"),
    (r"\\Omega", "Ω"),
    (r"\\rho", "ρ"),
    (r"\\omega", "ω"),
    (r"\\sigma", "σ"),
    (r"\\mathbb\{Q\}", "ℚ"),
    (r"\\mathbb\{C\}", "ℂ"),
    (r"\\mathcal\{O\}", "O"),
    (r"\\overline\{([^{}]+)\}", r'<span style="text-decoration:overline;">\1</span>'),
    (r"\\emptyset", "∅"),
    (r"\\infty", "∞"),
    (r"\\quad", "&nbsp;&nbsp;"),
    (r"\\;", "&nbsp;"),
    (r"\\,", ""),
    (r"\\left", ""),
    (r"\\right", ""),
    (r"\\mid", " | "),
    (r"\\circ", "°"),
    (r"\\sin", "sen"),
    (r"\\cos", "cos"),
    (r"\\tan", "tg"),
    (r"\\arccos", "arccos"),
]


def _tex_para_html_inline(tex: str, _escaped: bool = False) -> str:
    """Converte expressao LaTeX matematica comum (matrizes, fracoes, raizes, vetores) para HTML offline."""
    s = tex.strip() if _escaped else html.escape(tex.strip())

    # \begin{bmatrix} / pmatrix / vmatrix / cases
    def _conv_env(m: re.Match) -> str:
        env = m.group(1)
        corpo = m.group(2).strip()
        linhas = [ln.strip() for ln in re.split(r"\\\\|\n", corpo) if ln.strip()]
        trs = []
        for ln in linhas:
            cols = [c.strip() for c in ln.split("&amp;")]
            tds = "".join(f"<td>{_tex_para_html_inline(c, _escaped=True)}</td>" for c in cols)
            trs.append(f"<tr>{tds}</tr>")
        if env == "vmatrix":
            cls = "m-grid m-det"
        elif env == "pmatrix":
            cls = "m-grid m-par"
        elif env == "cases":
            cls = "m-grid m-cases"
        else:
            cls = "m-grid m-bmat"
        return f'<table class="{cls}" cellspacing="0" cellpadding="0">{"".join(trs)}</table>'

    s = re.sub(
        r"\\begin\{(bmatrix|pmatrix|vmatrix|cases)\}(.*?)\\end\{\1\}",
        _conv_env,
        s,
        flags=re.DOTALL,
    )

    # \overrightarrow{AB} e \vec{v} e \hat{v}
    s = re.sub(r"\\overrightarrow\{([^{}]+)\}", r'<span class="vec">\1</span>', s)
    s = re.sub(r"\\vec\{([^{}]+)\}", r'<span class="vec">\1</span>', s)
    s = re.sub(r"\\hat\{([^{}]+)\}", r'<span class="hat">\1</span>', s)

    # \frac{a}{b} (de dentro para fora)
    for _ in range(4):
        novo = re.sub(
            r"\\(?:d|t)?frac\{([^{}]+)\}\{([^{}]+)\}",
            lambda mf: f'<span class="frac"><span class="f-num">{mf.group(1)}</span><span class="f-den">{mf.group(2)}</span></span>',
            s,
        )
        if novo == s:
            break
        s = novo

    # \sqrt{...}
    for _ in range(3):
        novo = re.sub(
            r"\\sqrt\{([^{}]+)\}",
            r'√<span class="sqrt-rad">\1</span>',
            s,
        )
        if novo == s:
            break
        s = novo

    # \mathbf{...}, \text{...}
    s = re.sub(r"\\mathbf\{([^{}]+)\}", r"<strong>\1</strong>", s)
    s = re.sub(r"\\text\{([^{}]+)\}", r'<span class="m-txt">\1</span>', s)

    for pad, sub in _LATEX_SIMBOLOS:
        s = re.sub(pad, sub, s)

    # Sobrescritos ^{...} e ^x; subscritos _{...} e _x
    s = re.sub(r"\^\{([^{}]+)\}", r"<sup>\1</sup>", s)
    s = re.sub(r"\^([a-zA-Z0-9T])", r"<sup>\1</sup>", s)
    s = re.sub(r"_\{([^{}]+)\}", r"<sub>\1</sub>", s)
    s = re.sub(r"_([a-zA-Z0-9])", r"<sub>\1</sub>", s)

    s = s.replace("{", "").replace("}", "")
    return f'<span class="math">{s}</span>'


def _render_md_matematica(texto: str) -> str:
    """Protege blocos $...$ e $$...$$ antes de passar ao parser Markdown e renderiza em HTML limpo."""
    placeholders: Dict[str, str] = {}
    contador = 0

    def _guardar(val_html: str) -> str:
        nonlocal contador
        chave = f"MATHPH{contador}ENDPH"
        contador += 1
        placeholders[chave] = val_html
        return chave

    # Proteger blocos de codigo antes para nao mexer em exemplos ```...```
    texto_proc = str(texto or "")
    code_phs: Dict[str, str] = {}

    def _stash_code(m: re.Match) -> str:
        k = f"CODEPH{len(code_phs)}ENDPH"
        code_phs[k] = m.group(0)
        return k

    texto_proc = re.sub(r"```.*?```|`[^`\n]+`", _stash_code, texto_proc, flags=re.DOTALL)

    # 1) Bloco $$ ... $$
    texto_proc = re.sub(
        r"\$\$(.*?)\$\$",
        lambda m: _guardar(f'<div class="math-block">{_tex_para_html_inline(m.group(1))}</div>'),
        texto_proc,
        flags=re.DOTALL,
    )
    # 2) Inline $ ... $
    texto_proc = re.sub(
        r"\$([^\n$]+?)\$",
        lambda m: _guardar(_tex_para_html_inline(m.group(1))),
        texto_proc,
    )

    # Restaurar trechos de codigo antes de rodar markdown
    for k, v in code_phs.items():
        texto_proc = texto_proc.replace(k, v)

    rendered = markdown.markdown(
        texto_proc,
        extensions=["fenced_code", "tables", "nl2br"],
    )
    for k, v in placeholders.items():
        rendered = rendered.replace(k, v)
    return rendered


def _render_md(texto: str, disciplina: str = "algoritmos") -> str:
    try:
        tipo_av = config.obter_disciplina(disciplina).get("tipo_avaliacao", "")
    except Exception:
        tipo_av = ""
    if tipo_av in ("matematica", "matematica_geral", "logica_matematica") or ("$" in (texto or "")):
        return _render_md_matematica(texto)
    return markdown.markdown(
        texto,
        extensions=["fenced_code", "tables", "nl2br"],
    )


def _bloco_resposta_html(q: Questao, disciplina: str = "algoritmos") -> str:
    try:
        tipo_av = config.obter_disciplina(disciplina).get("tipo_avaliacao", "")
    except Exception:
        tipo_av = ""
    if disciplina == "matrizes_vetores":
        linhas = "".join(
            '<div class="linha-texto"><span class="traco"></span></div>'
            for _ in range(1, 9)
        )
        dica = "Desenvolva passo a passo (fracoes/radicais exatos) e destaque a Resposta Final na linha abaixo."
        return f"""
        <div class="caixa-resposta caixa-mv">
          <div class="marcador-ocr">[QUESTAO: {html.escape(q.questao_id)}] &bull; {html.escape(dica)}</div>
          <div class="area-manuscrita">{linhas}</div>
          <div class="resposta-final-box"><strong>Resposta Final:</strong> ____________________________________________________________</div>
          <div class="marcador-ocr-fim">[/QUESTAO]</div>
        </div>
        """

    if q.tipo == "codigo":
        linhas = "".join(
            f'<div class="linha-codigo"><span class="num-linha">{i:02d}</span><span class="traco"></span></div>'
            for i in range(1, 19)
        )
        dica = "Escreva o programa ou algoritmo completo a caneta mantendo sintaxe, tipos e casos de borda."
    elif q.tipo == "sql":
        linhas = "".join(
            f'<div class="linha-codigo"><span class="num-linha">{i:02d}</span><span class="traco"></span></div>'
            for i in range(1, 13)
        )
        dica = "Escreva os comandos SQL (DDL/DML/consultas) a caneta respeitando chaves, juncoes e restricoes."
    elif q.tipo == "bug":
        linhas = "".join(
            f'<div class="linha-codigo"><span class="num-linha">{i:02d}</span><span class="traco"></span></div>'
            for i in range(1, 11)
        )
        dica = "Identifique o erro da solucao acima e reescreva a versao corrigida."
    elif q.spec_matematica or tipo_av == "matematica_geral" or q.tipo in ("calculo", "matriz", "vetor"):
        linhas = "".join(
            '<div class="linha-texto"><span class="traco"></span></div>'
            for _ in range(1, 9)
        )
        dica = "Desenvolva passo a passo e destaque a Resposta Final na linha abaixo."
        return f"""
        <div class="caixa-resposta caixa-mv">
          <div class="marcador-ocr">[QUESTAO: {html.escape(q.questao_id)}] &bull; {html.escape(dica)}</div>
          <div class="area-manuscrita">{linhas}</div>
          <div class="resposta-final-box"><strong>Resposta Final:</strong> ____________________________________________________________</div>
          <div class="marcador-ocr-fim">[/QUESTAO]</div>
        </div>
        """
    elif tipo_av == "logica_matematica" or q.tipo == "logica":
        linhas = "".join(
            '<div class="linha-texto"><span class="traco"></span></div>'
            for _ in range(1, 9)
        )
        dica = "Desenvolva passos, tabela/derivacao ou representacao formal e registre a conclusao abaixo."
        return f"""
        <div class="caixa-resposta">
          <div class="marcador-ocr">[QUESTAO: {html.escape(q.questao_id)}] &bull; {html.escape(dica)}</div>
          <div class="area-manuscrita">{linhas}</div>
          <div class="resposta-final-box"><strong>Conclusao / Resposta Final:</strong> ________________________________________________</div>
          <div class="marcador-ocr-fim">[/QUESTAO]</div>
        </div>
        """
    elif tipo_av == "conceitual_textual" or q.tipo in ("conceitual", "redacao", "projeto"):
        linhas = "".join(
            '<div class="linha-texto"><span class="traco"></span></div>'
            for _ in range(1, 9)
        )
        dica = "Redija sua resposta estruturada, objetiva e fundamentada nas linhas abaixo."
    else:
        linhas = "".join(
            '<div class="linha-texto"><span class="traco"></span></div>'
            for _ in range(1, 8)
        )
        dica = "Preencha passo a passo o teste de mesa / resposta final de forma legivel."

    return f"""
    <div class="caixa-resposta">
      <div class="marcador-ocr">[QUESTAO: {html.escape(q.questao_id)}] &bull; {html.escape(dica)}</div>
      <div class="area-manuscrita">{linhas}</div>
      <div class="marcador-ocr-fim">[/QUESTAO]</div>
    </div>
    """


def gerar_folha_prova(
    aluno: Dict[str, Any],
    bloco: BlocoCurricular,
    variante: str = "V1",
    tentativa: int = 1,
    modo: str = "checagem",
    protocolo: str = "",
    disciplina: str = "",
) -> Dict[str, Any]:
    config.garantir_diretorios()
    disc_id = config.normalizar_disciplina_id(
        disciplina or getattr(bloco, "disciplina", "") or config.DISCIPLINA_PADRAO
    )
    disc = config.obter_disciplina(disc_id)
    if not protocolo:
        protocolo = gerar_protocolo(
            aluno["id"], bloco.bloco_id, variante, tentativa, modo, disciplina=disc_id
        )

    questoes = bloco.obter_questoes(modo=modo, incluir_opcionais=False)
    tempo_alvo = bloco.tempo_alvo(modo=modo)
    modo_label = "CHECAGEM INDEPENDENTE (100% SEM CONSULTA)" if modo == "checagem" else "SESSAO DE PRATICA GUIADA"

    if variante == "V2":
        aviso_variante = """
        <div class="aviso-v2">
          <strong>VARIANTE V2 (RECUPERACAO DIRECIONADA):</strong> Revise cuidadosamente os desvios da Tentativa 1 antes de resolver.
          Para avancar de bloco e necessario atingir <strong>100% de acerto</strong> nesta checagem.
        </div>
        """
    else:
        aviso_variante = ""

    bloco_instrucoes = ""
    if modo == "pratica" and bloco.instrucoes_curtas_md:
        bloco_instrucoes = f"""
        <section class="instrucoes">
          <h2>Instrucoes Curtas do Bloco</h2>
          {_render_md(bloco.instrucoes_curtas_md, disciplina=disc_id)}
        </section>
        """

    questoes_html = []
    for idx, q in enumerate(questoes, start=1):
        questoes_html.append(
            f"""
            <article class="questao">
              <div class="questao-cabecalho">
                <span class="qid">{html.escape(q.questao_id)}</span>
                <span class="qtitulo">{html.escape(q.titulo)}</span>
                <span class="qtipo">{html.escape(q.tipo.upper())}</span>
              </div>
              <div class="enunciado">{_render_md(q.enunciado_md, disciplina=disc_id)}</div>
              {_bloco_resposta_html(q, disciplina=disc_id)}
            </article>
            """
        )

    doc_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8" />
  <title>Folha de Prova {html.escape(protocolo)} - {html.escape(disc['codigo'])} {html.escape(bloco.bloco_id)}</title>
  <style>
    @page {{
      size: A4;
      margin: 12mm;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      font-family: "Segoe UI", Arial, sans-serif;
      color: #111827;
      background: #f3f4f6;
      margin: 0;
      padding: 16px;
      font-size: 10.5pt;
      line-height: 1.4;
    }}
    .barra-acoes {{
      max-width: 210mm;
      margin: 0 auto 12px auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #1e293b;
      color: #fff;
      padding: 10px 16px;
      border-radius: 8px;
    }}
    .btn-imprimir {{
      background: #10b981;
      color: #fff;
      border: none;
      padding: 8px 16px;
      border-radius: 6px;
      font-weight: bold;
      cursor: pointer;
      font-size: 10pt;
    }}
    .folha-a4 {{
      width: 210mm;
      min-height: 297mm;
      margin: 0 auto;
      background: #fff;
      padding: 14mm;
      box-shadow: 0 4px 16px rgba(0,0,0,0.12);
      position: relative;
    }}
    .canto-ancora {{
      position: absolute;
      font-family: monospace;
      font-size: 12pt;
      font-weight: bold;
      color: #374151;
    }}
    .canto-tl {{ top: 6mm; left: 6mm; }}
    .canto-tr {{ top: 6mm; right: 6mm; }}
    .canto-bl {{ bottom: 6mm; left: 6mm; }}
    .canto-br {{ bottom: 6mm; right: 6mm; }}
    .cabecalho-prova {{
      border: 2px solid #111827;
      padding: 10px 12px;
      margin-bottom: 12px;
    }}
    .cabecalho-topo {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #cbd5e1;
      padding-bottom: 6px;
      margin-bottom: 8px;
    }}
    .titulo-curso {{ font-size: 12pt; font-weight: 700; text-transform: uppercase; }}
    .badge-modo {{
      background: #111827;
      color: #fff;
      padding: 3px 8px;
      font-size: 8.5pt;
      font-weight: 700;
      letter-spacing: 0.4px;
    }}
    .grid-meta {{
      display: grid;
      grid-template-columns: 1.4fr 1fr;
      gap: 6px 14px;
      font-size: 9.5pt;
    }}
    .box-protocolo {{
      margin-top: 8px;
      padding: 6px 10px;
      border: 1.5px dashed #111827;
      background: #f8fafc;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-family: monospace;
      font-size: 10pt;
      font-weight: bold;
    }}
    .box-tempo {{
      margin-top: 8px;
      padding: 6px 10px;
      border: 1px solid #475569;
      background: #fffbeb;
      font-size: 9.5pt;
      display: flex;
      justify-content: space-between;
    }}
    .aviso-v2 {{
      border: 1.5px solid #b45309;
      background: #fef3c7;
      padding: 8px 10px;
      margin-bottom: 12px;
      font-size: 9.5pt;
    }}
    .instrucoes {{
      border: 1px solid #94a3b8;
      background: #f8fafc;
      padding: 8px 12px;
      margin-bottom: 12px;
      font-size: 9.5pt;
    }}
    .instrucoes h2 {{ margin: 0 0 6px 0; font-size: 10.5pt; }}
    .questao {{
      margin-bottom: 14px;
      page-break-inside: avoid;
    }}
    .questao-cabecalho {{
      background: #e2e8f0;
      padding: 5px 8px;
      border-left: 4px solid #0f172a;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 6px;
      font-weight: 700;
    }}
    .qid {{ font-family: monospace; font-size: 10.5pt; }}
    .qtipo {{
      font-size: 8pt;
      background: #334155;
      color: #fff;
      padding: 2px 6px;
      border-radius: 3px;
    }}
    .enunciado pre {{
      background: #f8fafc;
      border: 1px solid #cbd5e1;
      padding: 8px;
      font-family: Consolas, monospace;
      font-size: 9pt;
      white-space: pre-wrap;
    }}
    .enunciado code {{ font-family: Consolas, monospace; background: #f1f5f9; padding: 1px 4px; }}
    /* Tipografia Matematica Offline (MAT121) */
    .math {{
      font-family: "Cambria Math", "Times New Roman", Georgia, serif;
      font-size: 10.8pt;
      display: inline;
    }}
    .math-block {{
      margin: 6px 0;
      text-align: center;
    }}
    .frac {{
      display: inline-flex;
      flex-direction: column;
      vertical-align: middle;
      text-align: center;
      font-size: 0.92em;
      line-height: 1.05;
      margin: 0 2px;
    }}
    .frac .f-num {{
      border-bottom: 1px solid #111827;
      padding: 0 3px 1px 3px;
    }}
    .frac .f-den {{
      padding: 1px 3px 0 3px;
    }}
    .vec, .hat {{
      display: inline-block;
      position: relative;
      padding-top: 2px;
    }}
    .vec::before {{
      content: "→";
      position: absolute;
      top: -7px;
      left: 0;
      right: 0;
      text-align: center;
      font-size: 0.68em;
      line-height: 1;
    }}
    .hat::before {{
      content: "^";
      position: absolute;
      top: -6px;
      left: 0;
      right: 0;
      text-align: center;
      font-size: 0.72em;
      line-height: 1;
    }}
    .sqrt-rad {{
      border-top: 1px solid #111827;
      padding: 0 2px;
    }}
    table.m-grid {{
      display: inline-table;
      vertical-align: middle;
      border-collapse: collapse;
      margin: 2px 4px;
    }}
    table.m-grid td {{
      padding: 2px 7px;
      text-align: center;
    }}
    table.m-bmat {{
      border-left: 2px solid #111827;
      border-right: 2px solid #111827;
      border-radius: 3px;
    }}
    table.m-par {{
      border-left: 1.8px solid #111827;
      border-right: 1.8px solid #111827;
      border-radius: 8px;
    }}
    table.m-det {{
      border-left: 1.5px solid #111827;
      border-right: 1.5px solid #111827;
    }}
    table.m-cases {{
      border-left: 2.2px solid #111827;
      padding-left: 4px;
    }}
    table.m-cases td {{
      text-align: left;
      padding: 1px 6px;
    }}
    .caixa-resposta {{
      border: 1.5px solid #1e293b;
      padding: 6px 8px 8px 8px;
      margin-top: 6px;
      background: #fff;
    }}
    .resposta-final-box {{
      margin-top: 8px;
      padding: 6px 8px;
      border: 1.2px dashed #475569;
      background: #f8fafc;
      font-size: 9.2pt;
    }}
    .marcador-ocr, .marcador-ocr-fim {{
      font-family: monospace;
      font-size: 8.5pt;
      color: #475569;
    }}
    .marcador-ocr {{ margin-bottom: 4px; border-bottom: 1px dotted #cbd5e1; padding-bottom: 3px; }}
    .marcador-ocr-fim {{ margin-top: 4px; text-align: right; }}
    .linha-codigo, .linha-texto {{
      display: flex;
      align-items: flex-end;
      height: 29px;
      margin-bottom: 2px;
      border-bottom: 1px solid #cbd5e1;
    }}
    .num-linha {{
      width: 24px;
      font-family: monospace;
      font-size: 7.5pt;
      padding-bottom: 2px;
      color: #94a3b8;
    }}
    .rodape-devolucao {{
      margin-top: 14px;
      border-top: 2px solid #111827;
      padding-top: 8px;
      font-size: 8.5pt;
      color: #334155;
    }}
    @media print {{
      body {{ background: #fff; padding: 0; }}
      .barra-acoes {{ display: none !important; }}
      .folha-a4 {{ box-shadow: none; width: 100%; min-height: auto; padding: 6mm; }}
    }}
  </style>
</head>
<body>
  <div class="barra-acoes">
    <span>{html.escape(disc['codigo'])} &bull; Protocolo: <strong>{html.escape(protocolo)}</strong> | Tempo-alvo: <strong>{tempo_alvo} min</strong></span>
    <button class="btn-imprimir" onclick="window.print()">Imprimir Folha A4 / Salvar PDF</button>
  </div>

  <div class="folha-a4">
    <span class="canto-ancora canto-tl">[+]</span>
    <span class="canto-ancora canto-tr">[+]</span>
    <span class="canto-ancora canto-bl">[+]</span>
    <span class="canto-ancora canto-br">[+]</span>

    <header class="cabecalho-prova">
      <div class="cabecalho-topo">
        <div class="titulo-curso">Curso de {html.escape(disc['nome'])} ({html.escape(disc['codigo'])} - UTFPR)</div>
        <div class="badge-modo">{html.escape(modo_label)}</div>
      </div>
      <div class="grid-meta">
        <div><strong>Aluno:</strong> {html.escape(aluno["nome"])} ({html.escape(aluno["email"])})</div>
        <div><strong>Bloco:</strong> {html.escape(bloco.bloco_id)} | <strong>Variante:</strong> {html.escape(variante)} | <strong>Tentativa:</strong> #{tentativa} | <strong>{int(disc.get('periodo', 1))}º Per. ({int(disc.get('carga_horaria', 60))}h)</strong></div>
        <div><strong>Tema:</strong> {html.escape(bloco.titulo)}</div>
        <div><strong>Meta de Tempo:</strong> {tempo_alvo} min &bull; <strong>Criterio:</strong> 100% sem consulta</div>
      </div>
      <div class="box-protocolo">
        <span>[PROTOCOLO: {html.escape(protocolo)}]</span>
        <span>REGISTRO AUTOMATICO OCR</span>
      </div>
      <div class="box-tempo">
        <span><strong>HORA INICIO:</strong> ____ : ____</span>
        <span><strong>HORA TERMINO:</strong> ____ : ____</span>
        <span><strong>[TEMPO: ______ min]</strong></span>
      </div>
    </header>

    {aviso_variante}
    {bloco_instrucoes}

    <main>
      {"".join(questoes_html)}
    </main>

    <footer class="rodape-devolucao">
      <strong>Como devolver para correcao automatica:</strong> 1) Preencha os horarios e todas as caixas de resposta a caneta dentro do tempo-alvo.
      2) Tire uma foto nitida (ou escaneie) mantendo os 4 marcadores <code>[+]</code> visiveis.
      3) Responda ao e-mail recebido anexando a foto com o codigo <strong>{html.escape(protocolo)}</strong> no assunto (ou envie diretamente pelo Dashboard).
    </footer>
  </div>
</body>
</html>
"""

    caminho_html = os.path.join(config.FOLHAS_DIR, f"{protocolo}.html")
    with open(caminho_html, "w", encoding="utf-8") as f:
        f.write(doc_html)

    return {
        "protocolo": protocolo,
        "disciplina": disc_id,
        "caminho_folha_html": caminho_html,
        "tempo_alvo_min": tempo_alvo,
        "qtd_questoes": len(questoes),
        "questoes_ids": [q.questao_id for q in questoes],
        "html": doc_html,
    }
