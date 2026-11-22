#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Servico de entrega de folhas de prova e boletins de feedback por e-mail.
Suporta envio/recebimento SMTP/IMAP real quando configurado e opera com
spool MIME (.eml) deterministico local em spool_email/enviados e spool_email/recebidos.
"""

import base64
import email
import email.utils
import hashlib
import html
import imaplib
import os
import pathlib
import re
import select
import shutil
import smtplib
import subprocess
import threading
import time
from email.message import EmailMessage
from email.policy import default as email_policy
from typing import Any, Callable, Dict, List, Optional

import requests

import banco_dados
import config
from catalogo_curricular import BlocoCurricular


def _encontrar_navegador_pdf() -> Optional[str]:
    candidatos = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        shutil.which("google-chrome"),
        shutil.which("chromium"),
        shutil.which("chromium-browser"),
        shutil.which("msedge"),
    ]
    for c in candidatos:
        if c and os.path.isfile(c):
            return c
    return None


def _garantir_pdf_folha(caminho_html: str) -> Optional[str]:
    """Converte a folha A4 HTML para PDF usando Chrome/Edge headless para visualizacao limpa no Gmail."""
    if not caminho_html or not os.path.isfile(caminho_html):
        return None
    caminho_pdf = os.path.splitext(caminho_html)[0] + ".pdf"
    try:
        if (
            os.path.isfile(caminho_pdf)
            and os.path.getsize(caminho_pdf) > 1000
            and os.path.getmtime(caminho_pdf) >= os.path.getmtime(caminho_html)
        ):
            return caminho_pdf
    except OSError:
        pass
    browser = _encontrar_navegador_pdf()
    if not browser:
        return None
    uri_html = pathlib.Path(os.path.abspath(caminho_html)).as_uri()
    cmd = [
        browser,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--no-pdf-header-footer",
        f"--print-to-pdf={os.path.abspath(caminho_pdf)}",
        uri_html,
    ]
    try:
        subprocess.run(
            cmd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=25,
            check=False,
        )
        if os.path.isfile(caminho_pdf) and os.path.getsize(caminho_pdf) > 1000:
            return caminho_pdf
    except Exception:
        pass
    return None


def _anexar_folha_prova(msg: EmailMessage, caminho_html: str, protocolo: str) -> str:
    """Anexa a folha em PDF (preferencial) ou HTML como fallback; retorna o nome do arquivo anexado."""
    caminho_pdf = _garantir_pdf_folha(caminho_html)
    if caminho_pdf:
        with open(caminho_pdf, "rb") as af:
            msg.add_attachment(
                af.read(),
                maintype="application",
                subtype="pdf",
                filename=f"{protocolo}.pdf",
            )
        return f"{protocolo}.pdf"
    with open(caminho_html, "rb") as af:
        msg.add_attachment(
            af.read(),
            maintype="text",
            subtype="html",
            filename=f"{protocolo}.html",
        )
    return f"{protocolo}.html"


def _enviar_via_brevo_https(msg: EmailMessage, api_key: str, remetente_padrao: str) -> None:
    """Envia EmailMessage pela API HTTPS da Brevo (porta 443, sem precisar de porta SMTP)."""
    remetente_nome, remetente_addr = email.utils.parseaddr(msg["From"] or remetente_padrao)
    remetente_addr = (remetente_addr or remetente_padrao or config.ADMIN_EMAIL).strip()
    dest_nome, dest_addr = email.utils.parseaddr(msg["To"] or "")
    dest_addr = (dest_addr or str(msg["To"] or "")).strip()
    if not dest_addr:
        raise ValueError("Destinatario ausente.")

    texto_partes: List[str] = []
    html_partes: List[str] = []
    anexos: List[Dict[str, str]] = []

    for part in msg.walk():
        if part.is_multipart():
            continue
        disp = (part.get_content_disposition() or "").lower()
        fname = part.get_filename()
        raw = part.get_payload(decode=True) or b""
        if disp == "attachment" or fname:
            anexos.append(
                {
                    "name": fname or "anexo.bin",
                    "content": base64.b64encode(raw).decode("ascii"),
                }
            )
        elif part.get_content_type() == "text/html":
            html_partes.append(raw.decode(part.get_content_charset() or "utf-8", errors="replace"))
        elif part.get_content_type() == "text/plain":
            texto_partes.append(raw.decode(part.get_content_charset() or "utf-8", errors="replace"))

    payload: Dict[str, Any] = {
        "sender": {"email": remetente_addr, "name": remetente_nome or "Preparacao Intensiva"},
        "to": [{"email": dest_addr, "name": dest_nome or dest_addr}],
        "subject": str(msg["Subject"] or "Preparacao Intensiva"),
    }
    if html_partes:
        payload["htmlContent"] = "\n".join(html_partes)
    if texto_partes:
        payload["textContent"] = "\n".join(texto_partes)
    if anexos:
        payload["attachment"] = anexos

    resp = requests.post(
        "https://api.brevo.com/v3/smtp/email",
        headers={
            "api-key": api_key,
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        json=payload,
        timeout=20,
    )
    resp.raise_for_status()


def _despachar_mime(msg: EmailMessage, nome_arquivo_eml: str) -> Dict[str, Any]:
    config.garantir_diretorios()
    if "X-Prep-Origem" not in msg:
        msg["X-Prep-Origem"] = "sistema"

    cfg = config.obter_integracoes()
    smtp_host = cfg["smtp_host"]
    smtp_port = int(cfg["smtp_port"])
    smtp_user = cfg["smtp_user"]
    smtp_pass = cfg["smtp_pass"]
    brevo_key = str(cfg.get("brevo_api_key", "") or "").strip()
    if cfg["smtp_from"] and (not msg["From"] or msg["From"] == config.SMTP_FROM):
        del msg["From"]
        msg["From"] = cfg["smtp_from"]

    caminho_eml = os.path.join(config.SPOOL_ENVIADOS_DIR, nome_arquivo_eml)
    with open(caminho_eml, "wb") as f:
        f.write(msg.as_bytes())

    envio_real = False
    modo_entrega = "SPOOL_LOCAL"
    erro_smtp = ""
    if brevo_key:
        try:
            _enviar_via_brevo_https(msg, brevo_key, cfg["smtp_from"] or smtp_user)
            envio_real = True
            modo_entrega = "HTTPS_BREVO"
        except Exception as exc:
            erro_smtp = f"Brevo HTTPS: {exc}"

    if not envio_real and smtp_host and smtp_user and smtp_pass:
        try:
            if smtp_port == 465:
                with smtplib.SMTP_SSL(smtp_host, smtp_port, timeout=12) as srv:
                    srv.login(smtp_user, smtp_pass)
                    srv.send_message(msg)
            else:
                with smtplib.SMTP(smtp_host, smtp_port, timeout=12) as srv:
                    srv.starttls()
                    srv.login(smtp_user, smtp_pass)
                    srv.send_message(msg)
            envio_real = True
            modo_entrega = "SMTP_REAL"
            erro_smtp = ""
        except Exception as exc:
            erro_smtp = f"{erro_smtp} | SMTP: {exc}".strip(" |") if erro_smtp else str(exc)

    return {
        "caminho_eml": caminho_eml,
        "enviado_smtp": envio_real,
        "modo_entrega": modo_entrega,
        "erro_smtp": erro_smtp,
    }


def enviar_prova_por_email(
    aluno: Dict[str, Any],
    bloco: BlocoCurricular,
    folha_info: Dict[str, Any],
    variante: str = "V1",
    tentativa: int = 1,
    modo: str = "checagem",
    disciplina: Optional[str] = None,
) -> Dict[str, Any]:
    protocolo = folha_info["protocolo"]
    disc_id = config.normalizar_disciplina_id(
        disciplina or getattr(bloco, "disciplina", "") or config.disciplina_por_protocolo(protocolo)
    )
    disc = config.obter_disciplina(disc_id)
    tempo_alvo = folha_info["tempo_alvo_min"]
    url_base = config.obter_public_url() or f"http://{config.DASHBOARD_HOST}:{config.DASHBOARD_PORT}"
    url_portal = f"{url_base}/aluno?disciplina={disc_id}"
    pin_aluno = str(aluno.get("pin_inicial") or "").strip()
    if not pin_aluno and aluno.get("id"):
        try:
            al_full = banco_dados.obter_aluno_por_id(int(aluno["id"]), incluir_pin=True)
            if al_full:
                pin_aluno = str(al_full.get("pin_inicial") or "").strip()
        except Exception:
            pin_aluno = ""
    linha_pin_txt = f"   (E-mail: {aluno['email']} | PIN de acesso: {pin_aluno})\n" if pin_aluno else ""
    linha_pin_html = (
        f'<tr><td style="padding: 6px; border: 1px solid #cbd5e1;"><strong>Acesso ao Portal</strong></td>'
        f'<td style="padding: 6px; border: 1px solid #cbd5e1;">'
        f'<a href="{html.escape(url_portal)}">{html.escape(url_portal)}</a><br>'
        f'E-mail: <code>{html.escape(aluno["email"])}</code> &bull; PIN: <strong><code>{html.escape(pin_aluno)}</code></strong>'
        f'</td></tr>'
        if pin_aluno
        else f'<tr><td style="padding: 6px; border: 1px solid #cbd5e1;"><strong>Portal do Aluno</strong></td>'
        f'<td style="padding: 6px; border: 1px solid #cbd5e1;"><a href="{html.escape(url_portal)}">{html.escape(url_portal)}</a></td></tr>'
    )
    modo_txt = "Checagem Independente (Sem Consulta)" if modo == "checagem" else "Sessao de Pratica Guiada"
    tipo_av = str(disc.get("tipo_avaliacao") or "codigo_c")
    if tipo_av in ("matematica", "matematica_geral"):
        instrucao_papel = "Resolva tudo a caneta no papel (desenvolvimento passo a passo e resposta final exata em fracoes/radicais/simbolos sem calculadora)."
    elif tipo_av == "logica_matematica":
        instrucao_papel = "Resolva tudo a caneta no papel (tabelas-verdade, derivacoes, diagramas ou calculos com notacao formal clara)."
    elif tipo_av == "computacao_tecnica":
        instrucao_papel = "Resolva tudo a caneta no papel (desenhando passos, algoritmos, SQL/codigo ou calculos tecnicos de forma legivel)."
    elif tipo_av == "conceitual_textual":
        instrucao_papel = "Redija as respostas a caneta de forma estruturada, objetiva e fundamentada diretamente na folha."
    else:
        instrucao_papel = "Resolva tudo a caneta no papel (sem compilador nas questoes de mesa/lacuna e escrevendo C99 a mao nas questoes de codigo)."

    assunto = (
        f"[{disc['tag_email']}] Prova {bloco.bloco_id} ({variante} - Tentativa #{tentativa}) "
        f"[{protocolo}]"
    )

    corpo_texto = (
        f"Ola {aluno['nome']},\n\n"
        f"Sua folha de prova ({disc['nome_curto']}) do bloco {bloco.bloco_id} ({bloco.titulo}) esta pronta em anexo.\n"
        f"Modalidade: {modo_txt} | Variante: {variante} | Tentativa: #{tentativa}\n"
        f"Tempo-alvo: {tempo_alvo} minutos | Criterio de dominio: 100% de acerto.\n\n"
        f"Passo a passo:\n"
        f"1. Abra e imprima o arquivo PDF em anexo ({protocolo}.pdf) ou acesse pelo Portal do Aluno.\n"
        f"2. Antes de comecar a escrever, acesse o Portal do Aluno para iniciar o cronometro: {url_portal}\n"
        f"{linha_pin_txt}"
        f"3. Preencha HORA INICIO, {instrucao_papel} e anote HORA TERMINO.\n"
        f"4. Tire uma foto nitida ou escaneie a folha completa (com os 4 cantos [+] visiveis).\n"
        f"5. Responda a este e-mail com a foto anexada (mantendo [{protocolo}] no assunto) ou envie pelo Dashboard.\n"
    )

    corpo_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<body style="font-family: Segoe UI, Arial, sans-serif; color: #1e293b; background: #f8fafc; padding: 20px;">
  <div style="max-width: 640px; margin: 0 auto; background: #ffffff; border: 1px solid #cbd5e1; border-radius: 8px; padding: 20px;">
    <h2 style="margin-top: 0; color: #0f172a;">Folha de Prova Liberada &mdash; {html.escape(disc['codigo'])} &bull; Bloco {html.escape(bloco.bloco_id)}</h2>
    <p>Ola, <strong>{html.escape(aluno['nome'])}</strong>.</p>
    <p>Sua nova folha de prova impressa para <strong>{html.escape(disc['nome'])} &mdash; {html.escape(bloco.titulo)}</strong> foi gerada e segue em anexo.</p>
    <table style="width: 100%; border-collapse: collapse; margin: 14px 0; font-size: 14px;">
      <tr><td style="padding: 6px; border: 1px solid #cbd5e1;"><strong>Protocolo</strong></td><td style="padding: 6px; border: 1px solid #cbd5e1; font-family: monospace;">{html.escape(protocolo)}</td></tr>
      <tr><td style="padding: 6px; border: 1px solid #cbd5e1;"><strong>Modalidade</strong></td><td style="padding: 6px; border: 1px solid #cbd5e1;">{html.escape(modo_txt)}</td></tr>
      <tr><td style="padding: 6px; border: 1px solid #cbd5e1;"><strong>Variante / Tentativa</strong></td><td style="padding: 6px; border: 1px solid #cbd5e1;">{html.escape(variante)} &bull; Tentativa #{tentativa}</td></tr>
      <tr><td style="padding: 6px; border: 1px solid #cbd5e1;"><strong>Tempo-alvo de Fluencia</strong></td><td style="padding: 6px; border: 1px solid #cbd5e1;"><strong>{tempo_alvo} minutos</strong></td></tr>
      {linha_pin_html}
    </table>
    <ol style="line-height: 1.6;">
      <li>Abra e imprima a folha A4 em anexo (<code>{html.escape(protocolo)}.pdf</code>).</li>
      <li>Anote a <strong>Hora de Inicio</strong> na folha (ou acione o cronometro em <a href="{html.escape(url_portal)}">{html.escape(url_portal)}</a>).</li>
      <li>{html.escape(instrucao_papel)}</li>
      <li>Fotografe ou escaneie a folha inteira mantendo os marcadores <code>[+]</code> visiveis e responda este e-mail com a imagem anexada.</li>
    </ol>
  </div>
</body>
</html>"""

    msg = EmailMessage()
    msg["Subject"] = assunto
    msg["From"] = config.SMTP_FROM
    msg["To"] = aluno["email"]
    msg["X-Prep-Protocolo"] = protocolo
    msg.set_content(corpo_texto)
    msg.add_alternative(corpo_html, subtype="html")

    _anexar_folha_prova(msg, folha_info["caminho_folha_html"], protocolo)

    res = _despachar_mime(msg, f"ENVIO_PROVA_{protocolo}.eml")
    res["assunto"] = assunto
    return res


