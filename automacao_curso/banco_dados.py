#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Persistencia SQLite e sincronizacao automatica com 00_acompanhamento.csv
com suporte completo a multiplas disciplinas (Algoritmos CC61A e Matrizes e Vetores MAT121).
"""

import csv
import datetime
import hashlib
import hmac
import os
import re
import secrets
import sqlite3
from typing import Any, Dict, List, Optional

import config

CSV_COLUNAS = [
    "data",
    "aluno",
    "bloco",
    "variante",
    "tentativa",
    "tempo_resolucao",
    "acertos_iniciais",
    "total_questoes",
    "acertos_apos_correcao",
    "resultado_checagem",
    "dificuldade_observada",
    "proxima_acao",
]


def _agora_iso() -> str:
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def _hoje_br() -> str:
    return datetime.datetime.now().strftime("%Y-%m-%d")


def gerar_pin_acesso() -> str:
    """Gera PIN numerico aleatorio de 6 digitos para primeiro acesso do aluno."""
    return f"{100000 + secrets.randbelow(900000)}"


def hash_senha(senha: str) -> str:
    """Gera hash PBKDF2-HMAC-SHA256 com salt aleatorio."""
    salt = secrets.token_hex(16)
    dk = hashlib.pbkdf2_hmac("sha256", senha.encode("utf-8"), salt.encode("ascii"), 120_000).hex()
    return f"pbkdf2_sha256$120000${salt}${dk}"


def verificar_senha(senha: str, senha_hash: str) -> bool:
    """Valida senha contra hash PBKDF2-HMAC-SHA256 em tempo constante."""
    if not senha or not senha_hash or "$" not in senha_hash:
        return False
    partes = senha_hash.split("$")
    if len(partes) != 4 or partes[0] != "pbkdf2_sha256":
        return False
    try:
        iters = int(partes[1])
        salt = partes[2]
        expected = partes[3]
    except ValueError:
        return False
    actual = hashlib.pbkdf2_hmac("sha256", senha.encode("utf-8"), salt.encode("ascii"), iters).hex()
    return hmac.compare_digest(actual, expected)


def _sanitizar_aluno(aluno: Dict[str, Any], incluir_pin: bool = False) -> Dict[str, Any]:
    out = dict(aluno)
    out.pop("senha_hash", None)
    if not incluir_pin:
        out.pop("pin_inicial", None)
    return out


def _disciplina_publica(disciplina: str) -> Dict[str, Any]:
    d = config.obter_disciplina(disciplina)
    return {
        "id": d["id"],
        "codigo": d["codigo"],
        "nome": d["nome"],
        "nome_curto": d["nome_curto"],
        "periodo": int(d.get("periodo", 1)),
        "carga_horaria": int(d.get("carga_horaria", 60)),
        "pre_requisitos": list(d.get("pre_requisitos") or []),
        "prefixo_protocolo": d["prefixo_protocolo"],
        "total_blocos": d["total_blocos"],
        "tipo_avaliacao": d["tipo_avaliacao"],
        "csv_filename": d.get("csv_filename", "00_acompanhamento.csv"),
        "objetivos": list(d.get("objetivos") or []),
        "material_apoio": list(d.get("material_apoio") or []),
    }


def _garantir_credenciais_alunos_conn(conn: sqlite3.Connection) -> None:
    pendentes = conn.execute(
        "SELECT id FROM alunos WHERE COALESCE(senha_hash, '') = ''"
    ).fetchall()
    for row in pendentes:
        pin = gerar_pin_acesso()
        conn.execute(
            "UPDATE alunos SET senha_hash = ?, pin_inicial = ? WHERE id = ?",
            (hash_senha(pin), pin, row["id"]),
        )
    if pendentes:
        conn.commit()


def _backfill_matriculas_conn(conn: sqlite3.Connection) -> None:
    """Garante que todo aluno preexistente em 'alunos' possua matricula em 'algoritmos' preservando estado."""
    alunos_rows = conn.execute("SELECT * FROM alunos ORDER BY id ASC").fetchall()
    for al in alunos_rows:
        tem_alg = conn.execute(
            "SELECT 1 FROM matriculas WHERE aluno_id = ? AND disciplina = 'algoritmos'",
            (al["id"],),
        ).fetchone()
        if tem_alg:
            continue
        alguma = conn.execute(
            "SELECT 1 FROM matriculas WHERE aluno_id = ?",
            (al["id"],),
        ).fetchone()
        if not alguma:
            conn.execute(
                """
                INSERT INTO matriculas
                (aluno_id, disciplina, bloco_atual, variante_atual, tentativa_bloco, modo_atual, status_curso, criado_em)
                VALUES (?, 'algoritmos', ?, ?, ?, ?, ?, ?)
                """,
                (
                    al["id"],
                    al["bloco_atual"],
                    al["variante_atual"],
                    al["tentativa_bloco"],
                    al["modo_atual"],
                    al["status_curso"],
                    al["criado_em"],
                ),
            )
    conn.commit()


def conectar() -> sqlite3.Connection:
    config.garantir_diretorios()
    conn = sqlite3.connect(config.DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def inicializar_banco() -> None:
    with conectar() as conn:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                bloco_atual TEXT NOT NULL DEFAULT 'A01',
                variante_atual TEXT NOT NULL DEFAULT 'V1',
                tentativa_bloco INTEGER NOT NULL DEFAULT 1,
                modo_atual TEXT NOT NULL DEFAULT 'checagem',
                status_curso TEXT NOT NULL DEFAULT 'EM_ANDAMENTO',
                criado_em TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS matriculas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                aluno_id INTEGER NOT NULL,
                disciplina TEXT NOT NULL DEFAULT 'algoritmos',
                bloco_atual TEXT NOT NULL DEFAULT 'A01',
                variante_atual TEXT NOT NULL DEFAULT 'V1',
                tentativa_bloco INTEGER NOT NULL DEFAULT 1,
                modo_atual TEXT NOT NULL DEFAULT 'pratica',
                status_curso TEXT NOT NULL DEFAULT 'EM_ANDAMENTO',
                criado_em TEXT NOT NULL,
                UNIQUE(aluno_id, disciplina),
                FOREIGN KEY (aluno_id) REFERENCES alunos(id)
            );

            CREATE TABLE IF NOT EXISTS provas_emitidas (
                protocolo TEXT PRIMARY KEY,
                aluno_id INTEGER NOT NULL,
                disciplina TEXT NOT NULL DEFAULT 'algoritmos',
                bloco TEXT NOT NULL,
                variante TEXT NOT NULL,
                tentativa INTEGER NOT NULL,
                modo TEXT NOT NULL,
                tempo_alvo_min INTEGER NOT NULL,
                caminho_folha_html TEXT NOT NULL,
                caminho_email_eml TEXT DEFAULT '',
                enviado_em TEXT NOT NULL,
                inicio_cronometro_em TEXT DEFAULT '',
                fim_cronometro_em TEXT DEFAULT '',
                tempo_cronometrado_min REAL DEFAULT 0,
                status TEXT NOT NULL DEFAULT 'emitida',
                FOREIGN KEY (aluno_id) REFERENCES alunos(id)
            );

            CREATE TABLE IF NOT EXISTS submissoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                protocolo TEXT NOT NULL,
                aluno_id INTEGER NOT NULL,
                disciplina TEXT NOT NULL DEFAULT 'algoritmos',
                bloco TEXT NOT NULL,
                variante TEXT NOT NULL,
                tentativa INTEGER NOT NULL,
                modo TEXT NOT NULL,
                recebido_em TEXT NOT NULL,
                caminho_imagem TEXT DEFAULT '',
                tempo_declarado_min REAL NOT NULL DEFAULT 0,
                tempo_janela_min REAL NOT NULL DEFAULT 0,
                fluencia_tempo TEXT NOT NULL DEFAULT 'dentro_meta',
                acertos_iniciais INTEGER NOT NULL,
                total_questoes INTEGER NOT NULL,
                acertos_apos_correcao INTEGER NOT NULL,
                percentual_acerto REAL NOT NULL,
                resultado_checagem TEXT NOT NULL,
                dificuldade_observada TEXT NOT NULL,
                proxima_acao TEXT NOT NULL,
                bloco_destino TEXT NOT NULL,
                relatorio_feedback_html TEXT NOT NULL,
                caminho_email_feedback TEXT DEFAULT '',
                camada_predominante TEXT NOT NULL DEFAULT 'local',
                FOREIGN KEY (aluno_id) REFERENCES alunos(id)
            );

            CREATE TABLE IF NOT EXISTS itens_submissao (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                submissao_id INTEGER NOT NULL,
                questao_id TEXT NOT NULL,
                tipo_questao TEXT NOT NULL,
                resposta_extraida TEXT NOT NULL,
                status_correcao TEXT NOT NULL,
                categoria_erro TEXT NOT NULL DEFAULT '',
                feedback_item TEXT NOT NULL,
                camada_avaliacao TEXT NOT NULL DEFAULT 'local',
                confianca REAL NOT NULL DEFAULT 1.0,
                FOREIGN KEY (submissao_id) REFERENCES submissoes(id)
            );

            CREATE TABLE IF NOT EXISTS metricas_jev (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                camada TEXT NOT NULL,
                modulo TEXT NOT NULL,
                confianca REAL NOT NULL,
                detalhes TEXT DEFAULT ''
            );

            CREATE TABLE IF NOT EXISTS emails_processados (
                msg_chave TEXT PRIMARY KEY,
                protocolo TEXT DEFAULT '',
                remetente TEXT DEFAULT '',
                assunto TEXT DEFAULT '',
                status TEXT NOT NULL,
                detalhes TEXT DEFAULT '',
                processado_em TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS componentes_integralizacao (
                aluno_id INTEGER NOT NULL,
                componente_key TEXT NOT NULL,
                horas_cumpridas REAL NOT NULL DEFAULT 0,
                observacoes TEXT DEFAULT '',
                atualizado_em TEXT NOT NULL,
                PRIMARY KEY (aluno_id, componente_key),
                FOREIGN KEY (aluno_id) REFERENCES alunos(id)
            );
            """
        )
        cols_provas = [r["name"] for r in conn.execute("PRAGMA table_info(provas_emitidas)").fetchall()]
        if "fim_cronometro_em" not in cols_provas:
            conn.execute("ALTER TABLE provas_emitidas ADD COLUMN fim_cronometro_em TEXT DEFAULT ''")
        if "tempo_cronometrado_min" not in cols_provas:
            conn.execute("ALTER TABLE provas_emitidas ADD COLUMN tempo_cronometrado_min REAL DEFAULT 0")
        if "disciplina" not in cols_provas:
            conn.execute("ALTER TABLE provas_emitidas ADD COLUMN disciplina TEXT NOT NULL DEFAULT 'algoritmos'")

        cols_subs = [r["name"] for r in conn.execute("PRAGMA table_info(submissoes)").fetchall()]
        if "disciplina" not in cols_subs:
            conn.execute("ALTER TABLE submissoes ADD COLUMN disciplina TEXT NOT NULL DEFAULT 'algoritmos'")

        cols_alunos = [r["name"] for r in conn.execute("PRAGMA table_info(alunos)").fetchall()]
        if "senha_hash" not in cols_alunos:
            conn.execute("ALTER TABLE alunos ADD COLUMN senha_hash TEXT DEFAULT ''")
        if "pin_inicial" not in cols_alunos:
            conn.execute("ALTER TABLE alunos ADD COLUMN pin_inicial TEXT DEFAULT ''")

        conn.commit()
        _garantir_credenciais_alunos_conn(conn)
        _backfill_matriculas_conn(conn)


