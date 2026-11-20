# 🎓 Painel do Aluno — Matrizes e Vetores (MAT121)

Sistema de **Preparação Intensiva** com acesso remoto: o aluno entra no seu painel de qualquer computador ou celular, em casa ou em qualquer lugar, para acompanhar o progresso, abrir folhas de prova, enviar respostas digitalizadas e ver feedback.

---

## 📁 O que está aqui

| Arquivo | Função |
|---------|--------|
| `iniciar_painel_mv.bat` | (Windows) Sobe o servidor + túnel público Cloudflare e grava a URL no `.env` |
| `iniciar_painel_mv.sh` | (Linux/Mac) Mesmo propósito acima |
| `setup_ngrok.bat` | (Windows) Baixa e instala o ngrok para expor na internet |
| `cloudflared.exe` | (Windows) Cloudflare Tunnel — já instalado nesta pasta |
| `scripts/carregar_env.ps1` | Le o `.env` e gera as variaveis para o CMD (aceita valores com espacos, `!` e `&`) |
| `scripts/ler_url_tunel.ps1` | Extrai a URL `trycloudflare.com` do log do tunel |
| `scripts/gravar_public_url.ps1` | Atualiza `PREP_PUBLIC_URL` no `.env` sem gravar BOM UTF-8 |
| `scripts/iniciar_processo.ps1` | Sobe servidor/tunel em background e grava o PID |
| `scripts/encerrar_processo.ps1` | Encerra apenas os processos deste projeto (nao os de terceiros) |
| `scripts/aguardar_saude.ps1` | Aguarda o `/health` responder antes de seguir |
| `automacao_curso/testar_smtp_e_reemitir.py` | Testa o SMTP e reemite uma folha (linha de comando) |
| `automacao_curso/verificar_entregas_email.py` | Confirma via IMAP se o Gmail aceitou a entrega e se houve bounce |
| `.env.example` | Modelo de variaveis de ambiente (copie para `.env`) |
| `docker-compose.yml` | Orquestração com volumes (banco SQLite persistente + curso MV montado) |
| `servidor_dashboard.py` | Servidor HTTP/JSON (porta 8090) — já suporta MAT121 nativamente |
| `ui/portal_aluno.html` | Interface do aluno (responsiva: celular e desktop) |
| `ui/login.html` | Tela de login do aluno (e-mail + PIN de 6 dígitos) |
| `ui/dashboard.html` | Painel gerencial da professora |

---

## 🚀 Como colocar o ar (3 passos)

### Passo 1 — Configurar variáveis de ambiente

Copie o exemplo e preencha, no mínimo, a senha da professora:

```cmd
copy .env.example .env
```

Edite `.env` e defina:

```env
PREP_ADMIN_PASSWORD=sua_senha_forte_aqui
PREP_CURSO_MV_DIR=C:/Users/d7opa/Documents/Matrizes e Vetores/Curso_Preparacao_Intensiva_Matrizes_Vetores
```

> ⚠️ `PREP_ADMIN_PASSWORD` é obrigatória para acesso externo seguro. Sem ela, o painel abre em modo aberto (somente localhost recomendado).

### Passo 2 — Iniciar o servidor

No Windows, dê duplo-clique em:

```
iniciar_painel_mv.bat
```

Ou no terminal:

```powershell
cd automacao_curso
python servidor_dashboard.py
```

> ✅ O `automacao_curso/config.py` **lê o `.env` da raiz do curso automaticamente**.
> Não importa como o servidor é iniciado (duplo clique, terminal, Docker): `PREP_PUBLIC_URL`,
> `PREP_ADMIN_PASSWORD`, `PREP_SMTP_*` e `PREP_DATA_DIR` sempre são aplicados.
> Para apontar para outro arquivo: `PREP_ENV_FILE=C:\caminho\meu.env`.

O servidor sobe na **porta 8090**:
- Portal do aluno: `http://localhost:8090/`
- Painel da professora: `http://localhost:8090/admin`

Na rede local (celular no mesmo Wi-Fi): `http://<SEU_IP_LOCAL>:8090/`

### Passo 3 — Expor para qualquer lugar (fora de casa)

O `iniciar_painel_mv.bat` já faz isso sozinho quando o `cloudflared.exe` está na raiz do curso:
ele sobe o túnel **antes** do servidor, lê a URL `https://xxx.trycloudflare.com`, grava em
`PREP_PUBLIC_URL` no `.env` e mostra os endereços no final.

