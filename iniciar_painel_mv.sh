#!/usr/bin/env bash
# =============================================================================
# Painel do Aluno - Matrizes e Vetores (MAT121 - UTFPR-PG)
# Inicia o servidor HTTP e opcionalmente expõe um tunel publico (ngrok/cloudflared)
# para acesso de qualquer computador ou celular, em casa ou em qualquer lugar.
# =============================================================================
set -euo pipefail

cd "$(dirname "$0")"

# Carrega .env se existir
if [[ -f .env ]]; then
  echo "[1/5] Carregando .env ..."
  set -a
  source .env
  set +a
else
  echo "[1/5] AVISO: .env nao encontrado. Copie .env.example para .env e preencha PREP_ADMIN_PASSWORD."
fi

export PORT="${PORT:-8090}"
export PREP_DASHBOARD_HOST="${PREP_DASHBOARD_HOST:-0.0.0.0}"
export DISCIPLINA_PADRAO="${DISCIPLINA_PADRAO:-matrizes_vetores}"
export PREP_CURSO_MV_DIR="${PREP_CURSO_MV_DIR:-/cursos/matrizes_vetores}"
export PREP_DATA_DIR="${PREP_DATA_DIR:-./dados}"

# Verifica diretorio do curso MV
if [[ ! -d "$PREP_CURSO_MV_DIR" ]]; then
  echo "ERRO: Diretorio do curso MV nao encontrado: $PREP_CURSO_MV_DIR"
  echo "      Ajuste PREP_CURSO_MV_DIR no .env."
  exit 1
fi
echo "[2/5] Curso MV encontrado em: $PREP_CURSO_MV_DIR"

# Dependencias Python
echo "[3/5] Instalando dependencias Python ..."
python3 -m pip install -q -r requirements.txt 2>/dev/null || true

# Verifica se ja esta rodando na porta
if curl -s http://127.0.0.1:${PORT}/health >/dev/null 2>&1; then
  echo "[4/5] Servidor ja esta online em http://127.0.0.1:${PORT}"
else
  echo "[4/5] Iniciando servidor na porta ${PORT} ..."
  nohup python3 servidor_dashboard.py > servidor.log 2>&1 &
  echo $! > servidor.pid
  sleep 4
  if curl -s http://127.0.0.1:${PORT}/health >/dev/null 2>&1; then
    echo "      Servidor online em http://127.0.0.1:${PORT}"
  else
    echo "      Falha ao iniciar. Veja servidor.log"
    exit 1
  fi
fi

echo ""
echo "=========================================================="
echo "  PAINEL GERENCIAL (professora): http://localhost:${PORT}/admin"
echo "  PORTAO DO ALUNO:               http://localhost:${PORT}/"
echo "  Acesso na rede local:          http://<SEU_IP_LOCAL>:${PORT}/"
echo "=========================================================="
echo ""
echo "Para acessar de QUALQUER LUGAR (fora de casa), expore um tunel:"
echo ""
echo "  Opcao A - ngrok (mais simples):"
echo "    1. Baixe em: https://ngrok.com/download"
echo "    2. Rode:     ngrok http ${PORT}"
echo "    3. Compartilhe a URL publica (https://...) com o aluno."
echo ""
echo "  Opcao B - cloudflared (Cloudflare Tunnel, gratuito):"
echo "    1. Rode:     cloudflared tunnel --url http://localhost:${PORT}"
echo "    2. Compartilhe a URL trycloudflare.com gerada."
echo ""
echo "  Opcao C - Deploy na nuvem (Railway/Render):"
echo "    docker-compose up --build"
echo "=========================================================="
echo ""
echo "Para parar o servidor: kill \$(cat servidor.pid)  (Linux/Mac)"
echo "                       taskkill /F /IM python.exe  (Windows)"