def obter_matricula(aluno_id: int, disciplina: str = config.DISCIPLINA_PADRAO) -> Optional[Dict[str, Any]]:
    inicializar_banco()
    disc_id = config.normalizar_disciplina_id(disciplina)
    with conectar() as conn:
        row = conn.execute(
            "SELECT * FROM matriculas WHERE aluno_id = ? AND disciplina = ?",
            (aluno_id, disc_id),
        ).fetchone()
        return dict(row) if row else None


def _ordem_blocos_meta(disc_id: str) -> List[str]:
    disc = config.obter_disciplina(disc_id)
    ordem: List[str] = []
    for _dir, pref, qtd, _tit in disc["estagios_meta"]:
        for i in range(1, int(qtd) + 1):
            ordem.append(f"{pref}{i:02d}")
    return ordem


def _validar_bloco_disciplina(
    disc_id: str, bloco_id: str, fallback_a01: bool = False
) -> str:
    ordem = _ordem_blocos_meta(disc_id)
    bloco_norm = (bloco_id or (ordem[0] if ordem else "A01")).strip().upper()
    if not ordem:
        return bloco_norm
    if bloco_norm in ordem:
        return bloco_norm
    if fallback_a01:
        return ordem[0]
    raise ValueError(
        f"Bloco '{bloco_norm}' invalido para disciplina '{disc_id}'. Blocos validos: {ordem[0]}..{ordem[-1]}."
    )


def _ultimo_bloco_disciplina(disc_id: str) -> str:
    ordem = _ordem_blocos_meta(disc_id)
    return ordem[-1] if ordem else "A01"


def listar_matriculas_aluno(aluno_id: int) -> List[Dict[str, Any]]:
    inicializar_banco()
    with conectar() as conn:
        rows = conn.execute(
            "SELECT * FROM matriculas WHERE aluno_id = ? ORDER BY id ASC",
            (aluno_id,),
        ).fetchall()
        return [dict(r) for r in rows]


def matricular_aluno(
    aluno_id: int,
    disciplina: str = config.DISCIPLINA_PADRAO,
    bloco_inicial: str = "A01",
    modo_inicial: str = "pratica",
    status_curso: str = "EM_ANDAMENTO",
    atualizar_existente: bool = False,
) -> Dict[str, Any]:
    inicializar_banco()
    disc_id = config.normalizar_disciplina_id(disciplina)
    bloco_norm = _validar_bloco_disciplina(disc_id, bloco_inicial, fallback_a01=False)
    modo_norm = modo_inicial if modo_inicial in ("pratica", "checagem") else "pratica"
    status_norm = status_curso if status_curso in ("EM_ANDAMENTO", "CONCLUIDO") else "EM_ANDAMENTO"
    with conectar() as conn:
        row_al = conn.execute("SELECT id FROM alunos WHERE id = ?", (aluno_id,)).fetchone()
        if not row_al:
            raise ValueError(f"Aluno ID {aluno_id} nao encontrado.")
        row = conn.execute(
            "SELECT * FROM matriculas WHERE aluno_id = ? AND disciplina = ?",
            (aluno_id, disc_id),
        ).fetchone()
        if row:
            if not atualizar_existente:
                return dict(row)
            conn.execute(
                """
                UPDATE matriculas
                SET bloco_atual = ?, variante_atual = 'V1', tentativa_bloco = 1, modo_atual = ?, status_curso = ?
                WHERE aluno_id = ? AND disciplina = ?
                """,
                (bloco_norm, modo_norm, status_norm, aluno_id, disc_id),
            )
        else:
            conn.execute(
                """
                INSERT INTO matriculas
                (aluno_id, disciplina, bloco_atual, variante_atual, tentativa_bloco, modo_atual, status_curso, criado_em)
                VALUES (?, ?, ?, 'V1', 1, ?, ?, ?)
                """,
                (aluno_id, disc_id, bloco_norm, modo_norm, status_norm, _agora_iso()),
            )
        if disc_id == "algoritmos":
            conn.execute(
                """
                UPDATE alunos
                SET bloco_atual = ?, variante_atual = 'V1', tentativa_bloco = 1, modo_atual = ?, status_curso = ?
                WHERE id = ?
                """,
                (bloco_norm, modo_norm, status_norm, aluno_id),
            )
        conn.commit()
        row = conn.execute(
            "SELECT * FROM matriculas WHERE aluno_id = ? AND disciplina = ?",
            (aluno_id, disc_id),
        ).fetchone()
        return dict(row)


