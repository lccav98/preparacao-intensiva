#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Configuracoes centrais do sistema de automacao do Curso de Preparação Intensiva em Algoritmos em C (UTFPR-PG).
"""

import json
import os
from typing import Any, Dict, List


def _carregar_arquivo_env(caminho: str) -> None:
    """Carrega um arquivo .env no ambiente sem sobrescrever variaveis ja existentes.

    Sem isso, iniciar `python servidor_dashboard.py` direto (sem o .bat) ignora
    PREP_PUBLIC_URL, PREP_ADMIN_PASSWORD, PREP_SMTP_* e PREP_DATA_DIR.
    """
    if not os.path.isfile(caminho):
        return
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if not linha or linha.startswith("#") or "=" not in linha:
                    continue
                chave, _, valor = linha.partition("=")
                chave = chave.strip()
                valor = valor.strip()
                if len(valor) >= 2 and valor[0] == valor[-1] and valor[0] in ("'", '"'):
                    valor = valor[1:-1]
                if chave and chave not in os.environ:
                    os.environ[chave] = valor
    except OSError:
        pass


# O .env fica na raiz do curso (mesma pasta do README e do iniciar_painel_mv.bat).
_RAIZ_CURSO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_carregar_arquivo_env(os.environ.get("PREP_ENV_FILE", "").strip() or os.path.join(_RAIZ_CURSO, ".env"))

CURSO_DIR = os.path.abspath(
    os.environ.get(
        "PREP_CURSO_DIR",
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    )
)
PROJECT_ROOT = os.path.dirname(CURSO_DIR)

AUTOMACAO_DIR = os.path.join(CURSO_DIR, "automacao_curso")
# PREP_DATA_DIR = pasta RAIZ dos dados de runtime (contem dados/, folhas_emitidas/,
# spool_email/). Caminhos relativos sao resolvidos a partir da RAIZ DO CURSO
# (nunca do CWD), senao o servidor cria um banco paralelo ao iniciar de outro lugar.
DATA_ROOT = os.environ.get("PREP_DATA_DIR", "").strip()
if DATA_ROOT:
    _RUNTIME_ROOT = os.path.abspath(
        DATA_ROOT if os.path.isabs(DATA_ROOT) else os.path.join(_RAIZ_CURSO, DATA_ROOT)
    )
else:
    _RUNTIME_ROOT = AUTOMACAO_DIR

DADOS_DIR = os.path.join(_RUNTIME_ROOT, "dados")
DB_PATH = os.path.join(DADOS_DIR, "automacao.db")
INTEGRACOES_CONFIG_PATH = os.path.join(DADOS_DIR, "integracoes_config.json")
CSV_ACOMPANHAMENTO_PATH = (
    os.path.join(_RUNTIME_ROOT, "00_acompanhamento.csv")
    if DATA_ROOT
    else os.path.join(CURSO_DIR, "00_acompanhamento.csv")
)

FOLHAS_DIR = os.path.join(_RUNTIME_ROOT, "folhas_emitidas")
SPOOL_DIR = os.path.join(_RUNTIME_ROOT, "spool_email")
SPOOL_ENVIADOS_DIR = os.path.join(SPOOL_DIR, "enviados")
SPOOL_RECEBIDOS_DIR = os.path.join(SPOOL_DIR, "recebidos")
UPLOADS_DIR = os.path.join(_RUNTIME_ROOT, "uploads_provas")
UI_DIR = os.path.join(AUTOMACAO_DIR, "ui")
LOGIN_HTML_PATH = os.path.join(UI_DIR, "login.html")
PORTAL_ALUNO_HTML_PATH = os.path.join(UI_DIR, "portal_aluno.html")
DASHBOARD_HTML_PATH = os.path.join(UI_DIR, "dashboard.html")
DASHBOARD_SNAPSHOT_PATH = os.path.join(_RUNTIME_ROOT, "dashboard_evolucao.html")

ESTAGIOS_META = [
    ("estagio_A", "A", 10, "Estagio A - Fundamentos, Variaveis, E/S e Binario"),
    ("estagio_B", "B", 10, "Estagio B - Expressoes, Operadores e Condicionais"),
    ("estagio_C", "C", 10, "Estagio C - Estruturas de Repeticao e Series"),
    ("estagio_D", "D", 10, "Estagio D - Vetores Unidimensionais e Strings"),
    ("estagio_E", "E", 8,  "Estagio E - Matrizes Bidimensionais e PGM P2"),
    ("estagio_F", "F", 10, "Estagio F - Modularizacao, Funcoes e Ponteiros"),
    ("estagio_G", "G", 9,  "Estagio G - Recursividade e Pilha de Execucao"),
    ("estagio_H", "H", 6,  "Estagio H - Integracao Geral e Projeto PGM"),
]

_MV_EMBUTIDO = os.path.join(CURSO_DIR, "cursos", "matrizes_vetores")
_MV_PADRAO_WIN = os.path.join(
    os.path.dirname(PROJECT_ROOT),
    "Matrizes e Vetores",
    "Curso_Preparacao_Intensiva_Matrizes_Vetores",
)
CURSO_MV_DIR = os.path.abspath(
    os.environ.get("PREP_CURSO_MV_DIR", "").strip()
    or (_MV_EMBUTIDO if os.path.isdir(_MV_EMBUTIDO) else _MV_PADRAO_WIN)
)
CSV_ACOMPANHAMENTO_MV_PATH = (
    os.path.join(_RUNTIME_ROOT, "00_acompanhamento_mv.csv")
    if DATA_ROOT
    else os.path.join(CURSO_MV_DIR, "00_acompanhamento.csv")
)

ESTAGIOS_META_MV = [
    ("estagio_A", "A", 9,  "Estagio A - Matrizes, Operacoes, Transposta e Especiais"),
    ("estagio_B", "B", 9,  "Estagio B - Determinantes, Inversa [A|I] e Equacoes Matriciais"),
    ("estagio_C", "C", 8,  "Estagio C - Sistemas Lineares, Escalonamento, Posto e Parametros"),
    ("estagio_D", "D", 10, "Estagio D - Vetores no R2/R3, Produtos, Areas e Volumes"),
    ("estagio_E", "E", 10, "Estagio E - Retas, Planos e Distancias no R3"),
    ("estagio_F", "F", 8,  "Estagio F - Secoes Conicas e Quadricas Canonicas"),
    ("estagio_G", "G", 6,  "Estagio G - Simulados Integradores P1, P2, P3 e Reavaliacao"),
]

_DISCIPLINA_PADRAO_ENV = os.environ.get("DISCIPLINA_PADRAO", "algoritmos").strip().lower()
if _DISCIPLINA_PADRAO_ENV in ("matrizes_vetores", "mv", "mat121", "matrizes", "re42b"):
    DISCIPLINA_PADRAO = "matrizes_vetores"
elif _DISCIPLINA_PADRAO_ENV in ("algoritmos", "cc61a", "c", "alg"):
    DISCIPLINA_PADRAO = "algoritmos"
else:
    DISCIPLINA_PADRAO = "algoritmos"

DISCIPLINAS: Dict[str, Dict[str, Any]] = {
    "algoritmos": {
        "id": "algoritmos",
        "codigo": "CC61A",
        "nome": "Algoritmos e Programacao em C",
        "nome_curto": "Algoritmos C (CC61A)",
        "tag_email": "Algoritmos C - UTFPR",
        "prefixo_protocolo": "PREP",
        "curso_dir": CURSO_DIR,
        "csv_path": CSV_ACOMPANHAMENTO_PATH,
        "estagios_meta": ESTAGIOS_META,
        "total_blocos": sum(x[2] for x in ESTAGIOS_META),
        "tipo_avaliacao": "codigo_c",
    },
    "matrizes_vetores": {
        "id": "matrizes_vetores",
        "codigo": "MAT121",
        "nome": "Matrizes e Vetores",
        "nome_curto": "Matrizes e Vetores (MAT121)",
        "tag_email": "Matrizes e Vetores - UTFPR",
        "prefixo_protocolo": "PREP-MV",
        "curso_dir": CURSO_MV_DIR,
        "csv_path": CSV_ACOMPANHAMENTO_MV_PATH,
        "estagios_meta": ESTAGIOS_META_MV,
        "total_blocos": sum(x[2] for x in ESTAGIOS_META_MV),
        "tipo_avaliacao": "matematica",
    },
}


def normalizar_disciplina_id(disciplina_id: str = "") -> str:
    d = str(disciplina_id or "").strip().lower()
    if d in ("matrizes_vetores", "mv", "mat121", "matrizes", "re42b"):
        return "matrizes_vetores"
    if d in ("algoritmos", "cc61a", "c", "alg", ""):
        return "algoritmos"
    if d in DISCIPLINAS:
        return d
    raise ValueError(f"Disciplina desconhecida: '{disciplina_id}'")


def obter_disciplina(disciplina_id: str = DISCIPLINA_PADRAO) -> Dict[str, Any]:
    return DISCIPLINAS[normalizar_disciplina_id(disciplina_id)]


def listar_disciplinas() -> List[Dict[str, Any]]:
    out = []
    for k in ("algoritmos", "matrizes_vetores"):
        d = DISCIPLINAS[k]
        out.append(
            {
                "id": d["id"],
                "codigo": d["codigo"],
                "nome": d["nome"],
                "nome_curto": d["nome_curto"],
                "total_blocos": d["total_blocos"],
                "prefixo_protocolo": d["prefixo_protocolo"],
                "disponivel": os.path.isdir(d["curso_dir"]),
            }
        )
    return out


def disciplina_por_protocolo(protocolo: str) -> str:
    p = str(protocolo or "").strip().upper()
    if p.startswith("PREP-MV-"):
        return "matrizes_vetores"
    return "algoritmos"

# Configuracoes opcionais de SMTP / IMAP (se ausentes, opera via Spool local deterministico)
SMTP_HOST = os.environ.get("PREP_SMTP_HOST", "")
SMTP_PORT = int(os.environ.get("PREP_SMTP_PORT", "587"))
SMTP_USER = os.environ.get("PREP_SMTP_USER", "")
SMTP_PASS = os.environ.get("PREP_SMTP_PASS", "")
SMTP_FROM = os.environ.get("PREP_SMTP_FROM", "tutor-algoritmos@utfpr-preparacao.local")

IMAP_HOST = os.environ.get("PREP_IMAP_HOST", "")
IMAP_PORT = int(os.environ.get("PREP_IMAP_PORT", "993"))
IMAP_USER = os.environ.get("PREP_IMAP_USER", "")
IMAP_PASS = os.environ.get("PREP_IMAP_PASS", "")
IMAP_POLL_SEC = int(os.environ.get("PREP_IMAP_POLL_SEC", "15"))
WEBHOOK_TOKEN = os.environ.get("PREP_WEBHOOK_TOKEN", "").strip()

# Configuracoes JEV System One (Camada 1)
JEV_API_URL = os.environ.get("JEV_API_URL", "https://api.typesafe.ai/v1/systemone")
JEV_API_KEY = (
    os.environ.get("TYPESAFE_API_KEY")
    or os.environ.get("JEV_API_KEY")
    or ""
)
JEV_CONFIDENCE_THRESHOLD = 0.75

# Configuracoes opcionais de Visao OCR externa
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = os.environ.get("PREP_GEMINI_MODEL", "gemini-2.5-flash")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")

# Servidor Dashboard & Autenticacao
DASHBOARD_HOST = os.environ.get(
    "PREP_DASHBOARD_HOST",
    "0.0.0.0" if os.environ.get("PORT") else "127.0.0.1",
)
DASHBOARD_PORT = int(os.environ.get("PORT") or os.environ.get("PREP_DASHBOARD_PORT") or "8090")
PUBLIC_URL = os.environ.get("PREP_PUBLIC_URL", "").strip().rstrip("/")


def obter_public_url() -> str:
    """Retorna a URL publica ativa, relendo PREP_PUBLIC_URL do .env caso o tunel tenha sido atualizado."""
    env_path = os.environ.get("PREP_ENV_FILE", "").strip() or os.path.join(_RAIZ_CURSO, ".env")
    if os.path.isfile(env_path):
        try:
            with open(env_path, "r", encoding="utf-8") as f:
                for linha in f:
                    s = linha.strip()
                    if not s or s.startswith("#") or "=" not in s:
                        continue
                    k, _, v = s.partition("=")
                    if k.strip() == "PREP_PUBLIC_URL":
                        val = v.strip().strip("'").strip('"').rstrip("/")
                        if val:
                            return val
        except OSError:
            pass
    return (os.environ.get("PREP_PUBLIC_URL", "").strip() or PUBLIC_URL).rstrip("/")
ADMIN_EMAIL = os.environ.get("PREP_ADMIN_EMAIL", "lcezenilda@gmail.com").strip().lower()
ADMIN_PASSWORD = os.environ.get("PREP_ADMIN_PASSWORD", "").strip()
SECRET_KEY = os.environ.get("PREP_SECRET_KEY", "").strip()


def garantir_diretorios():
    """Garante que todos os diretorios operacionais de automacao existam."""
    dirs = [
        AUTOMACAO_DIR,
        DADOS_DIR,
        FOLHAS_DIR,
        SPOOL_DIR,
        SPOOL_ENVIADOS_DIR,
        SPOOL_RECEBIDOS_DIR,
        UPLOADS_DIR,
        UI_DIR,
    ]
    if DATA_ROOT:
        dirs.insert(0, os.path.abspath(DATA_ROOT))
    for d in dirs:
        os.makedirs(d, exist_ok=True)


def _normalizar_senha_smtp(valor: str) -> str:
    """Remove os espacos de agrupamento que o Google usa nas senhas de app.

    O Google exibe a senha de aplicacao como "xxxx xxxx xxxx xxxx" (16 chars).
    O `smtplib` NAO remove espacos sozinho, entao um espaco residual faz o
    login falhar com 535. Removemos apenas quando o padrao 4-4-4-4 bate;
    caso contrario a senha e preservada exatamente como foi digitada.
    """
    texto = (valor or "").strip()
    partes = texto.split()
    if len(partes) == 4 and all(len(p) == 4 for p in partes):
        return "".join(partes)
    return texto


def obter_integracoes() -> Dict[str, Any]:
    """Combina integracoes_config.json (se existir) com variaveis de ambiente."""
    arquivo_cfg: Dict[str, Any] = {}
    if os.path.isfile(INTEGRACOES_CONFIG_PATH):
        try:
            with open(INTEGRACOES_CONFIG_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, dict):
                arquivo_cfg = data
        except Exception:
            arquivo_cfg = {}

    smtp_host = (os.environ.get("PREP_SMTP_HOST") or str(arquivo_cfg.get("smtp_host", ""))).strip()
    smtp_port = int(os.environ.get("PREP_SMTP_PORT") or arquivo_cfg.get("smtp_port") or 587)
    smtp_user = (os.environ.get("PREP_SMTP_USER") or str(arquivo_cfg.get("smtp_user", ""))).strip()
    smtp_pass = _normalizar_senha_smtp(
        os.environ.get("PREP_SMTP_PASS") or str(arquivo_cfg.get("smtp_pass", ""))
    )
    smtp_from = (
        os.environ.get("PREP_SMTP_FROM")
        or str(arquivo_cfg.get("smtp_from", ""))
        or smtp_user
        or SMTP_FROM
    ).strip()

    imap_host = (os.environ.get("PREP_IMAP_HOST") or str(arquivo_cfg.get("imap_host", ""))).strip()
    imap_port = int(os.environ.get("PREP_IMAP_PORT") or arquivo_cfg.get("imap_port") or 993)
    imap_user = (os.environ.get("PREP_IMAP_USER") or str(arquivo_cfg.get("imap_user", ""))).strip()
    imap_pass = os.environ.get("PREP_IMAP_PASS") or str(arquivo_cfg.get("imap_pass", ""))
    imap_poll_sec = max(
        3,
        int(os.environ.get("PREP_IMAP_POLL_SEC") or arquivo_cfg.get("imap_poll_sec") or IMAP_POLL_SEC),
    )

    gemini_key = (
        os.environ.get("GEMINI_API_KEY") or str(arquivo_cfg.get("gemini_api_key", ""))
    ).strip()
    gemini_model = (
        os.environ.get("PREP_GEMINI_MODEL") or str(arquivo_cfg.get("gemini_model", "")) or GEMINI_MODEL
    ).strip()
    brevo_key = (
        os.environ.get("BREVO_API_KEY")
        or os.environ.get("PREP_BREVO_API_KEY")
        or str(arquivo_cfg.get("brevo_api_key", ""))
    ).strip()
    webhook_token = (
        os.environ.get("PREP_WEBHOOK_TOKEN") or str(arquivo_cfg.get("webhook_token", ""))
    ).strip()

    return {
        "smtp_host": smtp_host,
        "smtp_port": smtp_port,
        "smtp_user": smtp_user,
        "smtp_pass": smtp_pass,
        "smtp_from": smtp_from,
        "imap_host": imap_host,
        "imap_port": imap_port,
        "imap_user": imap_user,
        "imap_pass": imap_pass,
        "imap_poll_sec": imap_poll_sec,
        "gemini_api_key": gemini_key,
        "gemini_model": gemini_model,
        "brevo_api_key": brevo_key,
        "webhook_token": webhook_token,
    }


def salvar_integracoes(novos_dados: Dict[str, Any]) -> Dict[str, Any]:
    """Salva configuracoes dinamicas em INTEGRACOES_CONFIG_PATH preservando segredos em branco."""
    garantir_diretorios()
    atual: Dict[str, Any] = {}
    if os.path.isfile(INTEGRACOES_CONFIG_PATH):
        try:
            with open(INTEGRACOES_CONFIG_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, dict):
                atual = data
        except Exception:
            atual = {}

    merged = dict(atual)
    campos_texto = [
        "smtp_host",
        "smtp_user",
        "smtp_from",
        "imap_host",
        "imap_user",
        "gemini_model",
    ]
    for c in campos_texto:
        if c in novos_dados and novos_dados[c] is not None:
            merged[c] = str(novos_dados[c]).strip()

    for cp in ("smtp_port", "imap_port", "imap_poll_sec"):
        if cp in novos_dados and str(novos_dados[cp]).strip():
            merged[cp] = int(novos_dados[cp])

    for cs in ("smtp_pass", "imap_pass", "gemini_api_key", "brevo_api_key", "webhook_token"):
        if cs in novos_dados:
            val = str(novos_dados[cs] or "").strip()
            if val:
                merged[cs] = val

    with open(INTEGRACOES_CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)

    return obter_integracoes()
