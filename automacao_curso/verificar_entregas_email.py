#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Diagnostico de entrega de e-mails via IMAP (Gmail).

Confirma se o servidor SMTP do Gmail ACEITOU a entrega de uma folha de
prova e se houve avisos de falha de entrega (bounce / NDR) para o
destinatario.

O Gmail arquiva em "[Gmail]/E-mails enviados" as mensagens enviadas via
SMTP pela mesma conta, entao essa pasta serve como prova de aceite.
Um destinatario inexistente faria o smtplib levantar
SMTPRecipientsRefused (que o sistema ja reporta como erro_smtp).

Uso (a partir de automacao_curso/):
    python verificar_entregas_email.py
    python verificar_entregas_email.py --aluno 2
    python verificar_entregas_email.py --email m12996530123@gmail.com
    python verificar_entregas_email.py --protocolo PREP-MV-A01-V1-T1-0BFF50
"""

import argparse
import imaplib
import os
import re
import sys
from datetime import datetime, timedelta
from email import policy
from email.parser import BytesParser
from email.utils import parsedate_to_datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import config  # noqa: E402

# Terminos que caracterizam um aviso de falha de entrega
TERMOS_BOUNCE = [
    "delivery status notification",
    "undelivered mail",
    "mail delivery failed",
    "delivery has failed",
    "undeliverable",
    "mail delivery subsystem",
    "failed delivery",
    "falha na entrega",
    "nao foi possivel entregar",
    "n\u00e3o foi poss\u00edvel entregar",
    "mensagem n\u00e3o entregue",
]


def _pastas(M):
    """Lista os nomes de pastas IMAP."""
    nomes = []
    typ, boxes = M.list()
    if typ != "OK":
        return nomes
    for b in boxes or []:
        if isinstance(b, bytes):
            b = b.decode("utf-8", "replace")
        m = re.search(r'"([^"]+)"\s*$', b)
        nomes.append(m.group(1) if m else b.split(" ")[-1])
    return nomes


def _pasta_enviados(pastas):
    for p in pastas:
        if re.search(r"sent|enviad", p, re.I):
            return p
    return ""


def _buscar_cabecalhos(M, pasta, limite=80):
    """Retorna lista de dicts com os cabecalhos das ultimas mensagens."""
    typ, _ = M.select(f'"{pasta}"')
    if typ != "OK":
        return []
    typ, data = M.search(None, "ALL")
    ids = data[0].split()
    saida = []
    for mid in ids[-limite:]:
        typ, msg_data = M.fetch(
            mid, "(BODY.PEEK[HEADER.FIELDS (DATE FROM TO CC SUBJECT MESSAGE-ID)])"
        )
        if typ != "OK" or not msg_data or not isinstance(msg_data[0], tuple):
            continue
        msg = BytesParser(policy=policy.default).parsebytes(msg_data[0][1])
        dt = None
        try:
            dt = parsedate_to_datetime(str(msg["Date"] or ""))
        except Exception:
            dt = None
        saida.append(
            {
                "id": mid.decode(),
                "date": str(msg["Date"] or ""),
                "dt": dt,
                "from": str(msg["From"] or ""),
                "to": str(msg["To"] or ""),
                "cc": str(msg["Cc"] or ""),
                "subject": str(msg["Subject"] or ""),
                "message_id": str(msg["Message-ID"] or ""),
            }
        )
    return saida


def _casar(msg, email_alvo, protocolo):
    alvo = (email_alvo or "").strip().lower()
    if alvo and alvo in msg["to"].lower():
        return True
    if alvo and alvo in msg["cc"].lower():
        return True
    if protocolo and protocolo.lower() in msg["subject"].lower():
        return True
    return False


def main() -> int:
    ap = argparse.ArgumentParser(description="Diagnostico de entrega de e-mails (IMAP).")
    ap.add_argument("--aluno", type=int, help="ID do aluno (busca o e-mail no banco)")
    ap.add_argument("--email", default="", help="e-mail do destinatario")
    ap.add_argument("--protocolo", default="", help="protocolo da prova")
    ap.add_argument("--dias", type=int, default=7, help="janela de tempo em dias")
    args = ap.parse_args()

    cfg = config.obter_integracoes()
    user = cfg.get("smtp_user") or ""
    pass_ = cfg.get("smtp_pass") or ""
    host = cfg.get("imap_host") or "imap.gmail.com"
    porta = int(cfg.get("imap_port") or 993)

    email_alvo = args.email
    if args.aluno:
        import banco_dados

        aluno = banco_dados.obter_aluno_por_id(args.aluno)
        if not aluno:
            print(f"ERRO: aluno {args.aluno} nao encontrado.")
            return 2
        email_alvo = aluno["email"]
        print(f"Aluno {args.aluno}: {aluno['nome']} <{aluno['email']}>")

    if not pass_:
        print("ERRO: senha SMTP/IMAP nao configurada (PREP_SMTP_PASS).")
        return 2

    print(f"Conectando em {host}:{porta} como {user} ...")
    try:
        M = imaplib.IMAP4_SSL(host, porta)
        M.login(user, pass_)
    except Exception as exc:
        print(f"ERRO IMAP: {type(exc).__name__}: {exc}")
        return 1
    print("LOGIN IMAP: OK\n")

    pastas = _pastas(M)
    pasta_env = _pasta_enviados(pastas)
    if not pasta_env:
        print("AVISO: pasta de enviados nao encontrada. Pastas:", pastas)
        M.logout()
        return 1

    limite = datetime.now() - timedelta(days=args.dias)
    print("=" * 72)
    print(f"ENTREGAS ACEITAS PELO GMAIL (pasta: {pasta_env})")
    print("=" * 72)
    encontradas = []
    for m in _buscar_cabecalhos(M, pasta_env, limite=100):
        if m["dt"] and m["dt"].tzinfo is not None and m["dt"].astimezone().replace(tzinfo=None) < limite:
            continue
        if not _casar(m, email_alvo, args.protocolo):
            continue
        encontradas.append(m)
        print(f"  Date   : {m['date']}")
        print(f"  From   : {m['from']}")
        print(f"  To     : {m['to']}")
        print(f"  Subject: {m['subject']}")
        print(f"  Msg-ID : {m['message_id']}")
        print("  ---")
    if not encontradas:
        print("  (nenhuma mensagem correspondente)")

    print()
    print("=" * 72)
    print("AVISOS DE FALHA DE ENTREGA (bounce / NDR) EM TODAS AS PASTAS")
    print("=" * 72)
    bounces = []
    for pasta in pastas:
        for m in _buscar_cabecalhos(M, pasta, limite=60):
            blob = f"{m['from']} {m['to']} {m['subject']}".lower()
            if any(t in blob for t in TERMOS_BOUNCE):
                bounces.append((pasta, m))
    if bounces:
        for pasta, m in bounces:
            print(f"  [Pasta: {pasta}]")
            print(f"  Date   : {m['date']}")
            print(f"  Subject: {m['subject']}")
            print("  ---")
    else:
        print("  Nenhum aviso de falha de entrega encontrado.")

    M.logout()

    print()
    if bounces:
        print("VEREDITO: HAV E FALHA DE ENTREGA registrada. Verifique as mensagens acima.")
        return 1
    if encontradas:
        print(
            f"VEREDITO: {len(encontradas)} entrega(s) ACEITA(S) pelo Gmail e sem bounce. "
            "Se o aluno nao visualizing, o problema e filtro de spam/promocoes ou "
            "endereco divergente - nao a emissao."
        )
        return 0
    print("VEREDITO: nenhuma entrega correspondente encontrada na janela de tempo.")
    return 2


if __name__ == "__main__":
    sys.exit(main())