def marcar_periodos_anteriores_concluidos(
    aluno_id: int,
    ate_periodo: int,
    excluir_disciplinas: Optional[List[str]] = None,
) -> List[Dict[str, Any]]:
    """Marca disciplinas de periodos anteriores como CONCLUIDO (aproveitamento para aluno avancado)."""
    inicializar_banco()
    p_lim = int(ate_periodo or 0)
    if p_lim <= 0:
        return []
    excluir = {config.normalizar_disciplina_id(x) for x in (excluir_disciplinas or []) if str(x or "").strip()}
    resultados: List[Dict[str, Any]] = []
    with conectar() as conn:
        row_al = conn.execute("SELECT id FROM alunos WHERE id = ?", (aluno_id,)).fetchone()
        if not row_al:
            raise ValueError(f"Aluno ID {aluno_id} nao encontrado.")
        for d in config.listar_disciplinas():
            if int(d.get("periodo", 1)) > p_lim or d["id"] in excluir:
                continue
            did = d["id"]
            ult_bloco = _ultimo_bloco_disciplina(did)
            row = conn.execute(
                "SELECT * FROM matriculas WHERE aluno_id = ? AND disciplina = ?",
                (aluno_id, did),
            ).fetchone()
            if row:
                if row["status_curso"] == "CONCLUIDO":
                    resultados.append(dict(row))
                    continue
                qtd_subs = int(
                    conn.execute(
                        "SELECT COUNT(*) AS c FROM submissoes WHERE aluno_id = ? AND COALESCE(disciplina, 'algoritmos') = ?",
                        (aluno_id, did),
                    ).fetchone()["c"]
                )
                if qtd_subs == 0:
                    conn.execute(
                        """
                        UPDATE matriculas
                        SET bloco_atual = ?, variante_atual = 'V1', tentativa_bloco = 1, modo_atual = 'checagem', status_curso = 'CONCLUIDO'
                        WHERE aluno_id = ? AND disciplina = ?
                        """,
                        (ult_bloco, aluno_id, did),
                    )
                    if did == "algoritmos":
                        conn.execute(
                            """
                            UPDATE alunos
                            SET bloco_atual = ?, variante_atual = 'V1', tentativa_bloco = 1, modo_atual = 'checagem', status_curso = 'CONCLUIDO'
                            WHERE id = ?
                            """,
                            (ult_bloco, aluno_id),
                        )
            else:
                conn.execute(
                    """
                    INSERT INTO matriculas
                    (aluno_id, disciplina, bloco_atual, variante_atual, tentativa_bloco, modo_atual, status_curso, criado_em)
                    VALUES (?, ?, ?, 'V1', 1, 'checagem', 'CONCLUIDO', ?)
                    """,
                    (aluno_id, did, ult_bloco, _agora_iso()),
                )
                if did == "algoritmos":
                    conn.execute(
                        """
                        UPDATE alunos
                        SET bloco_atual = ?, variante_atual = 'V1', tentativa_bloco = 1, modo_atual = 'checagem', status_curso = 'CONCLUIDO'
                        WHERE id = ?
                        """,
                        (ult_bloco, aluno_id),
                    )
            row_f = conn.execute(
                "SELECT * FROM matriculas WHERE aluno_id = ? AND disciplina = ?",
                (aluno_id, did),
            ).fetchone()
            if row_f:
                resultados.append(dict(row_f))
        conn.commit()
    return resultados


def matricular_aluno_periodo(
    aluno_id: int,
    periodo: int,
    bloco_inicial: str = "A01",
    modo_inicial: str = "pratica",
    atualizar_existente: bool = False,
    concluir_anteriores: bool = False,
) -> List[Dict[str, Any]]:
    """Matricula um aluno em todas as disciplinas de um periodo (1..8)."""
    inicializar_banco()
    p_int = int(periodo)
    discs = [d for d in config.listar_disciplinas() if int(d.get("periodo", 1)) == p_int]
    if not discs:
        raise ValueError(f"Periodo invalido ou sem disciplinas cadastradas: {periodo}")
    if concluir_anteriores and p_int > 1:
        marcar_periodos_anteriores_concluidos(aluno_id, p_int - 1)
    resultados: List[Dict[str, Any]] = []
    for d in discs:
        existente = obter_matricula(aluno_id, disciplina=d["id"])
        bloco_eff = _validar_bloco_disciplina(d["id"], bloco_inicial, fallback_a01=True)
        mat = matricular_aluno(
            aluno_id,
            disciplina=d["id"],
            bloco_inicial=bloco_eff,
            modo_inicial=modo_inicial,
            status_curso="EM_ANDAMENTO",
            atualizar_existente=atualizar_existente,
        )
        out_m = dict(mat)
        out_m["recem_criada"] = existente is None
        resultados.append(out_m)
    return resultados


def matricular_aluno_lote(
    aluno_id: int,
    disciplinas: List[Any],
    bloco_inicial: str = "A01",
    modo_inicial: str = "pratica",
    status_curso: str = "EM_ANDAMENTO",
    atualizar_existente: bool = False,
    concluir_anteriores_ate: int = 0,
) -> List[Dict[str, Any]]:
    """Matricula um aluno em multiplas disciplinas (inclusive de periodos diferentes)."""
    inicializar_banco()
    if not disciplinas:
        raise ValueError("Informe ao menos uma disciplina para matricula em lote.")
    specs: List[Dict[str, Any]] = []
    vistos: set = set()
    for item in disciplinas:
        if isinstance(item, dict):
            did = config.normalizar_disciplina_id(str(item.get("disciplina") or ""))
            bl_item = item.get("bloco_inicial")
            modo_item = str(item.get("modo_inicial") or modo_inicial).strip().lower()
            st_item = str(item.get("status_curso") or status_curso).strip().upper()
            bloco_eff = _validar_bloco_disciplina(
                did,
                str(bl_item or bloco_inicial),
                fallback_a01=(bl_item is None or str(bl_item).strip() == ""),
            )
        else:
            did = config.normalizar_disciplina_id(str(item))
            modo_item = modo_inicial
            st_item = status_curso
            bloco_eff = _validar_bloco_disciplina(did, bloco_inicial, fallback_a01=True)
        if did in vistos:
            continue
        vistos.add(did)
        specs.append(
            {
                "disciplina": did,
                "bloco_inicial": bloco_eff,
                "modo_inicial": modo_item,
                "status_curso": st_item,
            }
        )
    if int(concluir_anteriores_ate or 0) > 0:
        marcar_periodos_anteriores_concluidos(
            aluno_id,
            int(concluir_anteriores_ate),
            excluir_disciplinas=[s["disciplina"] for s in specs],
        )
    resultados: List[Dict[str, Any]] = []
    for sp in specs:
        existente = obter_matricula(aluno_id, disciplina=sp["disciplina"])
        mat = matricular_aluno(
            aluno_id,
            disciplina=sp["disciplina"],
            bloco_inicial=sp["bloco_inicial"],
            modo_inicial=sp["modo_inicial"],
            status_curso=sp["status_curso"],
            atualizar_existente=atualizar_existente,
        )
        out_m = dict(mat)
        out_m["recem_criada"] = existente is None
        resultados.append(out_m)
    return resultados


def _mesclar_aluno_matricula(aluno_row: Dict[str, Any], mat_row: Optional[Dict[str, Any]], incluir_pin: bool) -> Dict[str, Any]:
    out = _sanitizar_aluno(aluno_row, incluir_pin=incluir_pin)
    if mat_row:
        out["disciplina"] = mat_row["disciplina"]
        out["bloco_atual"] = mat_row["bloco_atual"]
        out["variante_atual"] = mat_row["variante_atual"]
        out["tentativa_bloco"] = mat_row["tentativa_bloco"]
        out["modo_atual"] = mat_row["modo_atual"]
        out["status_curso"] = mat_row["status_curso"]
    else:
        out.setdefault("disciplina", config.DISCIPLINA_PADRAO)
    return out


def obter_ou_criar_aluno(
    nome: str,
    email: str,
    bloco_inicial: str = "A01",
    modo_inicial: str = "pratica",
    senha_inicial: str = "",
    disciplina: str = config.DISCIPLINA_PADRAO,
    status_curso: str = "EM_ANDAMENTO",
    atualizar_existente: bool = False,
) -> Dict[str, Any]:
    inicializar_banco()
    disc_id = config.normalizar_disciplina_id(disciplina)
    email_norm = email.strip().lower()
    bloco_norm = _validar_bloco_disciplina(disc_id, bloco_inicial, fallback_a01=False)
    modo_norm = modo_inicial if modo_inicial in ("pratica", "checagem") else "pratica"
    status_norm = status_curso if status_curso in ("EM_ANDAMENTO", "CONCLUIDO") else "EM_ANDAMENTO"
    with conectar() as conn:
        row = conn.execute(
            "SELECT * FROM alunos WHERE email = ?", (email_norm,)
        ).fetchone()
        if row:
            aid = int(row["id"])
            al_dict = dict(row)
        else:
            pin = senha_inicial.strip() or gerar_pin_acesso()
            cur = conn.execute(
                """
                INSERT INTO alunos (nome, email, bloco_atual, variante_atual, tentativa_bloco, modo_atual, status_curso, criado_em, senha_hash, pin_inicial)
                VALUES (?, ?, ?, 'V1', 1, ?, ?, ?, ?, ?)
                """,
                (
                    nome.strip(),
                    email_norm,
                    bloco_norm,
                    modo_norm,
                    status_norm,
                    _agora_iso(),
                    hash_senha(pin),
                    pin,
                ),
            )
            conn.commit()
            aid = int(cur.lastrowid)
            al_dict = dict(conn.execute("SELECT * FROM alunos WHERE id = ?", (aid,)).fetchone())

    mat = matricular_aluno(
        aid,
        disciplina=disc_id,
        bloco_inicial=bloco_norm,
        modo_inicial=modo_norm,
        status_curso=status_norm,
        atualizar_existente=atualizar_existente,
    )
    return _mesclar_aluno_matricula(al_dict, mat, incluir_pin=True)