**Opção A — Cloudflare Tunnel (gratuito, já instalado aqui — recomendada):**

```cmd
iniciar_painel_mv.bat
```

Ou manualmente:

```cmd
cloudflared tunnel --url http://localhost:8090
```

> ⚠️ O *quick tunnel* gera uma URL **temporária**: ela muda a cada reinício do túnel.
> Para um endereço fixo, crie uma conta no Cloudflare e use um túnel nomeado
> (`cloudflared tunnel create` + `cloudflared tunnel route dns`), ou use o ngrok com
> conta (domínio fixo `https://seu-subdominio.ngrok.io`).

**Opção B — ngrok (mais simples, conta gratuita):**

```cmd
setup_ngrok.bat          # baixa e instala o ngrok (uma única vez)
ngrok http 8090          # expõe a porta local na internet
```

O ngrok mostra uma URL pública tipo `https://abc123.ngrok.io`. Compartilhe com o aluno:
- Aluno acessa: `https://abc123.ngrok.io/`
- Professora acessa: `https://abc123.ngrok.io/admin`

**Opção C — Deploy na nuvem (Railway / Render):**

```bash
docker-compose up --build
```

Defina `PREP_PUBLIC_URL=https://seu-app.dominio.com` no `.env` para cookies Secure funcionarem corretamente em HTTPS.

---

## 📧 E-mail: entrega real (SMTP) vs. spool local

Por padrão o sistema grava a folha em `.eml` dentro de `automacao_curso/spool_email/enviados/`
(**modo `SPOOL_LOCAL`**) — nada sai pela internet. Para entrega real, preencha no `.env`:

```env
PREP_SMTP_HOST=smtp.gmail.com
PREP_SMTP_PORT=587
PREP_SMTP_USER=seu@gmail.com
PREP_SMTP_PASS=senha_de_aplicacao_16_chars
PREP_SMTP_FROM=seu@gmail.com
```

No Gmail a senha de aplicação fica em
`https://myaccount.google.com/apppasswords` (exige verificação em 2 etapas).
O Google exibe a senha no formato `xxxx xxxx xxxx xxxx` — **pode colar com os espaços**:
o `config.py` remove automaticamente os espaços de agrupamento (somente quando o
padrão 4-4-4-4 é reconhecido, para não alterar outras senhas).

Depois de salvar, **reinicie o servidor** e confira em
`Painel → Configurar E-mail & IA` ou em `GET /api/estado` o campo
`automacao_email.smtp_configurado`.

Teste rápido pela linha de comando:

```powershell
cd automacao_curso
python testar_smtp_e_reemitir.py
```

| `modo_entrega` | Significado |
|---|---|
| `SMTP_REAL` | A folha foi realmente transmitida ao servidor do e-mail |
| `SPOOL_LOCAL` | A folha foi apenas gravada em disco (sem SMTP configurado) |

### 🔎 Aluno diz que não recebeu a prova

Antes de reemitir, **confirme a entrega** — o Gmail arquiva em
`[Gmail]/E-mails enviados` tudo que foi aceito pelo servidor SMTP, e a
mesma senha de aplicação funciona no IMAP:

```powershell
cd automacao_curso
python verificar_entregas_email.py --aluno 2          # por ID do aluno
python verificar_entregas_email.py --email aluno@x.com
python verificar_entregas_email.py --protocolo PREP-MV-A01-V1-T1-0BFF50
```

O script imprime:

* as **entregas aceitas** (pasta de enviados) para aquele destinatário;
* os **avisos de falha de entrega** (bounce/NDR) em todas as pastas;
* um **veredito**.

| Veredito | O que fazer |
|---|---|
| Entrega aceita **e** sem bounce | A emissão funcionou. O problema é no lado do aluno: spam, aba "Promoções/Atualizações", ou endereço divergente. Peça para ele checar **todas as abas + spam** e confirmar o e-mail cadastrado. |
| Bounce encontrado | O endereço do aluno está errado/inexistente. Corrija o e-mail no painel e reemita. |
| Nenhuma entrega na janela | A folha não foi enviada (modo `SPOOL_LOCAL`) ou a emissão falhou. Reemita pelo painel. |

> Um destinatário inexistente faz o `smtplib` levantar `SMTPRecipientsRefused`
> (código 550), que o sistema reporta em `erro_smtp` com `enviado_smtp=false`.
> Então `enviado_smtp=true` **já garante** que o endereço é válido e foi aceito.

