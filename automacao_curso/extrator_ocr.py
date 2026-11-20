#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Processamento de imagem (PIL), extracao OCR de folhas manuscritas fotografadas/escaneadas
e gerador de imagens de prova simuladas para demonstracao e testes E2E.
"""

import base64
import io
import json
import os
import re
from typing import Any, Dict, List, Optional

from PIL import Image, ImageDraw, ImageOps, PngImagePlugin
import requests

import config


def _extrair_imagens_de_pdf(caminho_pdf: str) -> List[str]:
    """Extrai paginas JPEG embutidas em PDFs de scanner (ex.: CamScanner) usando Python puro + PIL."""
    with open(caminho_pdf, "rb") as f:
        raw = f.read()

    paginas_salvas: List[str] = []
    pos = 0
    idx_pag = 0
    base_sem_ext = os.path.splitext(caminho_pdf)[0]

    while True:
        start = raw.find(b"\xff\xd8\xff", pos)
        if start == -1:
            break
        end_stream = raw.find(b"endstream", start)
        chunk = raw[start:end_stream] if end_stream != -1 else raw[start:]
        eoi = chunk.rfind(b"\xff\xd9")
        if eoi != -1:
            jpg_bytes = chunk[: eoi + 2]
            try:
                with Image.open(io.BytesIO(jpg_bytes)) as im:
                    w, h = im.size
                    if w >= 300 and h >= 300:
                        idx_pag += 1
                        out_jpg = f"{base_sem_ext}_pag{idx_pag}.jpg"
                        with open(out_jpg, "wb") as out_f:
                            out_f.write(jpg_bytes)
                        paginas_salvas.append(out_jpg)
            except Exception:
                pass
        pos = end_stream if end_stream != -1 else start + 10

    return paginas_salvas


def preprocessar_imagem_scan(caminho_imagem: str) -> Dict[str, Any]:
    """Abre a foto/scan (PNG, JPG ou PDF) com PIL, valida resolucao e normaliza contraste."""
    if not os.path.isfile(caminho_imagem):
        raise FileNotFoundError(f"Arquivo da prova nao encontrado: {caminho_imagem}")

    if caminho_imagem.lower().endswith(".pdf"):
        paginas = _extrair_imagens_de_pdf(caminho_imagem)
        if not paginas:
            tem_sidecar = any(
                os.path.isfile(caminho_imagem + ext) for ext in (".ocr.txt", ".txt")
            )
            cfg_int = config.obter_integracoes()
            if tem_sidecar or cfg_int.get("gemini_api_key"):
                return {
                    "largura": 0,
                    "altura": 0,
                    "formato": "PDF (vetorial/nativo)",
                    "contraste_range": (0, 255),
                    "metadados_chaves": [],
                    "camada_ocr_embutida": "",
                    "paginas_imagens": [],
                }
            raise ValueError(
                "PDF recebido nao contem paginas de imagem JPEG extraiveis e Gemini Vision nao esta configurado. "
                "Exporte como imagem JPG/PNG ou configure GEMINI_API_KEY."
            )
        with Image.open(paginas[0]) as img:
            largura, altura = img.size
            cinza = ImageOps.grayscale(img)
            normalizada = ImageOps.autocontrast(cinza)
            extrema = normalizada.getextrema()
        return {
            "largura": largura,
            "altura": altura,
            "formato": f"PDF ({len(paginas)} paginas)",
            "contraste_range": extrema,
            "metadados_chaves": [],
            "camada_ocr_embutida": "",
            "paginas_imagens": paginas,
        }

    with Image.open(caminho_imagem) as img:
        largura, altura = img.size
        formato = img.format or "PNG"
        meta = dict(img.info or {})
        cinza = ImageOps.grayscale(img)
        normalizada = ImageOps.autocontrast(cinza)
        extrema = normalizada.getextrema()

    return {
        "largura": largura,
        "altura": altura,
        "formato": formato,
        "contraste_range": extrema,
        "metadados_chaves": list(meta.keys()),
        "camada_ocr_embutida": meta.get("prep_ocr_texto", ""),
        "paginas_imagens": [caminho_imagem],
    }


def _chamar_visao_gemini(
    caminhos_imagens: List[str],
    caminho_original: str = "",
) -> str:
    """Chama Gemini Vision API (suporta PDF nativo/vetorial ou imagens JPG/PNG)."""
    cfg_int = config.obter_integracoes()
    api_key = cfg_int.get("gemini_api_key", "")
    modelo = cfg_int.get("gemini_model", config.GEMINI_MODEL)
    if not api_key or (not caminhos_imagens and not caminho_original):
        return ""

    prompt = (
        "Transcreva LITERALMENTE a prova manuscrita nestas paginas, mantendo exatamente como o aluno escreveu o protocolo "
        "[PROTOCOLO: ...], o cabecalho de horario (HORA INICIO: HH:MM, HORA TERMINO: HH:MM, [TEMPO: XX min]) e cada resposta delimitada por "
        "[QUESTAO: ID] ... [/QUESTAO]. Preserve com exatidao codigo C99 OU notacao matematica (fracoes a/b, matrizes [[...]], vetores (x, y, z), "
        "radicais sqrt(...), equacoes e sinais +-). NUNCA corrija erros de sintaxe C ou de calculo/logica do aluno."
    )
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{modelo}:generateContent?key={api_key}"

    # Se o arquivo original for PDF (ex.: PDF anotado com caneta/vetores), enviar o PDF completo primeiro
    if (
        caminho_original
        and caminho_original.lower().endswith(".pdf")
        and os.path.isfile(caminho_original)
        and os.path.getsize(caminho_original) <= 18 * 1024 * 1024
    ):
        with open(caminho_original, "rb") as f:
            b64_pdf = base64.b64encode(f.read()).decode("ascii")
        payload_pdf = {
            "contents": [
                {
                    "parts": [
                        {"text": prompt},
                        {"inline_data": {"mime_type": "application/pdf", "data": b64_pdf}},
                    ]
                }
            ]
        }
        try:
            resp = requests.post(url, json=payload_pdf, timeout=45)
            if resp.status_code == 200:
                cands = resp.json().get("candidates", [])
                if cands:
                    out_parts = cands[0].get("content", {}).get("parts", [])
                    txt = "\n".join(p.get("text", "") for p in out_parts).strip()
                    if txt:
                        return txt
        except Exception:
            pass

    if not caminhos_imagens:
        return ""

    parts: List[Dict[str, Any]] = [{"text": prompt}]
    for img_path in caminhos_imagens[:8]:
        with open(img_path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("ascii")
        ext = os.path.splitext(img_path)[1].lower()
        mime = "image/jpeg" if ext in (".jpg", ".jpeg") else "image/png"
        parts.append({"inline_data": {"mime_type": mime, "data": b64}})

    payload = {"contents": [{"parts": parts}]}
    try:
        resp = requests.post(url, json=payload, timeout=45)
        if resp.status_code == 200:
            data = resp.json()
            cands = data.get("candidates", [])
            if cands:
                out_parts = cands[0].get("content", {}).get("parts", [])
                return "\n".join(p.get("text", "") for p in out_parts).strip()
    except Exception:
        pass
    return ""


def parse_texto_ocr(texto_bruto: str, protocolo_fallback: str = "") -> Dict[str, Any]:
    """Extrai protocolo, tempo declarado (ou diferenca HORA INICIO/TERMINO) e respostas por ID."""
    m_prot = re.search(
        r"(?:\[?PROTOCOLO\s*:\s*)?(PREP-(?:MV-)?[A-H]\d{2}-V\d+-T\d+-[A-F0-9]+)\]?",
        texto_bruto,
        re.IGNORECASE,
    )
    protocolo = m_prot.group(1).upper() if m_prot else protocolo_fallback

    cabecalho = re.split(r"\[QUESTAO\s*:", texto_bruto, maxsplit=1, flags=re.IGNORECASE)[0]

    pad_tempo = r"\[?\s*TEMPO(?:\s+(?:TOTAL|GASTO|REAL))?\s*:\s*(\d+(?:[.,]\d+)?)\s*(?:minutos?|min|m|')?\s*\]?"
    m_tempo = re.search(pad_tempo, cabecalho, re.IGNORECASE) or re.search(pad_tempo, texto_bruto, re.IGNORECASE)
    tempo_declarado = float(m_tempo.group(1).replace(",", ".")) if m_tempo else 0.0
    origem_tempo_ocr = "campo_tempo_folha" if tempo_declarado > 0 else "ausente"

    if tempo_declarado <= 0:
        m_ini = re.search(
            r"(?:HORA\s+(?:DE\s+)?IN[IÍ]CIO|IN[IÍ]CIO)\s*[:=\-]?\s*(\d{1,2})\s*(?:[:hH]\s*(\d{2})|[hH]\b)",
            cabecalho,
            re.IGNORECASE,
        )
        m_fim = re.search(
            r"(?:HORA\s+(?:DE\s+)?T[EÉ]RMINO|HORA\s+(?:DE\s+)?FIM|T[EÉ]RMINO|FIM)\s*[:=\-]?\s*(\d{1,2})\s*(?:[:hH]\s*(\d{2})|[hH]\b)",
            cabecalho,
            re.IGNORECASE,
        )
        if m_ini and m_fim:
            h_ini, m_ini_v = int(m_ini.group(1)), int(m_ini.group(2) or 0)
            h_fim, m_fim_v = int(m_fim.group(1)), int(m_fim.group(2) or 0)
            if 0 <= h_ini <= 23 and 0 <= m_ini_v <= 59 and 0 <= h_fim <= 23 and 0 <= m_fim_v <= 59:
                mins_ini = h_ini * 60 + m_ini_v
                mins_fim = h_fim * 60 + m_fim_v
                diff = mins_fim - mins_ini
                if diff < 0:
                    diff += 24 * 60
                if 0 < diff <= 360:
                    tempo_declarado = float(diff)
                    origem_tempo_ocr = "inicio_termino_folha"

    respostas: Dict[str, str] = {}
    pad_q = re.compile(
        r"\[QUESTAO\s*:\s*([A-H]\d{2}-(?:E|C|OP)\d+)\]\s*(.*?)\s*\[/QUESTAO\]",
        re.DOTALL | re.IGNORECASE,
    )
    for m in pad_q.finditer(texto_bruto):
        qid = m.group(1).upper().strip()
        conteudo = m.group(2).strip()
        respostas[qid] = conteudo

    return {
        "protocolo": protocolo,
        "tempo_declarado_min": tempo_declarado,
        "origem_tempo_ocr": origem_tempo_ocr,
        "respostas": respostas,
        "texto_bruto": texto_bruto,
    }


def extrair_respostas_da_imagem(
    caminho_imagem: str,
    protocolo_esperado: str = "",
) -> Dict[str, Any]:
    """
    Executa pipeline de visao/OCR sobre a foto ou scan enviado pelo aluno:
    1) Valida e normaliza a imagem via PIL.
    2) Le camada OCR embutida (PNG tEXt chunk) ou arquivo sidecar .ocr.txt/.json.
    3) Se ausente e houver chave Gemini Vision configurada, chama OCR por visao.
    4) Retorna dicionario estruturado com protocolo, tempo e mapa questao_id -> resposta.
    """
    info_img = preprocessar_imagem_scan(caminho_imagem)
    fonte_ocr = "nenhuma"
    texto_ocr = info_img.get("camada_ocr_embutida", "").strip()
    if texto_ocr:
        fonte_ocr = "png_chunk_ocr"

    if not texto_ocr:
        for ext in (".ocr.txt", ".txt"):
            cand = caminho_imagem + ext
            if os.path.isfile(cand):
                with open(cand, "r", encoding="utf-8") as f:
                    texto_ocr = f.read().strip()
                if texto_ocr:
                    fonte_ocr = "sidecar_txt"
                    break

    cfg_int = config.obter_integracoes()
    if not texto_ocr and cfg_int.get("gemini_api_key"):
        texto_ocr = _chamar_visao_gemini(
            info_img.get("paginas_imagens", []),
            caminho_original=caminho_imagem,
        )
        if texto_ocr:
            fonte_ocr = "gemini_vision_api"

    estruturado = parse_texto_ocr(texto_ocr, protocolo_fallback=protocolo_esperado)
    estruturado["imagem_info"] = {
        "largura": info_img["largura"],
        "altura": info_img["altura"],
        "formato": info_img["formato"],
        "fonte_ocr": fonte_ocr,
        "paginas": len(info_img.get("paginas_imagens", [caminho_imagem])),
    }
    return estruturado


def gerar_foto_prova_manuscrita_simulada(
    caminho_saida_png: str,
    protocolo: str,
    bloco_id: str,
    aluno_nome: str,
    tempo_min: int,
    respostas: Dict[str, str],
    disciplina: str = "",
) -> str:
    """
    Renderiza uma imagem PNG A4 simulando a folha fotografada/escaneada com respostas
    manuscritas a caneta azul e grava a camada de transcricao OCR nos metadados PNG.
    """
    disc_id = disciplina or config.disciplina_por_protocolo(protocolo)
    disc = config.obter_disciplina(disc_id)
    os.makedirs(os.path.dirname(os.path.abspath(caminho_saida_png)), exist_ok=True)
    largura, altura = 1240, 1754  # ~150 DPI A4
    img = Image.new("RGB", (largura, altura), (250, 249, 245))
    draw = ImageDraw.Draw(img)

    # Marcadores de calibracao nos 4 cantos [+]
    for (x, y) in [(30, 30), (largura - 80, 30), (30, altura - 60), (largura - 80, altura - 60)]:
        draw.text((x, y), "[+]", fill=(30, 41, 59))

    # Moldura e cabecalho simulado
    draw.rectangle([70, 70, largura - 70, 240], outline=(15, 23, 42), width=3)
    draw.text((95, 90), f"CURSO DE {disc['nome'].upper()} ({disc['codigo']} - UTFPR) - BLOCO {bloco_id}", fill=(15, 23, 42))
    draw.text((95, 125), f"ALUNO: {aluno_nome}", fill=(30, 41, 59))
    draw.text((95, 160), f"[PROTOCOLO: {protocolo}]   [TEMPO: {tempo_min} min]", fill=(180, 83, 9))
    draw.text((95, 195), "FOLHA DIGITALIZADA PARA CORRECAO AUTOMATICA POR VISAO", fill=(71, 85, 105))

    y_cursor = 275
    blocos_texto_ocr: List[str] = [
        f"[PROTOCOLO: {protocolo}]",
        f"[TEMPO: {tempo_min} min]",
    ]

    tinta_azul = (22, 65, 168)
    for qid, resp_texto in respostas.items():
        if y_cursor > altura - 220:
            break
        draw.rectangle([70, y_cursor, largura - 70, y_cursor + 34], fill=(226, 232, 240), outline=(51, 65, 85))
        draw.text((85, y_cursor + 10), f"[QUESTAO: {qid}]", fill=(15, 23, 42))
        y_cursor += 42

        linhas_resp = str(resp_texto).strip().splitlines() or [""]
        caixa_h = max(90, min(320, 24 + len(linhas_resp) * 20))
        draw.rectangle([70, y_cursor, largura - 70, y_cursor + caixa_h], outline=(100, 116, 139), width=2)

        ly = y_cursor + 12
        for linha in linhas_resp[:14]:
            draw.line([(85, ly + 15), (largura - 90, ly + 15)], fill=(203, 213, 225), width=1)
            draw.text((90, ly), linha[:105], fill=tinta_azul)
            ly += 20

        y_cursor += caixa_h + 24
        blocos_texto_ocr.append(f"[QUESTAO: {qid}]\n{resp_texto.strip()}\n[/QUESTAO]")

    texto_ocr_completo = "\n\n".join(blocos_texto_ocr)
    png_info = PngImagePlugin.PngInfo()
    png_info.add_text("prep_ocr_texto", texto_ocr_completo)
    png_info.add_text("prep_protocolo", protocolo)
    img.save(caminho_saida_png, format="PNG", pnginfo=png_info)
    return caminho_saida_png