def obter_aluno_por_id(
    aluno_id: int,
    incluir_pin: bool = False,
    disciplina: Optional[str] = None,
) -> Optional[Dict[str, Any]]:
    inicializar_banco()
    with conectar() as conn:
        row = conn.execute("SELECT * FROM alunos WHERE id = ?", (aluno_id,)).fetchone()
        if not row:
            return None
        al_dict = dict(row)
    if disciplina:
        mat = obter_matricula(aluno_id, disciplina=disciplina)
        return _mesclar_aluno_matricula(al_dict, mat, incluir_pin=incluir_pin)
    return _sanitizar_aluno(al_dict, incluir_pin=incluir_pin)


def autenticar_aluno(email: str, senha: str) -> Optional[Dict[str, Any]]:
    """Autentica um aluno por e-mail e PIN/senha."""
    inicializar_banco()
    email_norm = (email or "").strip().lower()
    senha_norm = (senha or "").strip()
    if not email_norm or not senha_norm:
        return None
    with conectar() as conn:
        row = conn.execute("SELECT * FROM alunos WHERE email = ?", (email_norm,)).fetchone()
        if not row:
            return None
        if not verificar_senha(senha_norm, row["senha_hash"] or ""):
            return None
        return _sanitizar_aluno(dict(row), incluir_pin=False)


def redefinir_pin_aluno(aluno_id: int, nova_senha: str = "") -> Optional[Dict[str, Any]]:
    """Gera um novo PIN de acesso de 6 digitos (ou aplica senha informada) para o aluno."""
    inicializar_banco()
    novo_pin = (nova_senha or "").strip() or gerar_pin_acesso()
    with conectar() as conn:
        conn.execute(
            "UPDATE alunos SET senha_hash = ?, pin_inicial = ? WHERE id = ?",
            (hash_senha(novo_pin), novo_pin, aluno_id),
        )
        conn.commit()
        row = conn.execute("SELECT * FROM alunos WHERE id = ?", (aluno_id,)).fetchone()
        return _sanitizar_aluno(dict(row), incluir_pin=True) if row else None


def excluir_aluno(aluno_id: int) -> Optional[Dict[str, Any]]:
    """Exclui permanentemente um aluno e todos os seus registros vinculados em transacao unica."""
    inicializar_banco()
    with conectar() as conn:
        row = conn.execute("SELECT * FROM alunos WHERE id = ?", (aluno_id,)).fetchone()
        if not row:
            return None
        sub_ids = [
            int(r["id"])
            for r in conn.execute(
                "SELECT id FROM submissoes WHERE aluno_id = ?", (aluno_id,)
            ).fetchall()
        ]
        itens_rem = 0
        if sub_ids:
            ph = ",".join("?" for _ in sub_ids)
            cur_it = conn.execute(
                f"DELETE FROM itens_submissao WHERE submissao_id IN ({ph})", sub_ids
            )
            itens_rem = cur_it.rowcount
        sub_rem = conn.execute("DELETE FROM submissoes WHERE aluno_id = ?", (aluno_id,)).rowcount
        prov_rem = conn.execute(
            "DELETE FROM provas_emitidas WHERE aluno_id = ?", (aluno_id,)
        ).rowcount
        mat_rem = conn.execute("DELETE FROM matriculas WHERE aluno_id = ?", (aluno_id,)).rowcount
        conn.execute("DELETE FROM componentes_integralizacao WHERE aluno_id = ?", (aluno_id,))
        conn.execute("DELETE FROM alunos WHERE id = ?", (aluno_id,))
        conn.commit()
        return {
            "id": int(row["id"]),
            "nome": row["nome"],
            "email": row["email"],
            "removidos": {
                "matriculas": mat_rem,
                "provas_emitidas": prov_rem,
                "submissoes": sub_rem,
                "itens_submissao": itens_rem,
            },
        }


def listar_alunos(incluir_pin: bool = False, disciplina: Optional[str] = None) -> List[Dict[str, Any]]:
    inicializar_banco()
    with conectar() as conn:
        if not disciplina:
            rows = conn.execute("SELECT * FROM alunos ORDER BY id ASC").fetchall()
            out = []
            for r in rows:
                d = _sanitizar_aluno(dict(r), incluir_pin=incluir_pin)
                mats = conn.execute(
                    "SELECT disciplina, bloco_atual, variante_atual, modo_atual FROM matriculas WHERE aluno_id = ? ORDER BY id ASC",
                    (r["id"],),
                ).fetchall()
                d["disciplinas_matriculadas"] = [m["disciplina"] for m in mats]
                out.append(d)
            return out

        disc_id = config.normalizar_disciplina_id(disciplina)
        rows = conn.execute(
            """
            SELECT a.*, m.disciplina AS mat_disc, m.bloco_atual AS mat_bloco,
                   m.variante_atual AS mat_var, m.tentativa_bloco AS mat_tent,
                   m.modo_atual AS mat_modo, m.status_curso AS mat_status
            FROM alunos a
            INNER JOIN matriculas m ON m.aluno_id = a.id AND m.disciplina = ?
            ORDER BY a.id ASC
            """,
            (disc_id,),
        ).fetchall()
        out = []
        for r in rows:
            rd = dict(r)
            mat = {
                "disciplina": rd.pop("mat_disc"),
                "bloco_atual": rd.pop("mat_bloco"),
                "variante_atual": rd.pop("mat_var"),
                "tentativa_bloco": rd.pop("mat_tent"),
                "modo_atual": rd.pop("mat_modo"),
                "status_curso": rd.pop("mat_status"),
            }
            out.append(_mesclar_aluno_matricula(rd, mat, incluir_pin=incluir_pin))
        return out


def email_ja_processado(msg_chave: str) -> bool:
    if not msg_chave:
        return False
    inicializar_banco()
    with conectar() as conn:
        row = conn.execute(
            "SELECT 1 FROM emails_processados WHERE msg_chave = ?",
            (msg_chave.strip(),),
        ).fetchone()
        return row is not None


