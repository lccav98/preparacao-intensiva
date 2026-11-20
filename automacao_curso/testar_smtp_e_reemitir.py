#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Testa o SMTP configurado no .env e (opcionalmente) reemite uma folha de prova.

Uso (a partir de automacao_curso/):
    python testar_smtp_e_reemitir.py
    python testar_smtp_e_reemitir.py --emitir 1 --disciplina matrizes_vetores --bloco A01
"""

import argparse
import smtplib
import sys

import config
import servidor_dashboard


def testar_smtp() -> bool:
    cfg = config.obter_integracoes()
    print("=" * 68)
    print("TESTE DE SMTP")
    print("=" * 68)
    print(f"  host       : {cfg['smtp_host']}:{cfg['smtp_port']}")
    print(f"  usuario    : {cfg['smtp_user']}")
    print(f"  remetente  : {cfg['smtp_from']}")
    print(f"  senha      : {'CONFIGURADA' if cfg['smtp_pass'] else 'VAZIA (PREP_SMTP_PASS)'}")
    if not (cfg["smtp_host"] and cfg["smtp_user"] and cfg["smtp_pass"]):
        print("  RESULTADO  : SMTP NAO CONFIGURADO -> as folhas vao para o spool local.")
        return False
    porta = int(cfg["smtp_port"])
    try:
        if porta == 465:
            srv = smtplib.SMTP_SSL(cfg["smtp_host"], porta, timeout=20)
        else:
            srv = smtplib.SMTP(cfg["smtp_host"], porta, timeout=20)
            srv.starttls()
        with srv:
            srv.login(cfg["smtp_user"], cfg["smtp_pass"])
        print("  RESULTADO  : CONEXAO SMTP OK (login efetuado)")
        return True
    except Exception as exc:
        print(f"  RESULTADO  : FALHA -> {type(exc).__name__}: {exc}")
        return False


def reemitir(aluno_id: int, disciplina: str, bloco: str, modo: str, variante: str, tentativa: int) -> None:
    orq = servidor_dashboard.obter_orquestrador()
    res = orq.emitir_e_enviar_prova(
        aluno_id=aluno_id,
        bloco_id=bloco,
        variante=variante,
        tentativa=tentativa,
        modo=modo,
        disciplina=disciplina,
    )
    prova, email = res["prova"], res["email"]
    print("=" * 68)
    print("FOLHA REEMITIDA")
    print("=" * 68)
    print(f"  protocolo    : {prova['protocolo']}")
    print(
        f"  aluno        : id {prova['aluno_id']} | bloco {prova['bloco']} "
        f"{prova['variante']} T{prova['tentativa']} | modo {prova['modo']}"
    )
    print(f"  modo_entrega : {email.get('modo_entrega')} (enviado_smtp={email.get('enviado_smtp')})")
    if email.get("erro_smtp"):
        print(f"  erro_smtp    : {email['erro_smtp']}")
    print(f"  arquivo .eml : {email.get('caminho_eml')}")
    print(f"  url publica  : {config.PUBLIC_URL or '(PREP_PUBLIC_URL vazio)'}")


def main() -> int:
    ap = argparse.ArgumentParser(description="Testa o SMTP e reemite folha de prova.")
    ap.add_argument("--emitir", type=int, metavar="ALUNO_ID", help="reemite a folha para este aluno")
    ap.add_argument("--disciplina", default="matrizes_vetores")
    ap.add_argument("--bloco", default="A01")
    ap.add_argument("--modo", default="pratica", choices=["pratica", "checagem"])
    ap.add_argument("--variante", default="V1")
    ap.add_argument("--tentativa", type=int, default=1)
    args = ap.parse_args()

    ok = testar_smtp()
    if args.emitir:
        reemitir(args.emitir, args.disciplina, args.bloco, args.modo, args.variante, args.tentativa)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