**Rota alternativa garantida:** mesmo sem e-mail, o aluno acessa
`/folha/<protocolo>` pelo próprio portal (botão *"Abrir Folha A4 para
Imprimir"*), autenticado com e-mail + PIN. Teste rápido pela API:

```powershell
curl -H "Cookie: sessao=<cookie>" "https://<tunel>/folha/PREP-MV-A01-V1-T1-0BFF50"
```

---

## 👨‍🎓 Fluxo do aluno no painel

1. **Login:** e-mail + PIN de 6 dígitos (gerado automaticamente pela professora).
2. **Escolhe a disciplina:** se matriculado em mais de uma (ex: Algoritmos + Matrizes e Vetores).
3. **Veja o bloco atual:** micro-habilidade, estágio, percentual de domínio.
4. **Abra a folha A4:** imprime a prova do bloco atual com protocolo `PREP-MV-<BLOCO>-<VARIANTE>-T<TENTATIVA>-<HASH>`.
5. **Cronômetro:** inicia ao começar a escrever no papel; encerra ao terminar.
6. **Envia foto/PDF:** tira foto da prova resolvida e envia para correção automática.
7. **Feedback:** vê acertos, erros com categoria, dificuldade observada e próximo bloco liberado (apenas com 100% na checagem independente).

---

## 👩‍🏫 Fluxo da professora (painel gerencial)

1. **Cadastra o aluno:** e-mail → gera PIN automático.
2. **Matricula em Matrizes e Vetores:** define bloco inicial (ex: `A01`).
3. **Emite a prova:** escolhe bloco, variante e modo (prática/checagem).
4. **Acompanha a turma:** tabela de blocos dominados, últimas submissões, métricas JEV.
5. **Exporta CSV:** `00_acompanhamento_mv.csv` com as 12 colunas padrão.

---

## 🔐 Segurança

| Camada | Como funciona |
|--------|---------------|
| Autenticação | Login com e-mail + PIN (aluno) ou senha (professora) |
| Sessão | Cookie JWT assinado (HMAC-SHA256), expira em 7 dias |
| Acesso a folhas | O aluno só vê/edita suas próprias provas |
| Acesso externo | Exigir `PREP_ADMIN_PASSWORD` + `PREP_PUBLIC_URL` em HTTPS |
| Banco | SQLite criptografado por pasta de dados persistente (`./dados`) |

---

## 🐳 Docker (implantação em nuvem)

```bash
# 1. Copie e ajuste o .env
copy .env.example .env

# 2. Ajuste CURSO_MV_WINDOWS_PATH no docker-compose.yml se necessário

# 3. Suba
docker-compose up --build -d

# 4. Acesse https://<SEU_DOMINIO>/  (defina PREP_PUBLIC_URL)
```

O volume `prep_data` persiste banco de dados, CSVs e sessões entre reinicializações.

---

## 📱 Compatibilidade

- **Desktop:** Chrome, Firefox, Edge, Safari
- **Celular:** Chrome Mobile, Safari Mobile (interface responsiva, botões grandes para toque)
- **Tablet:** mesma interface do desktop, adaptada à largura da tela

---

## 🛠️ Solução de problemas

| Problema | Solução |
|----------|---------|
| Servidor não sobe | Confirme que a porta 8090 não está em uso: `netstat -ano \| findstr 8090` |
| Aluno não consegue acessar de fora | O túnel não está rodando. Suba `cloudflared tunnel --url http://localhost:8090` (ou `iniciar_painel_mv.bat`) e confira a URL |
| Link do e-mail aponta para `127.0.0.1` | `PREP_PUBLIC_URL` vazio no `.env`. Preencha com a URL do túnel e **reinicie o servidor** |
| Painel abre sem pedir senha | O `.env` não está sendo lido. Confirme que `automacao_curso/config.py` está atualizado e que existe `.env` na raiz do curso |
| Painel abre sempre em "Algoritmos" | `DISCIPLINA_PADRAO=matrizes_vetores` no `.env` + reiniciar o servidor |
| Login não funciona | Confirme `PREP_ADMIN_PASSWORD` no `.env`; reinicie o servidor |
| Prova não chega no e-mail do aluno | Verifique `automacao_email.smtp_configurado`; sem SMTP a folha fica só no spool local |
| Folha não carrega | O aluno precisa ter uma prova emitida pelo painel da professora |
| Banco corrompido | Apague a pasta `automacao_curso/dados` e reinicie (perde histórico de submissões) |

---

## 📄 Licença

Uso interno — Curso de Preparação Intensiva MAT121, UTFPR – Campus Ponta Grossa.