def registrar_email_processado(
    msg_chave: str,
    protocolo: str,
    remetente: str,
    assunto: str,
    status: str,
    detalhes: str = "",
) -> None:
    if not msg_chave:
        return
    inicializar_banco()
    with conectar() as conn:
        conn.execute(
            """
            INSERT OR REPLACE INTO emails_processados
            (msg_chave, protocolo, remetente, assunto, status, detalhes, processado_em)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                msg_chave.strip(),
                (protocolo or "").strip(),
                (remetente or "").strip()[:240],
                (assunto or "").strip()[:300],
                (status or "processado").strip(),
                (detalhes or "").strip()[:500],
                _agora_iso(),
            ),
        )
        conn.commit()


def obter_prova_pendente_por_aluno_id(
    aluno_id: int,
    disciplina: Optional[str] = None,
) -> Optional[Dict[str, Any]]:
    inicializar_banco()
    with conectar() as conn:
        if disciplina:
            disc_id = config.normalizar_disciplina_id(disciplina)
            row = conn.execute(
                """
                SELECT * FROM provas_emitidas
                WHERE aluno_id = ? AND COALESCE(disciplina, 'algoritmos') = ?
                  AND status IN ('emitida', 'em_execucao')
                ORDER BY enviado_em DESC
                LIMIT 1
                """,
                (aluno_id, disc_id),
            ).fetchone()
        else:
            row = conn.execute(
                """
                SELECT * FROM provas_emitidas
                WHERE aluno_id = ? AND status IN ('emitida', 'em_execucao')
                ORDER BY enviado_em DESC
                LIMIT 1
                """,
                (aluno_id,),
            ).fetchone()
        return dict(row) if row else None


def obter_prova_pendente_por_email(
    email_remetente: str,
    disciplina: Optional[str] = None,
) -> Optional[Dict[str, Any]]:
    email_norm = (email_remetente or "").strip().lower()
    if not email_norm:
        return None
    inicializar_banco()
    with conectar() as conn:
        row_al = conn.execute(
            "SELECT id FROM alunos WHERE email = ?", (email_norm,)
        ).fetchone()
        if not row_al:
            return None
        return obter_prova_pendente_por_aluno_id(int(row_al["id"]), disciplina=disciplina)


def atualizar_estado_matricula(
    aluno_id: int,
    disciplina: str,
    bloco_atual: str,
    variante_atual: str,
    tentativa_bloco: int,
    modo_atual: str,
    status_curso: str = "EM_ANDAMENTO",
) -> Dict[str, Any]:
    inicializar_banco()
    disc_id = config.normalizar_disciplina_id(disciplina)
    matricular_aluno(aluno_id, disciplina=disc_id, bloco_inicial=bloco_atual, modo_inicial=modo_atual)
    with conectar() as conn:
        conn.execute(
            """
            UPDATE matriculas
            SET bloco_atual = ?, variante_atual = ?, tentativa_bloco = ?, modo_atual = ?, status_curso = ?
            WHERE aluno_id = ? AND disciplina = ?
            """,
            (bloco_atual, variante_atual, tentativa_bloco, modo_atual, status_curso, aluno_id, disc_id),
        )
        if disc_id == "algoritmos":
            conn.execute(
                """
                UPDATE alunos
                SET bloco_atual = ?, variante_atual = ?, tentativa_bloco = ?, modo_atual = ?, status_curso = ?
                WHERE id = ?
                """,
                (bloco_atual, variante_atual, tentativa_bloco, modo_atual, status_curso, aluno_id),
            )
        conn.commit()
        row = conn.execute(
            "SELECT * FROM matriculas WHERE aluno_id = ? AND disciplina = ?",
            (aluno_id, disc_id),
        ).fetchone()
        return dict(row)


def atualizar_fase_aluno(
    aluno_id: int,
    disciplina: str,
    bloco_atual: str,
    modo_atual: str = "pratica",
    variante_atual: str = "V1",
    tentativa_bloco: int = 1,
    status_curso: str = "EM_ANDAMENTO",
) -> Dict[str, Any]:
    """Posiciona ou atualiza a fase/bloco atual de um aluno em determinada disciplina."""
    inicializar_banco()
    disc_id = config.normalizar_disciplina_id(disciplina)
    bloco_norm = _validar_bloco_disciplina(disc_id, bloco_atual, fallback_a01=False)
    modo_norm = modo_atual if modo_atual in ("pratica", "checagem") else "pratica"
    var_norm = variante_atual if variante_atual in ("V1", "V2") else "V1"
    tent_norm = max(1, int(tentativa_bloco or 1))
    status_norm = status_curso if status_curso in ("EM_ANDAMENTO", "CONCLUIDO") else "EM_ANDAMENTO"
    return atualizar_estado_matricula(
        aluno_id=int(aluno_id),
        disciplina=disc_id,
        bloco_atual=bloco_norm,
        variante_atual=var_norm,
        tentativa_bloco=tent_norm,
        modo_atual=modo_norm,
        status_curso=status_norm,
    )


def atualizar_estado_aluno(
    aluno_id: int,
    bloco_atual: str,
    variante_atual: str,
    tentativa_bloco: int,
    modo_atual: str,
    status_curso: str = "EM_ANDAMENTO",
    disciplina: str = config.DISCIPLINA_PADRAO,
) -> Dict[str, Any]:
    mat = atualizar_estado_matricula(
        aluno_id=aluno_id,
        disciplina=disciplina,
        bloco_atual=bloco_atual,
        variante_atual=variante_atual,
        tentativa_bloco=tentativa_bloco,
        modo_atual=modo_atual,
        status_curso=status_curso,
    )
    al = obter_aluno_por_id(aluno_id, incluir_pin=False, disciplina=disciplina)
    return al or mat


def registrar_prova_emitida(
    protocolo: str,
    aluno_id: int,
    bloco: str,
    variante: str,
    tentativa: int,
    modo: str,
    tempo_alvo_min: int,
    caminho_folha_html: str,
    caminho_email_eml: str = "",
    disciplina: str = "",
) -> Dict[str, Any]:
    inicializar_banco()
    disc_id = config.normalizar_disciplina_id(
        disciplina or config.disciplina_por_protocolo(protocolo)
    )
    now = _agora_iso()
    with conectar() as conn:
        conn.execute(
            """
            INSERT OR REPLACE INTO provas_emitidas
            (protocolo, aluno_id, disciplina, bloco, variante, tentativa, modo, tempo_alvo_min, caminho_folha_html, caminho_email_eml, enviado_em, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'emitida')
            """,
            (
                protocolo,
                aluno_id,
                disc_id,
                bloco,
                variante,
                tentativa,
                modo,
                tempo_alvo_min,
                caminho_folha_html,
                caminho_email_eml,
                now,
            ),
        )
        conn.commit()
        row = conn.execute(
            "SELECT * FROM provas_emitidas WHERE protocolo = ?", (protocolo,)
        ).fetchone()
        return dict(row)


def obter_prova(protocolo: str) -> Optional[Dict[str, Any]]:
    inicializar_banco()
    with conectar() as conn:
        if protocolo:
            row = conn.execute(
                "SELECT * FROM provas_emitidas WHERE protocolo = ?", (protocolo,)
            ).fetchone()
            if row:
                return dict(row)
            parsed_p = config.parse_protocolo(protocolo)
            if parsed_p:
                row = conn.execute(
                    """
                    SELECT * FROM provas_emitidas
                    WHERE bloco = ? AND variante = ? AND tentativa = ?
                      AND COALESCE(disciplina, 'algoritmos') = ?
                    ORDER BY enviado_em DESC LIMIT 1
                    """,
                    (parsed_p["bloco"], parsed_p["variante"], parsed_p["tentativa"], parsed_p["disciplina"]),
                ).fetchone()
                if row:
                    return dict(row)
            return None
        row = conn.execute(
            "SELECT * FROM provas_emitidas ORDER BY enviado_em DESC LIMIT 1"
        ).fetchone()
        return dict(row) if row else None


def iniciar_cronometro_prova(protocolo: str) -> Optional[Dict[str, Any]]:
    inicializar_banco()
    prova = obter_prova(protocolo)
    if not prova:
        return None
    prot_real = prova["protocolo"]
    now = _agora_iso()
    with conectar() as conn:
        conn.execute(
            """
            UPDATE provas_emitidas
            SET inicio_cronometro_em = ?, fim_cronometro_em = '', tempo_cronometrado_min = 0, status = 'em_execucao'
            WHERE protocolo = ?
            """,
            (now, prot_real),
        )
        conn.commit()
        return obter_prova(prot_real)


def encerrar_cronometro_prova(
    protocolo: str, tempo_decorrido_seg: Optional[float] = None
) -> Optional[Dict[str, Any]]:
    inicializar_banco()
    prova = obter_prova(protocolo)
    if not prova:
        return None
    prot_real = prova["protocolo"]
    now_dt = datetime.datetime.now()
    now_str = now_dt.strftime("%Y-%m-%d %H:%M:%S")
    duracao_min = 0.0
    if tempo_decorrido_seg is not None and tempo_decorrido_seg > 0:
        duracao_min = round(max(1.0, float(tempo_decorrido_seg) / 60.0), 1)
    elif prova.get("inicio_cronometro_em"):
        try:
            ini_dt = datetime.datetime.strptime(prova["inicio_cronometro_em"], "%Y-%m-%d %H:%M:%S")
            duracao_min = round(max(1.0, (now_dt - ini_dt).total_seconds() / 60.0), 1)
        except Exception:
            duracao_min = float(prova.get("tempo_alvo_min", 20))
    else:
        duracao_min = float(prova.get("tempo_alvo_min", 20))

    with conectar() as conn:
        conn.execute(
            """
            UPDATE provas_emitidas
            SET fim_cronometro_em = ?, tempo_cronometrado_min = ?, status = 'tempo_encerrado'
            WHERE protocolo = ?
            """,
            (now_str, duracao_min, prot_real),
        )
        conn.commit()
        return obter_prova(prot_real)


def atualizar_status_prova(protocolo: str, status: str) -> None:
    with conectar() as conn:
        conn.execute(
            "UPDATE provas_emitidas SET status = ? WHERE protocolo = ?",
            (status, protocolo),
        )
        conn.commit()


def registrar_submissao(dados: Dict[str, Any], itens: List[Dict[str, Any]]) -> int:
    inicializar_banco()
    disc_id = config.normalizar_disciplina_id(
        dados.get("disciplina") or config.disciplina_por_protocolo(dados["protocolo"])
    )
    with conectar() as conn:
        cur = conn.execute(
            """
            INSERT INTO submissoes (
                protocolo, aluno_id, disciplina, bloco, variante, tentativa, modo, recebido_em,
                caminho_imagem, tempo_declarado_min, tempo_janela_min, fluencia_tempo,
                acertos_iniciais, total_questoes, acertos_apos_correcao, percentual_acerto,
                resultado_checagem, dificuldade_observada, proxima_acao, bloco_destino,
                relatorio_feedback_html, caminho_email_feedback, camada_predominante
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                dados["protocolo"],
                dados["aluno_id"],
                disc_id,
                dados["bloco"],
                dados["variante"],
                dados["tentativa"],
                dados["modo"],
                dados.get("recebido_em", _agora_iso()),
                dados.get("caminho_imagem", ""),
                dados.get("tempo_declarado_min", 0),
                dados.get("tempo_janela_min", 0),
                dados.get("fluencia_tempo", "dentro_meta"),
                dados["acertos_iniciais"],
                dados["total_questoes"],
                dados["acertos_apos_correcao"],
                dados["percentual_acerto"],
                dados["resultado_checagem"],
                dados["dificuldade_observada"],
                dados["proxima_acao"],
                dados["bloco_destino"],
                dados["relatorio_feedback_html"],
                dados.get("caminho_email_feedback", ""),
                dados.get("camada_predominante", "local"),
            ),
        )
        sub_id = cur.lastrowid
        for it in itens:
            conn.execute(
                """
                INSERT INTO itens_submissao (
                    submissao_id, questao_id, tipo_questao, resposta_extraida,
                    status_correcao, categoria_erro, feedback_item, camada_avaliacao, confianca
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    sub_id,
                    it["questao_id"],
                    it["tipo_questao"],
                    it["resposta_extraida"],
                    it["status_correcao"],
                    it.get("categoria_erro", ""),
                    it["feedback_item"],
                    it.get("camada_avaliacao", "local"),
                    it.get("confianca", 1.0),
                ),
            )
        conn.commit()
        return int(sub_id)


def registrar_metrica_jev(camada: str, modulo: str, confianca: float, detalhes: str = "") -> None:
    inicializar_banco()
    with conectar() as conn:
        conn.execute(
            """
            INSERT INTO metricas_jev (timestamp, camada, modulo, confianca, detalhes)
            VALUES (?, ?, ?, ?, ?)
            """,
            (_agora_iso(), camada, modulo, confianca, detalhes),
        )
        conn.commit()


def registrar_linha_csv(
    aluno_nome: str,
    bloco: str,
    variante: str,
    tentativa: int,
    tempo_resolucao_min: float,
    acertos_iniciais: int,
    total_questoes: int,
    acertos_apos_correcao: int,
    resultado_checagem: str,
    dificuldade_observada: str,
    proxima_acao: str,
    csv_path: Optional[str] = None,
    disciplina: str = config.DISCIPLINA_PADRAO,
) -> None:
    disc = config.obter_disciplina(disciplina)
    alvo = csv_path or disc["csv_path"]
    os.makedirs(os.path.dirname(os.path.abspath(alvo)), exist_ok=True)
    existe = os.path.isfile(alvo) and os.path.getsize(alvo) > 0
    precisa_nl = False
    if existe:
        with open(alvo, "rb") as fb:
            fb.seek(-1, os.SEEK_END)
            ultimo = fb.read(1)
            if ultimo not in (b"\n", b"\r"):
                precisa_nl = True

    with open(alvo, "a", encoding="utf-8", newline="") as f:
        if precisa_nl:
            f.write("\n")
        writer = csv.writer(f)
        if not existe:
            writer.writerow(CSV_COLUNAS)
        writer.writerow(
            [
                _hoje_br(),
                aluno_nome,
                bloco,
                variante,
                tentativa,
                int(round(tempo_resolucao_min)),
                acertos_iniciais,
                total_questoes,
                acertos_apos_correcao,
                resultado_checagem,
                dificuldade_observada,
                proxima_acao,
            ]
        )


def ler_acompanhamento_csv(
    csv_path: Optional[str] = None,
    disciplina: str = config.DISCIPLINA_PADRAO,
) -> List[Dict[str, str]]:
    disc = config.obter_disciplina(disciplina)
    alvo = csv_path or disc["csv_path"]
    if not os.path.isfile(alvo):
        return []
    with open(alvo, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        return [dict(r) for r in reader]


def obter_metricas_jev_resumo() -> Dict[str, Any]:
    inicializar_banco()
    with conectar() as conn:
        rows = conn.execute(
            "SELECT camada, COUNT(*) as qtd, AVG(confianca) as media_conf FROM metricas_jev GROUP BY camada"
        ).fetchall()
    cont = {"local": 0, "jev": 0, "escalate": 0}
    conf_sum = 0.0
    total = 0
    for r in rows:
        c = r["camada"]
        q = int(r["qtd"])
        if c in cont:
            cont[c] = q
        total += q
        conf_sum += float(r["media_conf"] or 0.0) * q

    light = cont["local"] + cont["jev"]
    light_share = round((light / total) * 100.0, 1) if total > 0 else 100.0
    return {
        "total_decisoes": total,
        "local": cont["local"],
        "jev": cont["jev"],
        "escalate": cont["escalate"],
        "light_share_pct": light_share,
        "confianca_media": round(conf_sum / total, 3) if total > 0 else 1.0,
    }


def obter_resumo_turma(disciplina: str = config.DISCIPLINA_PADRAO) -> List[Dict[str, Any]]:
    """Retorna visao consolidada dos alunos matriculados na disciplina para a tabela gerencial."""
    inicializar_banco()
    disc_id = config.normalizar_disciplina_id(disciplina)
    alunos = listar_alunos(incluir_pin=True, disciplina=disc_id)
    with conectar() as conn:
        resumo = []
        for al in alunos:
            aid = al["id"]
            subs = conn.execute(
                """
                SELECT bloco, percentual_acerto, resultado_checagem, recebido_em
                FROM submissoes
                WHERE aluno_id = ? AND COALESCE(disciplina, 'algoritmos') = ?
                ORDER BY id DESC
                """,
                (aid, disc_id),
            ).fetchall()
            ultima_prova = conn.execute(
                """
                SELECT protocolo, modo, status, enviado_em
                FROM provas_emitidas
                WHERE aluno_id = ? AND COALESCE(disciplina, 'algoritmos') = ?
                ORDER BY enviado_em DESC LIMIT 1
                """,
                (aid, disc_id),
            ).fetchone()
            aprovados = {
                s["bloco"]
                for s in subs
                if str(s["resultado_checagem"] or "").startswith("APROVADO")
            }
            resumo.append(
                {
                    "id": aid,
                    "disciplina": disc_id,
                    "nome": al["nome"],
                    "email": al["email"],
                    "bloco_atual": al["bloco_atual"],
                    "variante_atual": al["variante_atual"],
                    "tentativa_bloco": al["tentativa_bloco"],
                    "modo_atual": al["modo_atual"],
                    "status_curso": al["status_curso"],
                    "pin_inicial": al.get("pin_inicial", ""),
                    "total_submissoes": len(subs),
                    "blocos_dominados": len(aprovados),
                    "ultimo_acerto_pct": subs[0]["percentual_acerto"] if subs else None,
                    "ultima_atividade": subs[0]["recebido_em"] if subs else (ultima_prova["enviado_em"] if ultima_prova else al["criado_em"]),
                    "ultimo_protocolo": ultima_prova["protocolo"] if ultima_prova else "",
                    "ultimo_status_prova": ultima_prova["status"] if ultima_prova else "",
                }
            )
        return resumo


def obter_integralizacao_aluno(aluno_id: Optional[int]) -> List[Dict[str, Any]]:
    inicializar_banco()
    salvos: Dict[str, Dict[str, Any]] = {}
    if aluno_id is not None:
        with conectar() as conn:
            for r in conn.execute(
                "SELECT componente_key, horas_cumpridas, observacoes, atualizado_em FROM componentes_integralizacao WHERE aluno_id = ?",
                (int(aluno_id),),
            ).fetchall():
                salvos[str(r["componente_key"])] = dict(r)
    out: List[Dict[str, Any]] = []
    for comp in config.COMPONENTES_INTEGRALIZACAO:
        key = str(comp["key"])
        exig = float(comp.get("horas_exigidas", 0))
        reg = salvos.get(key) or {}
        cump = float(reg.get("horas_cumpridas") or 0.0)
        pct = min(100.0, round((cump / exig) * 100.0, 1)) if exig > 0 else 100.0
        out.append(
            {
                "key": key,
                "nome": comp.get("nome", key),
                "horas_exigidas": exig,
                "horas_cumpridas": round(cump, 1),
                "percentual": pct,
                "concluido": cump >= exig and exig > 0,
                "descricao": comp.get("descricao", ""),
                "observacoes": str(reg.get("observacoes") or ""),
                "atualizado_em": str(reg.get("atualizado_em") or ""),
            }
        )
    return out


def atualizar_integralizacao_aluno(
    aluno_id: int,
    componente_key: str,
    horas_cumpridas: float,
    observacoes: str = "",
) -> List[Dict[str, Any]]:
    inicializar_banco()
    key = str(componente_key or "").strip()
    if key not in config.COMPONENTES_INTEGRALIZACAO_MAP:
        raise ValueError(f"Componente de integralizacao desconhecido: '{componente_key}'")
    horas = max(0.0, float(horas_cumpridas))
    with conectar() as conn:
        row_al = conn.execute("SELECT id FROM alunos WHERE id = ?", (int(aluno_id),)).fetchone()
        if not row_al:
            raise ValueError(f"Aluno ID {aluno_id} nao encontrado.")
        conn.execute(
            """
            INSERT OR REPLACE INTO componentes_integralizacao
            (aluno_id, componente_key, horas_cumpridas, observacoes, atualizado_em)
            VALUES (?, ?, ?, ?, ?)
            """,
            (int(aluno_id), key, horas, str(observacoes or "").strip()[:400], _agora_iso()),
        )
        conn.commit()
    return obter_integralizacao_aluno(int(aluno_id))


def obter_resumo_curriculo_aluno(aluno_id: Optional[int]) -> Dict[str, Any]:
    inicializar_banco()
    estrutura = config.obter_estrutura_bcc()
    mats_map: Dict[str, Dict[str, Any]] = {}
    aprov_por_disc: Dict[str, set] = {}
    if aluno_id is not None:
        with conectar() as conn:
            for r in conn.execute(
                "SELECT * FROM matriculas WHERE aluno_id = ?",
                (int(aluno_id),),
            ).fetchall():
                mats_map[str(r["disciplina"])] = dict(r)
            for s in conn.execute(
                """
                SELECT COALESCE(disciplina, 'algoritmos') AS disc, bloco
                FROM submissoes
                WHERE aluno_id = ? AND resultado_checagem LIKE 'APROVADO%'
                """,
                (int(aluno_id),),
            ).fetchall():
                aprov_por_disc.setdefault(str(s["disc"]), set()).add(str(s["bloco"]))

    status_por_disc: Dict[str, str] = {}
    for did in config.DISCIPLINAS_ORDEM:
        m = mats_map.get(did)
        if not m:
            status_por_disc[did] = "nao_matriculada"
        elif m.get("status_curso") == "CONCLUIDO":
            status_por_disc[did] = "concluida"
        else:
            status_por_disc[did] = "em_andamento"

    periodos_out: List[Dict[str, Any]] = []
    concluidas_total = 0
    matriculadas_total = 0
    for per in estrutura["periodos"]:
        discs_p: List[Dict[str, Any]] = []
        concl_p = 0
        mat_p = 0
        for d in per["disciplinas"]:
            did = d["id"]
            st = status_por_disc[did]
            m = mats_map.get(did)
            aprov_qtd = len(aprov_por_disc.get(did, set()))
            tot_b = int(d["total_blocos"])
            prereq_pend = [
                {
                    "id": pid,
                    "nome": config.obter_disciplina(pid)["nome"] if pid in config.DISCIPLINAS else pid,
                    "status": status_por_disc.get(pid, "nao_matriculada"),
                }
                for pid in (d.get("pre_requisitos") or [])
                if status_por_disc.get(pid) != "concluida"
            ]
            if st == "concluida":
                concl_p += 1
                concluidas_total += 1
            if st != "nao_matriculada":
                mat_p += 1
                matriculadas_total += 1
            discs_p.append(
                {
                    **d,
                    "status_aluno": st,
                    "matriculada": st != "nao_matriculada",
                    "bloco_atual": m["bloco_atual"] if m else "A01",
                    "modo_atual": m["modo_atual"] if m else "pratica",
                    "blocos_dominados": aprov_qtd,
                    "percentual": round((aprov_qtd / float(tot_b)) * 100.0, 1) if tot_b else 0.0,
                    "prerequisitos_pendentes": prereq_pend,
                }
            )
        periodos_out.append(
            {
                "periodo": per["periodo"],
                "titulo": per["titulo"],
                "matriculadas": mat_p,
                "concluidas": concl_p,
                "total": len(discs_p),
                "disciplinas": discs_p,
            }
        )

    return {
        "curso": estrutura["curso"],
        "instituicao": estrutura["instituicao"],
        "matriz": estrutura["matriz"],
        "ppc_ano": estrutura["ppc_ano"],
        "fontes_curriculares": estrutura["fontes_curriculares"],
        "roteiro_apoio_por_area": estrutura["roteiro_apoio_por_area"],
        "total_disciplinas": estrutura["total_disciplinas"],
        "total_blocos_geral": estrutura["total_blocos_geral"],
        "disciplinas_matriculadas_qtd": matriculadas_total,
        "disciplinas_concluidas_qtd": concluidas_total,
        "periodos": periodos_out,
        "integralizacao": obter_integralizacao_aluno(aluno_id),
    }


def obter_estado_portal_aluno(
    aluno_id: int,
    mapa_blocos: Optional[List[Dict[str, Any]]] = None,
    disciplina: Optional[str] = None,
) -> Optional[Dict[str, Any]]:
    """Retorna payload estritamente enxuto e isolado para o Portal do Aluno."""
    inicializar_banco()
    with conectar() as conn:
        row_al = conn.execute("SELECT * FROM alunos WHERE id = ?", (aluno_id,)).fetchone()
        if not row_al:
            return None
        mats_raw = conn.execute(
            "SELECT * FROM matriculas WHERE aluno_id = ? ORDER BY id ASC",
            (aluno_id,),
        ).fetchall()
        mats = [dict(m) for m in mats_raw]

        if disciplina:
            disc_id = config.normalizar_disciplina_id(disciplina)
            mat_ativa = next((m for m in mats if m["disciplina"] == disc_id), None)
            if not mat_ativa and mats:
                ativas = [m for m in mats if m.get("status_curso") != "CONCLUIDO"]
                mat_ativa = ativas[0] if ativas else mats[0]
                disc_id = mat_ativa["disciplina"]
        else:
            ativas = [m for m in mats if m.get("status_curso") != "CONCLUIDO"]
            mat_ativa = ativas[0] if ativas else (mats[0] if mats else None)
            disc_id = mat_ativa["disciplina"] if mat_ativa else config.DISCIPLINA_PADRAO

        disc_meta = config.obter_disciplina(disc_id)
        aluno = _mesclar_aluno_matricula(dict(row_al), mat_ativa, incluir_pin=False)

        provas_raw = conn.execute(
            """
            SELECT * FROM provas_emitidas
            WHERE aluno_id = ? AND COALESCE(disciplina, 'algoritmos') = ?
            ORDER BY enviado_em DESC
            """,
            (aluno_id, disc_id),
        ).fetchall()
        subs_raw = conn.execute(
            """
            SELECT * FROM submissoes
            WHERE aluno_id = ? AND COALESCE(disciplina, 'algoritmos') = ?
            ORDER BY id DESC
            """,
            (aluno_id, disc_id),
        ).fetchall()

        ultima_sub = None
        if subs_raw:
            s0 = dict(subs_raw[0])
            itens_rows = conn.execute(
                """
                SELECT questao_id, tipo_questao, resposta_extraida, status_correcao, categoria_erro, feedback_item
                FROM itens_submissao
                WHERE submissao_id = ?
                ORDER BY id ASC
                """,
                (s0["id"],),
            ).fetchall()
            ultima_sub = {
                "id": s0["id"],
                "protocolo": s0["protocolo"],
                "disciplina": disc_id,
                "bloco": s0["bloco"],
                "variante": s0["variante"],
                "tentativa": s0["tentativa"],
                "modo": s0["modo"],
                "recebido_em": s0["recebido_em"],
                "tempo_declarado_min": s0["tempo_declarado_min"],
                "fluencia_tempo": s0["fluencia_tempo"],
                "acertos_iniciais": s0["acertos_iniciais"],
                "total_questoes": s0["total_questoes"],
                "percentual_acerto": s0["percentual_acerto"],
                "resultado_checagem": s0["resultado_checagem"],
                "dificuldade_observada": s0["dificuldade_observada"],
                "proxima_acao": s0["proxima_acao"],
                "bloco_destino": s0["bloco_destino"],
                "itens": [dict(ir) for ir in itens_rows],
            }

    provas = [
        {
            "protocolo": p["protocolo"],
            "disciplina": p["disciplina"] or disc_id,
            "bloco": p["bloco"],
            "variante": p["variante"],
            "tentativa": p["tentativa"],
            "modo": p["modo"],
            "tempo_alvo_min": p["tempo_alvo_min"],
            "enviado_em": p["enviado_em"],
            "inicio_cronometro_em": p["inicio_cronometro_em"],
            "fim_cronometro_em": p["fim_cronometro_em"],
            "tempo_cronometrado_min": p["tempo_cronometrado_min"],
            "status": p["status"],
        }
        for p in provas_raw
    ]

    blocos_aprovados = sorted(
        list(
            {
                s["bloco"]
                for s in subs_raw
                if str(s["resultado_checagem"] or "").startswith("APROVADO")
            }
        )
    )
    aprov_set = set(blocos_aprovados)
    tempos = [float(s["tempo_declarado_min"]) for s in subs_raw if (s["tempo_declarado_min"] or 0) > 0]
    notas = [float(s["percentual_acerto"]) for s in subs_raw]

    historico_evolucao = [
        {
            "data": str(s["recebido_em"])[:10],
            "protocolo": s["protocolo"],
            "bloco": s["bloco"],
            "variante": s["variante"],
            "tentativa": s["tentativa"],
            "modo": s["modo"],
            "acertos_iniciais": s["acertos_iniciais"],
            "total_questoes": s["total_questoes"],
            "percentual_acerto": s["percentual_acerto"],
            "tempo_declarado_min": s["tempo_declarado_min"],
            "fluencia_tempo": s["fluencia_tempo"],
            "aprovado": str(s["resultado_checagem"] or "").startswith("APROVADO"),
            "proxima_acao": s["proxima_acao"],
        }
        for s in reversed(subs_raw)
    ]

    total_blocos = len(mapa_blocos) if mapa_blocos else int(disc_meta["total_blocos"])
    titulo_bloco_atual = f"Bloco {aluno['bloco_atual']}"
    micro_atual = ""
    estagios_resumo = []
    if mapa_blocos:
        por_est: Dict[str, List[Dict[str, Any]]] = {}
        for b in mapa_blocos:
            est = b["estagio"]
            por_est.setdefault(est, []).append(b)
            if b["bloco_id"] == aluno["bloco_atual"]:
                titulo_bloco_atual = b.get("titulo", titulo_bloco_atual)
                micro_atual = b.get("micro_habilidade", "")

        est_nomes = {let: desc for _, let, _, desc in disc_meta["estagios_meta"]}
        est_atual = aluno["bloco_atual"][:1]
        for est_let in sorted(por_est.keys()):
            itens_est = por_est[est_let]
            dom_est = sum(1 for x in itens_est if x["bloco_id"] in aprov_set)
            tot_est = len(itens_est)
            if dom_est >= tot_est and tot_est > 0:
                status_est = "concluido"
            elif est_let == est_atual or dom_est > 0:
                status_est = "em_andamento"
            else:
                status_est = "pendente"
            estagios_resumo.append(
                {
                    "estagio": est_let,
                    "descricao": est_nomes.get(est_let, f"Estagio {est_let}"),
                    "dominados": dom_est,
                    "total": tot_est,
                    "status": status_est,
                }
            )

    disciplinas_disponiveis = []
    for m in mats:
        dm = _disciplina_publica(m["disciplina"])
        dm["bloco_atual"] = m["bloco_atual"]
        dm["status_curso"] = m.get("status_curso", "EM_ANDAMENTO")
        dm["modo_atual"] = m.get("modo_atual", "pratica")
        disciplinas_disponiveis.append(dm)

    return {
        "aluno": aluno,
        "servidor_agora_iso": _agora_iso(),
        "disciplina_ativa": _disciplina_publica(disc_id),
        "disciplinas_disponiveis": disciplinas_disponiveis,
        "prova_atual": provas[0] if provas else None,
        "provas_recentes": provas[:5],
        "ultima_submissao": ultima_sub,
        "historico_evolucao": historico_evolucao,
        "integralizacao": obter_integralizacao_aluno(aluno_id),
        "grade_bcc": obter_resumo_curriculo_aluno(aluno_id),
        "progresso": {
            "blocos_dominados": len(blocos_aprovados),
            "total_blocos": total_blocos,
            "percentual_curso": round((len(blocos_aprovados) / float(total_blocos)) * 100.0, 1) if total_blocos else 0.0,
            "blocos_aprovados": blocos_aprovados,
            "media_acerto_pct": round(sum(notas) / len(notas), 1) if notas else 0.0,
            "tempo_medio_min": round(sum(tempos) / len(tempos), 1) if tempos else 0.0,
            "total_avaliacoes": len(subs_raw),
            "estagio_atual": aluno["bloco_atual"][:1],
            "titulo_bloco_atual": titulo_bloco_atual,
            "micro_habilidade_atual": micro_atual,
            "estagios_resumo": estagios_resumo,
        },
    }


def obter_estado_dashboard(
    aluno_id: Optional[int] = None,
    disciplina: str = config.DISCIPLINA_PADRAO,
) -> Dict[str, Any]:
    inicializar_banco()
    disc_id = config.normalizar_disciplina_id(disciplina)
    disc_pub = _disciplina_publica(disc_id)
    alunos_disc = listar_alunos(incluir_pin=True, disciplina=disc_id)
    todos_alunos = listar_alunos(incluir_pin=True, disciplina=None)

    aluno = None
    if aluno_id is not None:
        for a in alunos_disc:
            if a["id"] == aluno_id:
                aluno = a
                break
    if aluno is None and alunos_disc:
        aluno = alunos_disc[0]

    with conectar() as conn:
        if aluno:
            aid = aluno["id"]
            provas = [
                dict(r)
                for r in conn.execute(
                    """
                    SELECT * FROM provas_emitidas
                    WHERE aluno_id = ? AND COALESCE(disciplina, 'algoritmos') = ?
                    ORDER BY enviado_em DESC
                    """,
                    (aid, disc_id),
                ).fetchall()
            ]
            subs = [
                dict(r)
                for r in conn.execute(
                    """
                    SELECT * FROM submissoes
                    WHERE aluno_id = ? AND COALESCE(disciplina, 'algoritmos') = ?
                    ORDER BY id DESC
                    """,
                    (aid, disc_id),
                ).fetchall()
            ]
            for s in subs:
                itens = [
                    dict(ir)
                    for ir in conn.execute(
                        "SELECT * FROM itens_submissao WHERE submissao_id = ? ORDER BY id ASC",
                        (s["id"],),
                    ).fetchall()
                ]
                s["itens"] = itens
        else:
            provas = []
            subs = []

    blocos_aprovados = sorted(
        list(
            {
                s["bloco"]
                for s in subs
                if str(s.get("resultado_checagem", "")).startswith("APROVADO")
            }
        )
    )
    tempos = [float(s["tempo_declarado_min"]) for s in subs if s.get("tempo_declarado_min", 0) > 0]
    notas = [float(s["percentual_acerto"]) for s in subs]

    return {
        "disciplina_ativa": disc_pub,
        "disciplinas": config.listar_disciplinas(),
        "alunos": alunos_disc,
        "todos_alunos": todos_alunos,
        "aluno_ativo": aluno,
        "resumo_turma": obter_resumo_turma(disciplina=disc_id),
        "blocos_aprovados": blocos_aprovados,
        "provas_emitidas": provas,
        "submissoes": subs,
        "indicadores": {
            "total_submissoes": len(subs),
            "blocos_dominados": len(blocos_aprovados),
            "total_blocos": disc_pub["total_blocos"],
            "media_acerto_pct": round(sum(notas) / len(notas), 1) if notas else 0.0,
            "tempo_medio_min": round(sum(tempos) / len(tempos), 1) if tempos else 0.0,
        },
        "metricas_jev": obter_metricas_jev_resumo(),
        "acompanhamento_csv": ler_acompanhamento_csv(disciplina=disc_id),
        "integralizacao": obter_integralizacao_aluno(aluno["id"]) if aluno else [],
        "grade_bcc": obter_resumo_curriculo_aluno(aluno["id"] if aluno else None),
    }
