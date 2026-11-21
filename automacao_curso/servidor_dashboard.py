#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Servidor HTTP/JSON do Dashboard Gerencial, Portal do Aluno e Autenticacao por Perfil (porta 8090)
e gerador do snapshot interativo estatico dashboard_evolucao.html.
"""

import base64
import csv
import hashlib
import hmac
import http.cookies
import json
import os
import re
import secrets
import sqlite3
import sys
import threading
import time
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any, Dict, Optional

import banco_dados
import config
import gerador_folha
import servico_email
from catalogo_curricular import CatalogoCurricular
from corretor_automatico import OrquestradorCurso

COOKIE_NAME = "prep_session"
SESSION_TTL_SEC = 7 * 24 * 3600

_ORQUESTRADOR: Optional[OrquestradorCurso] = None
_WATCHER: Optional[servico_email.EmailAutoWatcher] = None
_SECRET_BYTES: Optional[bytes] = None
_JOBS_LOCK = threading.Lock()
_JOBS_CORRECAO: Dict[str, Dict[str, Any]] = {}


def _registrar_job_correcao(job_id: str, dados: Dict[str, Any]) -> None:
    with _JOBS_LOCK:
        _JOBS_CORRECAO[job_id] = dados
        if len(_JOBS_CORRECAO) > 100:
            chaves_antigas = list(_JOBS_CORRECAO.keys())[:-100]
            for k in chaves_antigas:
                _JOBS_CORRECAO.pop(k, None)


def _atualizar_job_correcao(job_id: str, **campos: Any) -> None:
    with _JOBS_LOCK:
        if job_id in _JOBS_CORRECAO:
            _JOBS_CORRECAO[job_id].update(campos)
            _JOBS_CORRECAO[job_id]["atualizado_em"] = time.strftime("%Y-%m-%d %H:%M:%S")


def _garantir_csv_inicial() -> None:
    for disc in config.DISCIPLINAS.values():
        alvo = disc["csv_path"]
        if not os.path.isfile(alvo):
            os.makedirs(os.path.dirname(os.path.abspath(alvo)), exist_ok=True)
            with open(alvo, "w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(banco_dados.CSV_COLUNAS)


def _obter_segredo() -> bytes:
    global _SECRET_BYTES
    if config.SECRET_KEY:
        return config.SECRET_KEY.encode("utf-8")
    if _SECRET_BYTES is not None:
        return _SECRET_BYTES
    config.garantir_diretorios()
    secret_file = os.path.join(config.DADOS_DIR, ".secret_key")
    if os.path.isfile(secret_file):
        with open(secret_file, "r", encoding="utf-8") as f:
            val = f.read().strip()
        if val:
            _SECRET_BYTES = val.encode("utf-8")
            return _SECRET_BYTES
    novo = secrets.token_urlsafe(48)
    with open(secret_file, "w", encoding="utf-8") as f:
        f.write(novo)
    _SECRET_BYTES = novo.encode("utf-8")
    return _SECRET_BYTES


def _auth_config_path() -> str:
    return os.path.join(config.DADOS_DIR, "auth_config.json")


def _obter_config_auth() -> Dict[str, Any]:
    """Determina se a exigencia de login/senha esta ativa (env > auth_config.json > aberto)."""
    if config.ADMIN_PASSWORD:
        return {
            "ativo": True,
            "origem": "env",
            "email": config.ADMIN_EMAIL,
            "senha_env": config.ADMIN_PASSWORD,
        }
    auth_path = _auth_config_path()
    if os.path.isfile(auth_path):
        try:
            with open(auth_path, "r", encoding="utf-8") as f:
                cfg = json.load(f)
            if cfg.get("ativo") and cfg.get("admin_senha_hash"):
                return {
                    "ativo": True,
                    "origem": "arquivo",
                    "email": str(cfg.get("admin_email") or config.ADMIN_EMAIL).strip().lower(),
                    "senha_hash": str(cfg["admin_senha_hash"]),
                }
        except Exception:
            pass
    return {
        "ativo": False,
        "origem": "aberto",
        "email": config.ADMIN_EMAIL,
    }


def _auth_status_payload(incluir_email: bool = False) -> Dict[str, Any]:
    cfg = _obter_config_auth()
    return {
        "auth_ativa": bool(cfg["ativo"]),
        "origem": cfg["origem"],
        "admin_email": cfg["email"] if (not cfg["ativo"] or incluir_email) else "",
    }


def obter_orquestrador() -> OrquestradorCurso:
    global _ORQUESTRADOR
    if _ORQUESTRADOR is None:
        config.garantir_diretorios()
        _garantir_csv_inicial()
        _obter_segredo()
        _ORQUESTRADOR = OrquestradorCurso(CatalogoCurricular())
    return _ORQUESTRADOR


def _executar_coleta_com_snapshot() -> list:
    res = obter_orquestrador().processar_caixa_email_e_corrigir()
    if any(not r.get("erro") for r in res):
        gerar_snapshot_dashboard()
    return res


def obter_watcher() -> servico_email.EmailAutoWatcher:
    global _WATCHER
    if _WATCHER is None:
        obter_orquestrador()
        _WATCHER = servico_email.EmailAutoWatcher(_executar_coleta_com_snapshot)
    return _WATCHER


def _b64url_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("ascii")


def _b64url_decode(txt: str) -> bytes:
    pad = "=" * (-len(txt) % 4)
    return base64.urlsafe_b64decode((txt + pad).encode("ascii"))


def assinar_sessao(payload: Dict[str, Any]) -> str:
    dados = dict(payload)
    dados["exp"] = int(time.time()) + SESSION_TTL_SEC
    raw = json.dumps(dados, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    corpo = _b64url_encode(raw)
    sig = hmac.new(_obter_segredo(), corpo.encode("ascii"), hashlib.sha256).hexdigest()
    return f"{corpo}.{sig}"


def verificar_sessao(token: str) -> Optional[Dict[str, Any]]:
    if not token or "." not in token:
        return None
    corpo, sig = token.rsplit(".", 1)
    esperado = hmac.new(_obter_segredo(), corpo.encode("ascii"), hashlib.sha256).hexdigest()
    if not hmac.compare_digest(sig, esperado):
        return None
    try:
        dados = json.loads(_b64url_decode(corpo).decode("utf-8"))
    except Exception:
        return None
    if int(dados.get("exp", 0)) < int(time.time()):
        return None
    if dados.get("role") not in ("aluno", "admin"):
        return None
    return dados


def _sanitizar_resumo_correcao_aluno(res: Dict[str, Any]) -> Dict[str, Any]:
    itens_limpos = [
        {
            "questao_id": it.get("questao_id", ""),
            "tipo_questao": it.get("tipo_questao", ""),
            "resposta_extraida": it.get("resposta_extraida", ""),
            "status_correcao": it.get("status_correcao", ""),
            "categoria_erro": it.get("categoria_erro", ""),
            "feedback_item": it.get("feedback_item", ""),
        }
        for it in (res.get("itens") or [])
    ]
    return {
        "submissao_id": res.get("submissao_id"),
        "protocolo": res.get("protocolo"),
        "disciplina": res.get("disciplina", "algoritmos"),
        "bloco": res.get("bloco"),
        "variante": res.get("variante"),
        "tentativa": res.get("tentativa"),
        "acertos": res.get("acertos"),
        "total": res.get("total"),
        "percentual": res.get("percentual"),
        "aprovado": res.get("aprovado"),
        "tempo_declarado_min": res.get("tempo_declarado_min"),
        "tempo_alvo_min": res.get("tempo_alvo_min"),
        "origem_tempo": res.get("origem_tempo"),
        "fluencia_codigo": res.get("fluencia_codigo"),
        "fluencia_msg": res.get("fluencia_msg"),
        "resultado_checagem": res.get("resultado_checagem"),
        "proxima_acao": res.get("proxima_acao"),
        "bloco_destino": res.get("bloco_destino"),
        "itens": itens_limpos,
    }


def _resumo_mapa_seguro(orq: OrquestradorCurso, disciplina: str) -> list:
    try:
        return orq.obter_catalogo(disciplina).resumo_mapa()
    except Exception:
        return []


def montar_payload_estado(
    aluno_id: Optional[int] = None,
    disciplina: str = config.DISCIPLINA_PADRAO,
) -> Dict[str, Any]:
    orq = obter_orquestrador()
    disc_id = config.normalizar_disciplina_id(disciplina)
    estado = banco_dados.obter_estado_dashboard(aluno_id=aluno_id, disciplina=disc_id)
    estado["mapa_blocos"] = _resumo_mapa_seguro(orq, disc_id)
    estado["emails_spool"] = servico_email.listar_emails_spool()
    estado["auth_status"] = _auth_status_payload(incluir_email=True)
    estado["automacao_email"] = obter_watcher().obter_status()
    return estado


def montar_payload_aluno(
    aluno_id: int,
    is_admin_preview: bool = False,
    disciplina: Optional[str] = None,
) -> Optional[Dict[str, Any]]:
    orq = obter_orquestrador()
    mats = banco_dados.listar_matriculas_aluno(aluno_id)
    if disciplina:
        disc_req = config.normalizar_disciplina_id(disciplina)
        if any(m["disciplina"] == disc_req for m in mats):
            disc_id = disc_req
        else:
            disc_id = mats[0]["disciplina"] if mats else disc_req
    else:
        # Sem disciplina explicita: prioriza a disciplina padrao do servidor
        # (MAT121) quando o aluno esta matriculado nela; senao, a primeira.
        matriculadas = [m["disciplina"] for m in mats]
        if config.DISCIPLINA_PADRAO in matriculadas:
            disc_id = config.DISCIPLINA_PADRAO
        else:
            disc_id = matriculadas[0] if matriculadas else config.DISCIPLINA_PADRAO

    mapa = _resumo_mapa_seguro(orq, disc_id)
    payload = banco_dados.obter_estado_portal_aluno(
        aluno_id=aluno_id, mapa_blocos=mapa, disciplina=disc_id
    )
    if payload is not None:
        payload["is_admin_preview"] = bool(is_admin_preview)
    return payload


def _render_html_com_estado(template_path: str, payload: Any) -> str:
    with open(template_path, "r", encoding="utf-8") as f:
        tpl = f.read()
    estado_json = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
    return tpl.replace("__INITIAL_STATE_JSON__", estado_json)


def gerar_snapshot_dashboard(
    aluno_id: Optional[int] = None,
    disciplina: str = config.DISCIPLINA_PADRAO,
) -> str:
    """Gera dashboard_evolucao.html (gerencial) com o estado atual embutido."""
    config.garantir_diretorios()
    html_final = _render_html_com_estado(
        config.DASHBOARD_HTML_PATH,
        montar_payload_estado(aluno_id=aluno_id, disciplina=disciplina),
    )
    with open(config.DASHBOARD_SNAPSHOT_PATH, "w", encoding="utf-8") as out:
        out.write(html_final)
    return config.DASHBOARD_SNAPSHOT_PATH


class DashboardHandler(BaseHTTPRequestHandler):
    def log_message(self, format: str, *args: Any) -> None:
        pass

    def _cookie_eh_https(self) -> bool:
        """Decide se o cookie de sessao deve receber o flag Secure.

        So marca Secure quando a requisicao realmente chega por HTTPS: via proxy
        (X-Forwarded-Proto) ou no hostname publico configurado em PREP_PUBLIC_URL.
        Sem isso, o acesso local em http://127.0.0.1:8090 deixaria de funcionar
        (o navegador descarta cookies Secure em HTTP).
        """
        proto = (self.headers.get("X-Forwarded-Proto") or "").lower()
        if proto:
            return "https" in proto
        host = (self.headers.get("Host") or "").lower().split(":")[0]
        pub = config.obter_public_url().lower()
        pub_host = pub.split("//")[-1].split("/")[0].split(":")[0]
        if host and pub_host and host == pub_host:
            return pub.startswith("https://")
        return False

    def _montar_set_cookie(self, valor: str, max_age: int) -> str:
        partes = [
            f"{COOKIE_NAME}={valor}",
            "Path=/",
            "HttpOnly",
            "SameSite=Lax",
            f"Max-Age={max_age}",
        ]
        if self._cookie_eh_https():
            partes.append("Secure")
        return "; ".join(partes)

    def _obter_sessao(self) -> Optional[Dict[str, Any]]:
        cookie_hdr = self.headers.get("Cookie", "")
        if not cookie_hdr:
            return None
        jar = http.cookies.SimpleCookie()
        try:
            jar.load(cookie_hdr)
        except Exception:
            return None
        morsel = jar.get(COOKIE_NAME)
        if not morsel:
            return None
        return verificar_sessao(morsel.value)

    def _obter_sessao_efetiva(self) -> Optional[Dict[str, Any]]:
        cfg = _obter_config_auth()
        sess = self._obter_sessao()
        if cfg["ativo"]:
            return sess
        if sess:
            return sess
        return {
            "role": "admin",
            "aluno_id": None,
            "nome": "Modo Configuracao (Sem Senha)",
            "email": cfg["email"],
            "modo_aberto": True,
        }

    def _enviar_json(
        self, payload: Any, status: int = 200, cookie_header: Optional[str] = None
    ) -> None:
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        if cookie_header:
            self.send_header("Set-Cookie", cookie_header)
        self.end_headers()
        self.wfile.write(data)

    def _enviar_html(
        self, html_str: str, status: int = 200, cookie_header: Optional[str] = None
    ) -> None:
        data = html_str.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        if cookie_header:
            self.send_header("Set-Cookie", cookie_header)
        self.end_headers()
        self.wfile.write(data)

    def _redirecionar(self, destino: str, cookie_header: Optional[str] = None) -> None:
        self.send_response(302)
        self.send_header("Location", destino)
        self.send_header("Content-Length", "0")
        self.send_header("Cache-Control", "no-store")
        if cookie_header:
            self.send_header("Set-Cookie", cookie_header)
        self.end_headers()

    def _ler_body(self) -> Dict[str, Any]:
        length = int(self.headers.get("Content-Length", "0"))
        if length <= 0:
            return {}
        raw = self.rfile.read(length).decode("utf-8")
        ctype = (self.headers.get("Content-Type") or "").lower()
        if "application/x-www-form-urlencoded" in ctype:
            parsed = urllib.parse.parse_qs(raw, keep_blank_values=True)
            return {k: v[0] for k, v in parsed.items()}
        return json.loads(raw)

    def _exigir_sessao_api(self) -> Optional[Dict[str, Any]]:
        sess = self._obter_sessao_efetiva()
        if not sess:
            self._enviar_json({"erro": "Autenticacao obrigatoria."}, status=401)
            return None
        return sess

    def _exigir_admin_api(self) -> Optional[Dict[str, Any]]:
        sess = self._exigir_sessao_api()
        if not sess:
            return None
        if sess.get("role") != "admin":
            self._enviar_json(
                {"erro": "Acesso restrito a professora/administradora."}, status=403
            )
            return None
        return sess

    def do_GET(self) -> None:
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        qs = urllib.parse.parse_qs(parsed.query)

        if path == "/health":
            self._enviar_json({"status": "ok"})
            return

        if path == "/api/disciplinas":
            self._enviar_json({"disciplinas": config.listar_disciplinas()})
            return

        if path == "/api/auth-status":
            sess_raw = self._obter_sessao()
            self._enviar_json(
                _auth_status_payload(incluir_email=bool(sess_raw and sess_raw.get("role") == "admin"))
            )
            return

        if path == "/login":
            sess_cookie = self._obter_sessao()
            if sess_cookie:
                self._redirecionar("/admin" if sess_cookie["role"] == "admin" else "/")
                return
            with open(config.LOGIN_HTML_PATH, "r", encoding="utf-8") as f:
                self._enviar_html(f.read())
            return

        sess = self._obter_sessao_efetiva()

        if path == "/" or path == "/index.html":
            if not sess:
                self._redirecionar("/login")
                return
            if sess["role"] == "admin":
                self._redirecionar("/admin")
                return
            payload = montar_payload_aluno(int(sess["aluno_id"]), is_admin_preview=False)
            if payload is None:
                self._redirecionar("/login", cookie_header=self._montar_set_cookie("", 0))
                return
            self._enviar_html(_render_html_com_estado(config.PORTAL_ALUNO_HTML_PATH, payload))
            return

        if path == "/aluno":
            if not sess:
                dest_next = urllib.parse.quote(self.path, safe="")
                self._redirecionar(f"/login?next={dest_next}")
                return
            disc_qs = (qs.get("disciplina") or [""])[0] or None
            if sess["role"] == "aluno":
                aid = int(sess["aluno_id"])
                preview = False
            else:
                preview = True
                if "aluno_id" in qs and qs["aluno_id"][0].isdigit():
                    aid = int(qs["aluno_id"][0])
                else:
                    alunos = banco_dados.listar_alunos(incluir_pin=False, disciplina=disc_qs)
                    if not alunos and disc_qs:
                        alunos = banco_dados.listar_alunos(incluir_pin=False)
                    if not alunos:
                        self._redirecionar("/admin")
                        return
                    aid = int(alunos[0]["id"])
            payload = montar_payload_aluno(aid, is_admin_preview=preview, disciplina=disc_qs)
            if payload is None:
                self._enviar_json({"erro": "Aluno nao encontrado."}, status=404)
                return
            self._enviar_html(_render_html_com_estado(config.PORTAL_ALUNO_HTML_PATH, payload))
            return

        if path == "/admin":
            if not sess:
                self._redirecionar("/login")
                return
            if sess["role"] != "admin":
                self._redirecionar("/")
                return
            disc_qs = (qs.get("disciplina") or [config.DISCIPLINA_PADRAO])[0]
            aid = int(qs["aluno_id"][0]) if "aluno_id" in qs and qs["aluno_id"][0].isdigit() else None
            self._enviar_html(
                _render_html_com_estado(
                    config.DASHBOARD_HTML_PATH,
                    montar_payload_estado(aluno_id=aid, disciplina=disc_qs),
                )
            )
            return

        if path == "/api/sessao":
            if not sess:
                self._enviar_json({"erro": "Nao autenticado."}, status=401)
                return
            self._enviar_json(
                {
                    "role": sess["role"],
                    "aluno_id": sess.get("aluno_id"),
                    "nome": sess.get("nome", ""),
                    "email": sess.get("email", ""),
                    "modo_aberto": bool(sess.get("modo_aberto")),
                }
            )
            return

        if path == "/api/aluno/estado":
            if not sess:
                self._enviar_json({"erro": "Autenticacao obrigatoria."}, status=401)
                return
            disc_qs = (qs.get("disciplina") or [""])[0] or None
            if sess["role"] == "aluno":
                aid = int(sess["aluno_id"])
                preview = False
            else:
                preview = True
                if "aluno_id" in qs and qs["aluno_id"][0].isdigit():
                    aid = int(qs["aluno_id"][0])
                else:
                    alunos = banco_dados.listar_alunos(incluir_pin=False, disciplina=disc_qs)
                    if not alunos and disc_qs:
                        alunos = banco_dados.listar_alunos(incluir_pin=False)
                    if not alunos:
                        self._enviar_json({"erro": "Nenhum aluno cadastrado."}, status=404)
                        return
                    aid = int(alunos[0]["id"])
            payload = montar_payload_aluno(aid, is_admin_preview=preview, disciplina=disc_qs)
            if payload is None:
                self._enviar_json({"erro": "Aluno nao encontrado."}, status=404)
                return
            self._enviar_json(payload)
            return

        if path == "/api/estado":
            if not self._exigir_admin_api():
                return
            disc_qs = (qs.get("disciplina") or [config.DISCIPLINA_PADRAO])[0]
            aid = int(qs["aluno_id"][0]) if "aluno_id" in qs and qs["aluno_id"][0].isdigit() else None
            self._enviar_json(montar_payload_estado(aluno_id=aid, disciplina=disc_qs))
            return

        if path == "/api/automacao/status":
            if not self._exigir_admin_api():
                return
            self._enviar_json(obter_watcher().obter_status())
            return

        if path == "/api/admin/csv":
            if not self._exigir_admin_api():
                return
            _garantir_csv_inicial()
            disc_qs = (qs.get("disciplina") or [config.DISCIPLINA_PADRAO])[0]
            disc_meta = config.obter_disciplina(disc_qs)
            alvo_csv = disc_meta["csv_path"]
            fname_csv = "00_acompanhamento_mv.csv" if disc_meta["id"] == "matrizes_vetores" else "00_acompanhamento.csv"
            with open(alvo_csv, "rb") as f:
                data = f.read()
            self.send_response(200)
            self.send_header("Content-Type", "text/csv; charset=utf-8")
            self.send_header("Content-Disposition", f'attachment; filename="{fname_csv}"')
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
            return

        if path == "/api/admin/backup-db":
            if not self._exigir_admin_api():
                return
            banco_dados.inicializar_banco()
            with open(config.DB_PATH, "rb") as f:
                data = f.read()
            self.send_response(200)
            self.send_header("Content-Type", "application/x-sqlite3")
            self.send_header("Content-Disposition", 'attachment; filename="automacao.db"')
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
            return

        if path.startswith("/api/submissoes/status/"):
            sess_st = self._exigir_sessao_api()
            if not sess_st:
                return
            job_id = path[len("/api/submissoes/status/"):].strip()
            with _JOBS_LOCK:
                job = dict(_JOBS_CORRECAO.get(job_id) or {})
            if not job:
                self._enviar_json({"erro": "Processamento nao encontrado."}, status=404)
                return
            if sess_st.get("role") == "aluno" and job.get("aluno_id") != int(sess_st["aluno_id"]):
                self._enviar_json({"erro": "Acesso negado a este processamento."}, status=403)
                return
            self._enviar_json(job)
            return

        if path.startswith("/folha/"):
            if not sess:
                accept = (self.headers.get("Accept") or "").lower()
                if "text/html" in accept:
                    self._redirecionar("/login")
                else:
                    self._enviar_json({"erro": "Autenticacao obrigatoria."}, status=401)
                return
            prot = os.path.basename(path[len("/folha/"):]).strip()
            prot_safe = re.sub(r"[^a-zA-Z0-9_-]", "", prot)
            if not prot_safe:
                self._enviar_json({"erro": "Protocolo invalido."}, status=400)
                return
            prova = banco_dados.obter_prova(prot_safe)
            if not prova:
                self._enviar_json({"erro": "Folha de prova nao encontrada."}, status=404)
                return
            if sess["role"] == "aluno" and int(prova["aluno_id"]) != int(sess["aluno_id"]):
                self._enviar_json({"erro": "Acesso negado a folha de outro aluno."}, status=403)
                return
            folha_path = os.path.join(config.FOLHAS_DIR, f"{prot_safe}.html")
            if not os.path.isfile(folha_path):
                try:
                    al_f = banco_dados.obter_aluno_por_id(int(prova["aluno_id"]), incluir_pin=False)
                    disc_p = config.normalizar_disciplina_id(
                        prova.get("disciplina") or config.disciplina_por_protocolo(prot_safe)
                    )
                    bloco_f = obter_orquestrador().obter_catalogo(disc_p).obter(prova["bloco"])
                    if al_f and bloco_f:
                        folha_gerada = gerador_folha.gerar_folha_prova(
                            aluno=al_f,
                            bloco=bloco_f,
                            variante=prova["variante"],
                            tentativa=int(prova["tentativa"]),
                            modo=prova["modo"],
                            protocolo=prot_safe,
                            disciplina=disc_p,
                        )
                        folha_path = folha_gerada.get("caminho_folha_html") or folha_path
                except Exception:
                    pass
            if os.path.isfile(folha_path):
                with open(folha_path, "r", encoding="utf-8") as f:
                    self._enviar_html(f.read())
            else:
                self._enviar_json({"erro": "Arquivo da folha nao encontrado."}, status=404)
            return

        self._enviar_json({"erro": "Rota nao encontrada."}, status=404)

    def _tratar_submissao_binaria(self, orq: OrquestradorCurso) -> None:
        sess = self._exigir_sessao_api()
        if not sess:
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            length = 0
        if length <= 0:
            self._enviar_json({"erro": "Arquivo vazio ou Content-Length ausente."}, status=400)
            return
        if length > 25 * 1024 * 1024:
            self._enviar_json({"erro": "Arquivo excede o limite de 25 MB."}, status=413)
            return

        raw_bytes = self.rfile.read(length)
        nome_raw = urllib.parse.unquote(self.headers.get("X-Prep-Filename", "prova.png") or "prova.png")
        prot = urllib.parse.unquote(self.headers.get("X-Prep-Protocolo", "") or "").strip()
        disc_hdr = urllib.parse.unquote(self.headers.get("X-Prep-Disciplina", "") or "").strip() or None

        aid_sess = sess.get("aluno_id")
        if sess["role"] == "aluno":
            aid_int = int(aid_sess)
            if prot:
                prova = banco_dados.obter_prova(prot)
                if not prova:
                    self._enviar_json({"erro": "Protocolo nao encontrado."}, status=404)
                    return
                if int(prova["aluno_id"]) != aid_int:
                    self._enviar_json(
                        {"erro": "Voce so pode enviar respostas das suas proprias provas."},
                        status=403,
                    )
                    return
            else:
                estado_al = banco_dados.obter_estado_portal_aluno(aid_int, disciplina=disc_hdr)
                if not estado_al or not estado_al.get("prova_atual"):
                    self._enviar_json(
                        {"erro": "Nenhuma folha ativa encontrada para sua conta."},
                        status=400,
                    )
                    return
                prot = estado_al["prova_atual"]["protocolo"]
        elif prot:
            prova = banco_dados.obter_prova(prot)
            if prova:
                aid_sess = int(prova["aluno_id"])

        config.garantir_diretorios()
        fname = re.sub(r"[^a-zA-Z0-9._-]", "_", os.path.basename(nome_raw)) or "prova.png"
        prefix = f"al{aid_sess or 'adm'}_{int(time.time())}_"
        destino = os.path.join(config.UPLOADS_DIR, prefix + fname)
        with open(destino, "wb") as f:
            f.write(raw_bytes)

        job_id = secrets.token_hex(10)
        agora = time.strftime("%Y-%m-%d %H:%M:%S")
        eh_aluno = sess.get("role") == "aluno"
        _registrar_job_correcao(
            job_id,
            {
                "ok": True,
                "job_id": job_id,
                "aluno_id": int(aid_sess) if aid_sess is not None else None,
                "protocolo": prot,
                "arquivo": fname,
                "tamanho_bytes": len(raw_bytes),
                "etapa": "arquivo_recebido",
                "mensagem": "Arquivo recebido pelo servidor.",
                "atualizado_em": agora,
                "erro": "",
                "resultado": None,
            },
        )

        def _worker() -> None:
            try:
                _atualizar_job_correcao(
                    job_id,
                    etapa="lendo_e_corrigindo",
                    mensagem="Lendo respostas manuscritas e corrigindo...",
                )
                res = orq.processar_submissao_imagem(
                    caminho_imagem=destino,
                    protocolo_override=prot,
                )
                gerar_snapshot_dashboard(disciplina=res.get("disciplina", config.DISCIPLINA_PADRAO))
                out_res = _sanitizar_resumo_correcao_aluno(res) if eh_aluno else res
                _atualizar_job_correcao(
                    job_id,
                    etapa="concluido",
                    mensagem="Correcao concluida.",
                    resultado=out_res,
                )
            except Exception as exc:
                _atualizar_job_correcao(
                    job_id,
                    ok=False,
                    etapa="erro",
                    erro=str(exc),
                    mensagem="Falha ao processar o arquivo enviado.",
                )

        threading.Thread(target=_worker, name=f"JobCorr-{job_id[:6]}", daemon=True).start()
        self._enviar_json(
            {
                "ok": True,
                "job_id": job_id,
                "protocolo": prot,
                "etapa": "arquivo_recebido",
                "mensagem": "Arquivo recebido pelo servidor.",
            },
            status=202,
        )

    def do_POST(self) -> None:
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        orq = obter_orquestrador()
        if path == "/api/submeter-foto-binario":
            self._tratar_submissao_binaria(orq)
            return
        ctype = (self.headers.get("Content-Type") or "").lower()
        eh_form = "application/x-www-form-urlencoded" in ctype

        try:
            body = self._ler_body()
        except Exception as exc:
            self._enviar_json({"erro": f"Requisicao invalida: {exc}"}, status=400)
            return

        try:
            if path == "/api/login":
                perfil = str(body.get("perfil", "aluno")).strip().lower()
                email = str(body.get("email", "")).strip().lower()
                senha = str(body.get("senha", "")).strip()

                if perfil == "admin":
                    cfg = _obter_config_auth()
                    if not cfg["ativo"]:
                        ok_adm = True
                    elif cfg["origem"] == "env":
                        ok_adm = (email == cfg["email"]) and hmac.compare_digest(
                            senha, cfg["senha_env"]
                        )
                    else:
                        ok_adm = (email == cfg["email"]) and banco_dados.verificar_senha(
                            senha, cfg["senha_hash"]
                        )
                    if ok_adm:
                        token = assinar_sessao(
                            {
                                "role": "admin",
                                "aluno_id": None,
                                "nome": "Professora / Administradora",
                                "email": cfg["email"],
                            }
                        )
                        ck = self._montar_set_cookie(token, SESSION_TTL_SEC)
                        if eh_form:
                            self._redirecionar("/admin", cookie_header=ck)
                        else:
                            self._enviar_json(
                                {"ok": True, "role": "admin", "redirect": "/admin"},
                                cookie_header=ck,
                            )
                        return
                    self._enviar_json(
                        {"erro": "E-mail ou senha da professora invalidos."}, status=401
                    )
                    return

                al = banco_dados.autenticar_aluno(email, senha)
                if not al:
                    self._enviar_json(
                        {"erro": "E-mail ou PIN do aluno invalidos."}, status=401
                    )
                    return

                token = assinar_sessao(
                    {
                        "role": "aluno",
                        "aluno_id": al["id"],
                        "nome": al["nome"],
                        "email": al["email"],
                    }
                )
                ck = self._montar_set_cookie(token, SESSION_TTL_SEC)
                next_raw = str(body.get("next", "")).strip()
                destino_aluno = (
                    next_raw
                    if next_raw.startswith("/") and not next_raw.startswith("//") and not next_raw.startswith("/admin")
                    else "/"
                )
                if eh_form:
                    self._redirecionar(destino_aluno, cookie_header=ck)
                else:
                    self._enviar_json(
                        {"ok": True, "role": "aluno", "aluno_id": al["id"], "redirect": destino_aluno},
                        cookie_header=ck,
                    )
                return

            if path == "/api/logout":
                ck = self._montar_set_cookie("", 0)
                if eh_form:
                    self._redirecionar("/login", cookie_header=ck)
                else:
                    self._enviar_json({"ok": True, "redirect": "/login"}, cookie_header=ck)
                return

            if path == "/api/admin/config-auth":
                if not self._exigir_admin_api():
                    return
                cfg_atual = _obter_config_auth()
                ativo = bool(body.get("ativo", True))
                auth_file = _auth_config_path()
                config.garantir_diretorios()
                if not ativo:
                    if cfg_atual["origem"] == "env":
                        self._enviar_json(
                            {
                                "erro": "A senha esta travada pela variavel de ambiente PREP_ADMIN_PASSWORD no servidor."
                            },
                            status=400,
                        )
                        return
                    with open(auth_file, "w", encoding="utf-8") as f:
                        json.dump(
                            {"ativo": False, "admin_email": cfg_atual["email"]},
                            f,
                            ensure_ascii=False,
                            indent=2,
                        )
                    self._enviar_json(
                        {"ok": True, "auth_status": _auth_status_payload(incluir_email=True)},
                        cookie_header=self._montar_set_cookie("", 0),
                    )
                    return

                admin_email = str(
                    body.get("admin_email") or cfg_atual["email"] or config.ADMIN_EMAIL
                ).strip().lower()
                admin_senha = str(body.get("admin_senha", "")).strip()
                if "@" not in admin_email:
                    self._enviar_json({"erro": "Informe um e-mail valido."}, status=400)
                    return
                if len(admin_senha) < 6:
                    self._enviar_json(
                        {"erro": "A senha da professora deve ter pelo menos 6 caracteres."},
                        status=400,
                    )
                    return
                with open(auth_file, "w", encoding="utf-8") as f:
                    json.dump(
                        {
                            "ativo": True,
                            "admin_email": admin_email,
                            "admin_senha_hash": banco_dados.hash_senha(admin_senha),
                        },
                        f,
                        ensure_ascii=False,
                        indent=2,
                    )
                token = assinar_sessao(
                    {
                        "role": "admin",
                        "aluno_id": None,
                        "nome": "Professora / Administradora",
                        "email": admin_email,
                    }
                )
                ck = self._montar_set_cookie(token, SESSION_TTL_SEC)
                self._enviar_json(
                    {"ok": True, "auth_status": _auth_status_payload(incluir_email=True)},
                    cookie_header=ck,
                )
                return

            if path == "/api/alunos":
                if not self._exigir_admin_api():
                    return
                nome = str(body.get("nome", "")).strip()
                email = str(body.get("email", "")).strip()
                bloco = str(body.get("bloco_inicial", "A01")).strip().upper()
                senha_ini = str(body.get("senha_inicial", "")).strip()
                disc_req = config.normalizar_disciplina_id(body.get("disciplina", config.DISCIPLINA_PADRAO))
                if not nome or not email:
                    self._enviar_json({"erro": "Nome e e-mail sao obrigatorios."}, status=400)
                    return
                al = banco_dados.obter_ou_criar_aluno(
                    nome,
                    email,
                    bloco_inicial=bloco,
                    senha_inicial=senha_ini,
                    disciplina=disc_req,
                )
                gerar_snapshot_dashboard(al["id"], disciplina=disc_req)
                self._enviar_json(al, status=201)
                return

            if path == "/api/matriculas":
                if not self._exigir_admin_api():
                    return
                aid = int(body["aluno_id"])
                disc_req = config.normalizar_disciplina_id(body.get("disciplina", "matrizes_vetores"))
                bloco = str(body.get("bloco_inicial", "A01")).strip().upper()
                modo_ini = str(body.get("modo_inicial", "pratica")).strip().lower()
                emitir_agora = bool(body.get("emitir_prova", False))
                mat = banco_dados.matricular_aluno(
                    aid,
                    disciplina=disc_req,
                    bloco_inicial=bloco,
                    modo_inicial=modo_ini,
                )
                prova_emit = None
                if emitir_agora:
                    prova_emit = orq.emitir_e_enviar_prova(aid, disciplina=disc_req)
                gerar_snapshot_dashboard(aid, disciplina=disc_req)
                self._enviar_json(
                    {"ok": True, "matricula": mat, "emissao": prova_emit},
                    status=201,
                )
                return

            if path == "/api/alunos/reset-pin":
                if not self._exigir_admin_api():
                    return
                aid = int(body["aluno_id"])
                nova_senha = str(body.get("nova_senha", "")).strip()
                al = banco_dados.redefinir_pin_aluno(aid, nova_senha=nova_senha)
                if not al:
                    self._enviar_json({"erro": "Aluno nao encontrado."}, status=404)
                    return
                self._enviar_json(al)
                return

            if path == "/api/alunos/excluir":
                if not self._exigir_admin_api():
                    return
                try:
                    aid = int(body.get("aluno_id", 0))
                except (TypeError, ValueError):
                    aid = 0
                confirmar_email = str(body.get("confirmar_email", "")).strip().lower()
                confirmacao_dupla = bool(body.get("confirmacao_dupla", False))
                if aid <= 0:
                    self._enviar_json({"erro": "ID do aluno invalido."}, status=400)
                    return
                al_alvo = banco_dados.obter_aluno_por_id(aid, incluir_pin=False)
                if not al_alvo:
                    self._enviar_json({"erro": "Aluno nao encontrado."}, status=404)
                    return
                if not confirmacao_dupla:
                    self._enviar_json(
                        {"erro": "Confirmacao dupla obrigatoria para excluir o aluno."},
                        status=400,
                    )
                    return
                if confirmar_email != str(al_alvo["email"]).strip().lower():
                    self._enviar_json(
                        {"erro": "O e-mail digitado nao corresponde ao aluno selecionado."},
                        status=400,
                    )
                    return
                excluido = banco_dados.excluir_aluno(aid)
                disc_req = config.normalizar_disciplina_id(
                    body.get("disciplina") or config.DISCIPLINA_PADRAO
                )
                gerar_snapshot_dashboard(disciplina=disc_req)
                self._enviar_json({"ok": True, "excluido": excluido})
                return

            if path == "/api/admin/restore-db":
                if not self._exigir_admin_api():
                    return
                b64 = str(body.get("db_base64", "")).strip()
                if not b64:
                    self._enviar_json({"erro": "Campo db_base64 obrigatorio."}, status=400)
                    return
                try:
                    raw = base64.b64decode(b64, validate=True)
                except Exception:
                    self._enviar_json({"erro": "db_base64 invalido."}, status=400)
                    return
                if not raw.startswith(b"SQLite format 3\x00"):
                    self._enviar_json(
                        {"erro": "Arquivo nao possui cabecalho SQLite 3 valido."},
                        status=400,
                    )
                    return
                config.garantir_diretorios()
                db_dir = os.path.dirname(os.path.abspath(config.DB_PATH))
                os.makedirs(db_dir, exist_ok=True)
                tmp_path = os.path.join(db_dir, f".restore_{os.getpid()}_{secrets.token_hex(6)}.db")
                src_conn = None
                dst_conn = None
                try:
                    with open(tmp_path, "wb") as f:
                        f.write(raw)
                    src_conn = sqlite3.connect(tmp_path)
                    chk = src_conn.execute("PRAGMA integrity_check").fetchone()
                    if not chk or str(chk[0]).lower() != "ok":
                        raise ValueError("Banco SQLite falhou na verificacao de integridade.")
                    dst_conn = banco_dados.conectar()
                    src_conn.backup(dst_conn)
                    dst_conn.close()
                    dst_conn = None
                    src_conn.close()
                    src_conn = None
                    banco_dados.inicializar_banco()
                except Exception as exc:
                    if dst_conn is not None:
                        try:
                            dst_conn.close()
                        except Exception:
                            pass
                    if src_conn is not None:
                        try:
                            src_conn.close()
                        except Exception:
                            pass
                    self._enviar_json({"erro": f"Falha ao restaurar banco: {exc}"}, status=500)
                    return
                finally:
                    if os.path.isfile(tmp_path):
                        try:
                            os.remove(tmp_path)
                        except OSError:
                            pass
                self._enviar_json({"ok": True, "bytes": len(raw)})
                return

            if path == "/api/emitir-prova":
                if not self._exigir_admin_api():
                    return
                aid = int(body["aluno_id"])
                modo = body.get("modo")
                disc_req = body.get("disciplina")
                if modo and modo not in ("pratica", "checagem"):
                    self._enviar_json({"erro": "Modo deve ser 'pratica' ou 'checagem'."}, status=400)
                    return
                res = orq.emitir_e_enviar_prova(
                    aluno_id=aid,
                    bloco_id=body.get("bloco"),
                    variante=body.get("variante"),
                    tentativa=body.get("tentativa"),
                    modo=modo,
                    disciplina=disc_req,
                )
                disc_snap = res["prova"].get("disciplina") or config.DISCIPLINA_PADRAO
                gerar_snapshot_dashboard(aid, disciplina=disc_snap)
                self._enviar_json({"prova": res["prova"], "email": res["email"]})
                return

            if path == "/api/iniciar-cronometro":
                sess = self._exigir_sessao_api()
                if not sess:
                    return
                prot = str(body.get("protocolo", "")).strip()
                if not prot:
                    self._enviar_json({"erro": "Protocolo obrigatorio."}, status=400)
                    return
                prova = banco_dados.obter_prova(prot)
                if not prova:
                    self._enviar_json({"erro": "Protocolo nao encontrado."}, status=404)
                    return
                if sess["role"] == "aluno" and int(prova["aluno_id"]) != int(sess["aluno_id"]):
                    self._enviar_json({"erro": "Esta prova pertence a outro aluno."}, status=403)
                    return
                p = banco_dados.iniciar_cronometro_prova(prot)
                self._enviar_json(p)
                return

            if path == "/api/encerrar-cronometro":
                sess = self._exigir_sessao_api()
                if not sess:
                    return
                prot = str(body.get("protocolo", "")).strip()
                if not prot:
                    self._enviar_json({"erro": "Protocolo obrigatorio."}, status=400)
                    return
                prova = banco_dados.obter_prova(prot)
                if not prova:
                    self._enviar_json({"erro": "Protocolo nao encontrado."}, status=404)
                    return
                if sess["role"] == "aluno" and int(prova["aluno_id"]) != int(sess["aluno_id"]):
                    self._enviar_json({"erro": "Esta prova pertence a outro aluno."}, status=403)
                    return
                seg = body.get("tempo_decorrido_seg")
                p = banco_dados.encerrar_cronometro_prova(prot, tempo_decorrido_seg=seg)
                gerar_snapshot_dashboard(p["aluno_id"])
                self._enviar_json(p)
                return

            if path == "/api/submeter-foto":
                sess = self._exigir_sessao_api()
                if not sess:
                    return
                b64 = str(body.get("imagem_base64", ""))
                if not b64:
                    self._enviar_json({"erro": "Arquivo em base64 nao enviado."}, status=400)
                    return
                prot = str(body.get("protocolo", "")).strip()
                if sess["role"] == "aluno":
                    aid_sess = int(sess["aluno_id"])
                    if prot:
                        prova = banco_dados.obter_prova(prot)
                        if not prova:
                            self._enviar_json({"erro": "Protocolo nao encontrado."}, status=404)
                            return
                        if int(prova["aluno_id"]) != aid_sess:
                            self._enviar_json(
                                {"erro": "Voce so pode enviar respostas das suas proprias provas."},
                                status=403,
                            )
                            return
                    else:
                        disc_body = body.get("disciplina") or None
                        estado_al = banco_dados.obter_estado_portal_aluno(aid_sess, disciplina=disc_body)
                        if not estado_al or not estado_al.get("prova_atual"):
                            self._enviar_json(
                                {"erro": "Nenhuma folha ativa encontrada para sua conta."},
                                status=400,
                            )
                            return
                        prot = estado_al["prova_atual"]["protocolo"]

                fname = re.sub(r"[^a-zA-Z0-9._-]", "_", str(body.get("nome_arquivo", "prova.png")))
                prefix = f"al{sess.get('aluno_id') or 'adm'}_{int(time.time())}_"
                destino = os.path.join(config.UPLOADS_DIR, prefix + fname)
                with open(destino, "wb") as f:
                    f.write(base64.b64decode(b64))
                res = orq.processar_submissao_imagem(
                    caminho_imagem=destino,
                    protocolo_override=prot,
                    tempo_override_min=body.get("tempo_min"),
                )
                gerar_snapshot_dashboard(disciplina=res.get("disciplina", config.DISCIPLINA_PADRAO))
                if sess["role"] == "aluno":
                    self._enviar_json(_sanitizar_resumo_correcao_aluno(res))
                else:
                    self._enviar_json(res)
                return

            if path == "/api/coletar-emails":
                if not self._exigir_admin_api():
                    return
                resultados = obter_watcher().executar_ciclo_agora()
                self._enviar_json({"processados": len(resultados), "resultados": resultados})
                return

            if path == "/api/admin/config-integracoes":
                if not self._exigir_admin_api():
                    return
                cfg_atual = config.obter_integracoes()
                campos_permitidos = {
                    "smtp_host",
                    "smtp_port",
                    "smtp_user",
                    "smtp_pass",
                    "smtp_from",
                    "imap_host",
                    "imap_port",
                    "imap_user",
                    "imap_pass",
                    "imap_poll_sec",
                    "gemini_api_key",
                    "gemini_model",
                    "brevo_api_key",
                    "webhook_token",
                }
                filtrados = {k: v for k, v in body.items() if k in campos_permitidos}
                preview_cfg = dict(cfg_atual)
                for k, v in filtrados.items():
                    if k in ("smtp_pass", "imap_pass", "gemini_api_key", "brevo_api_key", "webhook_token"):
                        if str(v or "").strip():
                            preview_cfg[k] = str(v).strip()
                    elif v is not None and str(v).strip() != "":
                        preview_cfg[k] = int(v) if k in ("smtp_port", "imap_port", "imap_poll_sec") else str(v).strip()

                teste = None
                if body.get("testar_conexao", True):
                    teste = servico_email.testar_conexao_email(preview_cfg)

                if body.get("apenas_testar"):
                    self._enviar_json(
                        {
                            "ok": True,
                            "teste_conexao": teste,
                            "status": obter_watcher().obter_status(),
                        }
                    )
                    return

                config.salvar_integracoes(filtrados)
                obter_watcher().acordar()
                self._enviar_json(
                    {
                        "ok": True,
                        "teste_conexao": teste,
                        "status": obter_watcher().obter_status(),
                    }
                )
                return

            if path == "/api/webhook/email-entrada":
                cfg_int = config.obter_integracoes()
                tok_esperado = cfg_int.get("webhook_token", "")
                qs_post = urllib.parse.parse_qs(parsed.query)
                tok_hdr = str(self.headers.get("X-Prep-Webhook-Token", "")).strip()
                tok_qs = str(qs_post.get("token", [""])[0]).strip()
                tok_enviado = tok_hdr or tok_qs
                autorizado_token = bool(
                    tok_esperado and tok_enviado and hmac.compare_digest(tok_enviado, tok_esperado)
                )
                if not autorizado_token:
                    if not self._exigir_admin_api():
                        return

                remetente = str(body.get("remetente", "")).strip()
                assunto = str(body.get("assunto", "")).strip()
                prot_bruto = str(body.get("protocolo", "")).strip()
                if not prot_bruto:
                    m_p = re.search(r"(PREP-(?:MV-)?[A-H]\d{2}-V\d+-T\d+-[A-F0-9]+)", assunto, re.IGNORECASE)
                    if m_p:
                        prot_bruto = m_p.group(1).upper()
                prot_resolvido = servico_email.resolver_protocolo_entrada(prot_bruto, remetente)
                b64 = str(body.get("arquivo_base64") or body.get("imagem_base64") or "").strip()
                if not b64:
                    self._enviar_json({"erro": "arquivo_base64 nao enviado."}, status=400)
                    return
                fname = re.sub(r"[^a-zA-Z0-9._-]", "_", str(body.get("nome_arquivo", "webhook_prova.pdf")))
                destino = os.path.join(config.UPLOADS_DIR, f"wh_{int(time.time())}_{fname}")
                with open(destino, "wb") as f:
                    f.write(base64.b64decode(b64))
                res = orq.processar_submissao_imagem(
                    caminho_imagem=destino,
                    protocolo_override=prot_resolvido,
                    tempo_override_min=body.get("tempo_min"),
                )
                gerar_snapshot_dashboard(disciplina=res.get("disciplina", config.DISCIPLINA_PADRAO))
                self._enviar_json(res)
                return

            self._enviar_json({"erro": "Endpoint POST desconhecido."}, status=404)
        except Exception as exc:
            self._enviar_json({"erro": str(exc)}, status=400)


def criar_servidor(host: str = config.DASHBOARD_HOST, port: int = config.DASHBOARD_PORT) -> ThreadingHTTPServer:
    obter_orquestrador()
    gerar_snapshot_dashboard()
    obter_watcher().iniciar()
    return ThreadingHTTPServer((host, port), DashboardHandler)


def main() -> None:
    if "--snapshot-only" in sys.argv:
        snap = gerar_snapshot_dashboard()
        print(f"Snapshot estatico gerado em: {snap}")
        return

    srv = criar_servidor()
    print(f"Dashboard Multi-Disciplina de Preparacao Intensiva (CC61A & MAT121) rodando em http://{config.DASHBOARD_HOST}:{config.DASHBOARD_PORT}")
    print("Pressione Ctrl+C para encerrar.")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        obter_watcher().parar()
        srv.shutdown()


if __name__ == "__main__":
    main()