def enviar_feedback_por_email(
    aluno: Dict[str, Any],
    resultado: Dict[str, Any],
    nova_folha: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    protocolo = resultado["protocolo"]
    disc_id = config.normalizar_disciplina_id(
        resultado.get("disciplina") or config.disciplina_por_protocolo(protocolo)
    )
    disc = config.obter_disciplina(disc_id)
    bloco = resultado["bloco"]
    pct = resultado["percentual_acerto"]
    assunto = (
        f"[{disc['tag_email']}] Correcao & Feedback {bloco} "
        f"({resultado['acertos_iniciais']}/{resultado['total_questoes']} - {pct:.0f}%) [{protocolo}]"
    )

    msg = EmailMessage()
    msg["Subject"] = assunto
    msg["From"] = config.SMTP_FROM
    msg["To"] = aluno["email"]
    msg["X-Prep-Protocolo"] = protocolo
    msg.set_content(
        f"Resultado de {bloco} ({protocolo}): {resultado['acertos_iniciais']}/{resultado['total_questoes']} ({pct:.0f}%).\n"
        f"Tempo: {resultado['tempo_declarado_min']} min | Decisao: {resultado['proxima_acao']}.\n"
        f"Consulte o HTML em anexo/corpo e o Dashboard para o feedback detalhado item a item."
    )
    msg.add_alternative(resultado["relatorio_feedback_html"], subtype="html")

    if nova_folha and os.path.isfile(nova_folha.get("caminho_folha_html", "")):
        novo_prot = nova_folha["protocolo"]
        _anexar_folha_prova(msg, nova_folha["caminho_folha_html"], novo_prot)

    res = _despachar_mime(msg, f"FEEDBACK_{protocolo}.eml")
    res["assunto"] = assunto
    return res


def simular_resposta_email_aluno(
    protocolo: str,
    aluno_email: str,
    caminho_imagem: str,
) -> str:
    """Grava no spool de entrada uma resposta de e-mail realista do aluno com foto anexada."""
    config.garantir_diretorios()
    msg = EmailMessage()
    msg["Subject"] = f"Re: [Algoritmos C - UTFPR] Devolucao Prova [{protocolo}]"
    msg["From"] = aluno_email
    msg["To"] = config.SMTP_FROM
    msg["X-Prep-Protocolo"] = protocolo
    msg.set_content(
        f"Ola tutor,\nSegue em anexo a foto da minha folha resolvida do protocolo {protocolo}.\nObrigado!"
    )

    ext = os.path.splitext(caminho_imagem)[1].lower().lstrip(".") or "png"
    subtype = "jpeg" if ext in ("jpg", "jpeg") else "png"
    with open(caminho_imagem, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="image",
            subtype=subtype,
            filename=os.path.basename(caminho_imagem),
        )

    destino_eml = os.path.join(config.SPOOL_RECEBIDOS_DIR, f"RESP_{protocolo}.eml")
    with open(destino_eml, "wb") as f:
        f.write(msg.as_bytes())
    return destino_eml


_UIDS_IMAP_IGNORADOS: set = set()


def resolver_protocolo_entrada(protocolo_bruto: str, remetente_email: str) -> str:
    """
    Resolve o protocolo alvo de uma devolucao:
    - Se o protocolo informado existe e ainda esta pendente ('emitida'/'em_execucao'), usa-o.
    - Se o aluno respondeu em thread antigo (protocolo ja 'corrigida'), redireciona para a
      prova pendente mais recente do aluno na mesma disciplina.
    - Se nao ha protocolo no assunto, busca pela prova pendente do e-mail remetente.
    """
    prot = (protocolo_bruto or "").strip().upper()
    rem_clean = email.utils.parseaddr(remetente_email or "")[1].strip().lower()

    if prot:
        prova = banco_dados.obter_prova(prot)
        if prova:
            if prova.get("status") in ("emitida", "em_execucao"):
                return prot
            disc_prot = prova.get("disciplina") or config.disciplina_por_protocolo(prot)
            pend = banco_dados.obter_prova_pendente_por_aluno_id(
                int(prova["aluno_id"]), disciplina=disc_prot
            )
            if pend:
                return pend["protocolo"]
            return prot

    if rem_clean:
        pend_rem = banco_dados.obter_prova_pendente_por_email(rem_clean)
        if pend_rem:
            return pend_rem["protocolo"]

    return prot


def _extrair_anexo_resposta(msg: email.message.EmailMessage) -> Optional[Dict[str, Any]]:
    for part in msg.iter_attachments():
        ctype = (part.get_content_type() or "").lower()
        fname_raw = part.get_filename() or ""
        eh_pdf = ctype == "application/pdf" or fname_raw.lower().endswith(".pdf")
        eh_img = ctype.startswith("image/") or fname_raw.lower().endswith((".png", ".jpg", ".jpeg"))
        if eh_img or eh_pdf:
            payload = part.get_payload(decode=True)
            if not payload:
                continue
            return {
                "payload": payload,
                "eh_pdf": eh_pdf,
                "filename": fname_raw,
            }
    return None


def coletar_respostas_por_email() -> List[Dict[str, str]]:
    """
    Varre e-mails recebidos (IMAP real via BODY.PEEK[] se configurado + spool_email/recebidos)
    com protecao anti-loop, deduplicacao por msg_chave e resolucao por remetente.
    """
    config.garantir_diretorios()
    cfg = config.obter_integracoes()
    coletados: List[Dict[str, str]] = []

    # 1. Buscar via IMAP se configurado (usa BODY.PEEK[] para nao marcar e-mails pessoais como lidos)
    if cfg["imap_host"] and cfg["imap_user"] and cfg["imap_pass"]:
        try:
            with imaplib.IMAP4_SSL(cfg["imap_host"], int(cfg["imap_port"]), timeout=15) as mail:
                mail.login(cfg["imap_user"], cfg["imap_pass"])
                mail.select("INBOX")
                status, data = mail.uid("search", None, "UNSEEN")
                if status == "OK" and data and data[0]:
                    for uid_b in data[0].split():
                        uid_str = uid_b.decode("ascii", errors="ignore")
                        chave_mem = (cfg["imap_user"], uid_str)
                        if chave_mem in _UIDS_IMAP_IGNORADOS:
                            continue
                        st, raw = mail.uid("fetch", uid_b, "(BODY.PEEK[])")
                        if st != "OK" or not raw or not isinstance(raw[0], tuple):
                            continue
                        raw_bytes = raw[0][1]
                        msg = email.message_from_bytes(raw_bytes, policy=email_policy)

                        if str(msg.get("X-Prep-Origem", "")).strip().lower() == "sistema":
                            _UIDS_IMAP_IGNORADOS.add(chave_mem)
                            continue

                        anexo = _extrair_anexo_resposta(msg)
                        if not anexo:
                            _UIDS_IMAP_IGNORADOS.add(chave_mem)
                            continue

                        assunto = str(msg.get("Subject", ""))
                        prot_hdr = str(msg.get("X-Prep-Protocolo", ""))
                        remetente = str(msg.get("From", ""))
                        rem_clean = email.utils.parseaddr(remetente)[1].strip().lower()
                        tem_prot = bool(config.extrair_protocolo(f"{prot_hdr} {assunto}"))
                        pend_aluno = banco_dados.obter_prova_pendente_por_email(rem_clean)

                        # So baixa automaticamente e-mails que sejam do curso (protocolo PREP- ou aluno com prova pendente)
                        if not tem_prot and not pend_aluno:
                            _UIDS_IMAP_IGNORADOS.add(chave_mem)
                            continue

                        msg_id = str(msg.get("Message-ID", "")).strip()
                        msg_chave = msg_id or f"sha256:{hashlib.sha256(raw_bytes).hexdigest()}"
                        if banco_dados.email_ja_processado(msg_chave):
                            mail.uid("store", uid_b, "+FLAGS", "(\\Seen)")
                            continue

                        eml_path = os.path.join(
                            config.SPOOL_RECEBIDOS_DIR, f"IMAP_{int(time.time())}_{uid_str}.eml"
                        )
                        with open(eml_path, "wb") as f:
                            f.write(raw_bytes)
                        mail.uid("store", uid_b, "+FLAGS", "(\\Seen)")
        except Exception:
            pass

    # 2. Processar arquivos .eml presentes no spool_email/recebidos
    processados_dir = os.path.join(config.SPOOL_RECEBIDOS_DIR, "processados")
    os.makedirs(processados_dir, exist_ok=True)

    for nome in sorted(os.listdir(config.SPOOL_RECEBIDOS_DIR)):
        if not nome.lower().endswith(".eml"):
            continue
        caminho_eml = os.path.join(config.SPOOL_RECEBIDOS_DIR, nome)
        with open(caminho_eml, "rb") as f:
            raw_eml = f.read()
        msg = email.message_from_bytes(raw_eml, policy=email_policy)

        if str(msg.get("X-Prep-Origem", "")).strip().lower() == "sistema":
            os.replace(caminho_eml, os.path.join(processados_dir, nome))
            continue

        msg_id = str(msg.get("Message-ID", "")).strip()
        msg_chave = msg_id or f"sha256:{hashlib.sha256(raw_eml).hexdigest()}"
        if banco_dados.email_ja_processado(msg_chave):
            os.replace(caminho_eml, os.path.join(processados_dir, nome))
            continue

        assunto = str(msg.get("Subject", ""))
        prot_hdr = str(msg.get("X-Prep-Protocolo", ""))
        remetente = str(msg.get("From", ""))
        prot_bruto = config.extrair_protocolo(f"{prot_hdr} {assunto}")
        protocolo = resolver_protocolo_entrada(prot_bruto, remetente)

        anexo = _extrair_anexo_resposta(msg)
        caminho_img_salvo = ""
        if anexo:
            ext_default = ".pdf" if anexo["eh_pdf"] else ".png"
            fname = anexo["filename"] or f"anexo_{protocolo or 'prova'}{ext_default}"
            safe_name = re.sub(r"[^a-zA-Z0-9._-]", "_", fname)
            destino_img = os.path.join(
                config.UPLOADS_DIR, f"mail_{int(time.time())}_{safe_name}"
            )
            with open(destino_img, "wb") as out_f:
                out_f.write(anexo["payload"])
            caminho_img_salvo = destino_img

        os.replace(caminho_eml, os.path.join(processados_dir, nome))
        if caminho_img_salvo:
            coletados.append(
                {
                    "msg_chave": msg_chave,
                    "protocolo": protocolo,
                    "remetente": remetente,
                    "assunto": assunto,
                    "caminho_imagem": caminho_img_salvo,
                    "caminho_eml": os.path.join(processados_dir, nome),
                }
            )
        else:
            banco_dados.registrar_email_processado(
                msg_chave, protocolo, remetente, assunto, "ignorado_sem_anexo", "Sem anexo PDF/imagem"
            )

    return coletados


def testar_conexao_email(cfg: Dict[str, Any]) -> Dict[str, Any]:
    """Testa credenciais de envio (Brevo HTTPS ou SMTP) e IMAP antes de salvar/ativar."""
    res = {"smtp_ok": False, "smtp_erro": "", "imap_ok": False, "imap_erro": "", "envio_modo": "SMTP"}
    brevo_key = str(cfg.get("brevo_api_key", "") or "").strip()
    if brevo_key:
        try:
            r_b = requests.get(
                "https://api.brevo.com/v3/account",
                headers={"api-key": brevo_key, "Accept": "application/json"},
                timeout=12,
            )
            r_b.raise_for_status()
            res["smtp_ok"] = True
            res["envio_modo"] = "HTTPS_BREVO"
        except Exception as exc:
            res["smtp_erro"] = f"Brevo HTTPS: {exc}"
    elif cfg.get("smtp_host") and cfg.get("smtp_user") and cfg.get("smtp_pass"):
        try:
            port = int(cfg.get("smtp_port") or 587)
            if port == 465:
                with smtplib.SMTP_SSL(cfg["smtp_host"], port, timeout=8) as srv:
                    srv.login(cfg["smtp_user"], cfg["smtp_pass"])
            else:
                with smtplib.SMTP(cfg["smtp_host"], port, timeout=8) as srv:
                    srv.starttls()
                    srv.login(cfg["smtp_user"], cfg["smtp_pass"])
            res["smtp_ok"] = True
        except Exception as exc:
            res["smtp_erro"] = str(exc)
    else:
        res["smtp_erro"] = "Credenciais de envio (Brevo API Key ou SMTP) incompletas."

    if cfg.get("imap_host") and cfg.get("imap_user") and cfg.get("imap_pass"):
        try:
            port = int(cfg.get("imap_port") or 993)
            with imaplib.IMAP4_SSL(cfg["imap_host"], port, timeout=8) as mail:
                mail.login(cfg["imap_user"], cfg["imap_pass"])
                mail.select("INBOX")
            res["imap_ok"] = True
        except Exception as exc:
            res["imap_erro"] = str(exc)
    else:
        res["imap_erro"] = "Credenciais IMAP incompletas."

    gem_key = str(cfg.get("gemini_api_key", "") or "").strip()
    if gem_key:
        if not re.fullmatch(r"(?:AQ\.|AIza)[0-9A-Za-z._-]{16,}", gem_key):
            res["gemini_ok"] = False
            res["gemini_erro"] = "Formato invalido (deve comecar com AQ. ou AIza...)."
        else:
            try:
                r_g = requests.get(
                    "https://generativelanguage.googleapis.com/v1beta/models",
                    headers={"x-goog-api-key": gem_key},
                    timeout=10,
                )
                r_g.raise_for_status()
                res["gemini_ok"] = True
                res["gemini_erro"] = ""
            except requests.HTTPError as exc:
                st_g = exc.response.status_code if exc.response is not None else "HTTP"
                res["gemini_ok"] = False
                res["gemini_erro"] = f"Erro {st_g} na API Gemini."
            except Exception as exc:
                res["gemini_ok"] = False
                res["gemini_erro"] = str(exc)

    return res


class EmailAutoWatcher:
    """
    Worker em segundo plano que detecta respostas recebidas em tempo real:
    - Com IMAP configurado: usa IMAP IDLE (push instantaneo no Gmail) com fallback para polling.
    - Sem IMAP configurado: vigia continuamente spool_email/recebidos/ a cada 5s.
    """

    def __init__(self, fn_processar: Callable[[], List[Dict[str, Any]]]):
        self.fn_processar = fn_processar
        self._lock = threading.Lock()
        self._status_lock = threading.Lock()
        self._stop_event = threading.Event()
        self._wake_event = threading.Event()
        self._thread: Optional[threading.Thread] = None
        self._status: Dict[str, Any] = {
            "worker_ativo": False,
            "modo": "spool_local",
            "ultimo_ciclo_em": "",
            "ultima_correcao_em": "",
            "total_processados": 0,
            "ultimo_erro": "",
        }

    def iniciar(self) -> None:
        if self._thread and self._thread.is_alive():
            return
        self._stop_event.clear()
        self._thread = threading.Thread(
            target=self._loop_principal, name="EmailAutoWatcher", daemon=True
        )
        self._thread.start()
        with self._status_lock:
            self._status["worker_ativo"] = True

    def parar(self, timeout: float = 3.0) -> None:
        self._stop_event.set()
        self._wake_event.set()
        if self._thread and self._thread.is_alive():
            self._thread.join(timeout=timeout)
        with self._status_lock:
            self._status["worker_ativo"] = False

    def acordar(self) -> None:
        self._wake_event.set()

    def executar_ciclo_agora(self) -> List[Dict[str, Any]]:
        with self._lock:
            agora = time.strftime("%Y-%m-%d %H:%M:%S")
            try:
                resultados = self.fn_processar() or []
                with self._status_lock:
                    self._status["ultimo_ciclo_em"] = agora
                    self._status["ultimo_erro"] = ""
                    ok_cnt = sum(1 for r in resultados if not r.get("erro"))
                    if ok_cnt > 0:
                        self._status["total_processados"] += ok_cnt
                        self._status["ultima_correcao_em"] = agora
                return resultados
            except Exception as exc:
                with self._status_lock:
                    self._status["ultimo_ciclo_em"] = agora
                    self._status["ultimo_erro"] = str(exc)
                return []

    def obter_status(self) -> Dict[str, Any]:
        cfg = config.obter_integracoes()
        imap_cfg = bool(cfg["imap_host"] and cfg["imap_user"] and cfg["imap_pass"])
        smtp_cfg = bool(
            cfg.get("brevo_api_key")
            or (cfg["smtp_host"] and cfg["smtp_user"] and cfg["smtp_pass"])
        )
        gemini_cfg = bool(cfg["gemini_api_key"])
        brevo_cfg = bool(cfg.get("brevo_api_key"))
        with self._status_lock:
            st = dict(self._status)
        st["imap_configurado"] = imap_cfg
        st["smtp_configurado"] = smtp_cfg
        st["brevo_configurado"] = brevo_cfg
        st["gemini_configurado"] = gemini_cfg
        st["imap_user"] = cfg["imap_user"]
        st["smtp_user"] = cfg["smtp_user"]
        st["imap_host"] = cfg["imap_host"]
        st["smtp_host"] = cfg["smtp_host"]
        if not imap_cfg:
            st["modo"] = "spool_local"
        return st

    def _aguardar_imap_idle(self, cfg: Dict[str, Any]) -> None:
        with imaplib.IMAP4_SSL(cfg["imap_host"], int(cfg["imap_port"]), timeout=15) as mail:
            mail.login(cfg["imap_user"], cfg["imap_pass"])
            mail.select("INBOX")
            if "IDLE" not in getattr(mail, "capabilities", ()):
                with self._status_lock:
                    self._status["modo"] = "imap_polling"
                self._wake_event.wait(timeout=int(cfg["imap_poll_sec"]))
                self._wake_event.clear()
                return

            with self._status_lock:
                self._status["modo"] = "imap_idle"

            tag = mail._new_tag()
            mail.send(tag + b" IDLE\r\n")
            resp_ini = mail.readline()
            if not resp_ini.startswith(b"+"):
                self._wake_event.wait(timeout=int(cfg["imap_poll_sec"]))
                self._wake_event.clear()
                return

            deadline = time.time() + 240.0
            try:
                while not self._stop_event.is_set() and not self._wake_event.is_set():
                    if time.time() >= deadline:
                        break
                    pending = getattr(mail.sock, "pending", lambda: 0)()
                    if pending > 0:
                        readable = [mail.sock]
                    else:
                        readable, _, _ = select.select([mail.sock], [], [], 1.5)
                    if readable:
                        linha = mail.readline()
                        if not linha:
                            break
                        if b"EXISTS" in linha.upper() or b"RECENT" in linha.upper():
                            break
            finally:
                try:
                    mail.send(b"DONE\r\n")
                    fim_lim = time.time() + 5.0
                    while time.time() < fim_lim:
                        l_end = mail.readline()
                        if not l_end or l_end.startswith(tag):
                            break
                except Exception:
                    pass
            self._wake_event.clear()

    def _loop_principal(self) -> None:
        while not self._stop_event.is_set():
            cfg = config.obter_integracoes()
            self.executar_ciclo_agora()
            if self._stop_event.is_set():
                break

            if cfg["imap_host"] and cfg["imap_user"] and cfg["imap_pass"]:
                try:
                    self._aguardar_imap_idle(cfg)
                except Exception as exc:
                    with self._status_lock:
                        self._status["modo"] = "imap_polling"
                        self._status["ultimo_erro"] = f"IMAP IDLE reconectando: {exc}"
                    self._wake_event.wait(timeout=int(cfg["imap_poll_sec"]))
                    self._wake_event.clear()
            else:
                with self._status_lock:
                    self._status["modo"] = "spool_local"
                self._wake_event.wait(timeout=5.0)
                self._wake_event.clear()


def listar_emails_spool() -> List[Dict[str, str]]:
    config.garantir_diretorios()
    itens = []
    for pasta, direcao in [(config.SPOOL_ENVIADOS_DIR, "ENVIADO"), (config.SPOOL_RECEBIDOS_DIR, "RECEBIDO")]:
        if not os.path.isdir(pasta):
            continue
        for fn in sorted(os.listdir(pasta), reverse=True):
            if fn.endswith(".eml"):
                p = os.path.join(pasta, fn)
                with open(p, "rb") as f:
                    msg = email.message_from_bytes(f.read(), policy=email_policy)
                itens.append(
                    {
                        "arquivo": fn,
                        "direcao": direcao,
                        "assunto": str(msg.get("Subject", "")),
                        "de": str(msg.get("From", "")),
                        "para": str(msg.get("To", "")),
                        "protocolo": str(msg.get("X-Prep-Protocolo", "")),
                    }
                )
    return itens
