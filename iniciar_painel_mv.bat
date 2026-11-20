@echo off
chcp 65001 >nul
setlocal

REM ================================================================
REM  PAINEL DO ALUNO - MATRIZES E VETORES - MAT121 - UTFPR-PG
REM  Preparacao Intensiva - Acesso Remoto de Qualquer Lugar
REM ================================================================
echo.
echo ========================================================
echo  PAINEL DO ALUNO - MATRIZES E VETORES - MAT121 - UTFPR-PG
echo  Preparacao Intensiva - Acesso Remoto de Qualquer Lugar
echo ========================================================
echo.

REM ------------------------------------------------------------
REM Diretorios: o servidor vive em <raiz>\automacao_curso
REM
REM RAIZP = raiz SEM barra invertida final. Isso e obrigatorio:
REM o parser de linha de comando do PowerShell trata o \" de
REM "C:\pasta\" como escape e engoliria todos os argumentos
REM seguintes num unico valor.
REM ------------------------------------------------------------
set "RAIZ=%~dp0"
set "RAIZP=%RAIZ:~0,-1%"
set "AUTO_DIR=%RAIZP%\automacao_curso"
set "SCRIPTS_DIR=%RAIZP%\scripts"
if not exist "%AUTO_DIR%\" (
    echo ERRO: pasta do servidor nao encontrada: %AUTO_DIR%
    pause
    exit /b 1
)

REM ------------------------------------------------------------
REM [1/5] Carregar .env da raiz do curso
REM O parser fica em scripts\carregar_env.ps1 porque o .env aceita
REM valores com espacos (senha de app do Google no formato 4-4-4-4),
REM "!" (ex.: Prep2026!) e "&" - que o for/f nativo do CMD corrompe.
REM ------------------------------------------------------------
set "ENV_TMP=%TEMP%\prep_env_%RANDOM%.cmd"
if exist "%RAIZ%.env" (
    echo [1/5] Carregando variaveis de ambiente do arquivo .env ...
    powershell -NoProfile -ExecutionPolicy Bypass -File "%SCRIPTS_DIR%\carregar_env.ps1" -EnvFile "%RAIZP%\.env" -OutFile "%ENV_TMP%" >nul
    if exist "%ENV_TMP%" (
        call "%ENV_TMP%"
        del /q "%ENV_TMP%" >nul 2>&1
    ) else (
        echo       AVISO: falha ao carregar o .env. Verifique %SCRIPTS_DIR%\carregar_env.ps1
    )
) else (
    echo [1/5] AVISO: .env nao encontrado em %RAIZ%.env
    echo         Copie .env.example para .env e preencha PREP_ADMIN_PASSWORD.
)

if "%PORT%"=="" set "PORT=8090"

REM ------------------------------------------------------------
REM [2/5] Verificar o curso de Matrizes e Vetores
REM Se PREP_CURSO_MV_DIR nao vier do .env, usa o padrao do config.py.
REM ------------------------------------------------------------
set "CAMINHO_MV=%PREP_CURSO_MV_DIR%"
if not defined CAMINHO_MV (
    set "CAMINHO_MV=C:\Users\d7opa\Documents\Matrizes e Vetores\Curso_Preparacao_Intensiva_Matrizes_Vetores"
)
if not exist "%CAMINHO_MV%\" (
    echo ERRO: Diretorio do curso MV nao encontrado:
    echo       %CAMINHO_MV%
    echo       Ajuste PREP_CURSO_MV_DIR no .env.
    pause
    exit /b 1
)
echo [2/5] Curso MV encontrado em: %CAMINHO_MV%

cd /d "%AUTO_DIR%"

REM ------------------------------------------------------------
REM [3/5] Encerrar execucoes anteriores DESTE projeto
REM Usa os arquivos .pid e o caminho do executavel para nao
REM matar processos de terceiros.
REM ------------------------------------------------------------
echo [3/5] Limpando execucoes anteriores deste projeto ...
powershell -NoProfile -ExecutionPolicy Bypass -File "%SCRIPTS_DIR%\encerrar_processo.ps1" -PidFile "%RAIZP%\servidor.pid" >nul
powershell -NoProfile -ExecutionPolicy Bypass -File "%SCRIPTS_DIR%\encerrar_processo.ps1" -PidFile "%RAIZP%\tunel.pid" -ProcessName "cloudflared" -MatchPath "%RAIZP%" >nul
for /f "tokens=5" %%p in ('netstat -ano ^| findstr /r /c:":%PORT% .*LISTENING"') do (
    if not "%%p"=="0" taskkill /F /PID %%p >nul 2>&1
)

REM ------------------------------------------------------------
REM [4/5] Servidor HTTP + tunel publico (Cloudflare quick tunnel)
REM O tunel sobe logo apos o servidor; a URL publica e gravada no
REM .env para que os e-mails e cookies usem o endereco HTTPS.
REM ------------------------------------------------------------
set "TUNEL_URL="
set "TUNEL_LOG=%RAIZP%\tunel.log"

echo [4/5] Iniciando servidor HTTP na porta %PORT% ...
powershell -NoProfile -ExecutionPolicy Bypass -File "%SCRIPTS_DIR%\iniciar_processo.ps1" -FilePath "python" -Args "servidor_dashboard.py" -WorkingDirectory "%AUTO_DIR%" -StdOutFile "%RAIZP%\servidor.log" -StdErrFile "%RAIZP%\servidor.err.log" -PidFile "%RAIZP%\servidor.pid" >nul

for /f "usebackq tokens=*" %%h in (`powershell -NoProfile -ExecutionPolicy Bypass -File "%SCRIPTS_DIR%\aguardar_saude.ps1" -Url "http://127.0.0.1:%PORT%/health" -Tentativas 25 -EsperaSeg 1`) do set "SAUDE=%%h"
echo       Servidor: %SAUDE%

REM ------------------------------------------------------------
REM O tunel fica em rotulos (goto) e NAO em bloco if/else: dentro
REM de um bloco, o CMD expande %VAR% no momento da analise, ou
REM seja, a URL apareceria vazia mesmo tendo sido capturada.
REM ------------------------------------------------------------
if not exist "%RAIZP%\cloudflared.exe" goto :SEM_TUNEL

echo       Subindo tunel publico via Cloudflare ...
if exist "%TUNEL_LOG%" del /q "%TUNEL_LOG%" >nul 2>&1
powershell -NoProfile -ExecutionPolicy Bypass -File "%SCRIPTS_DIR%\iniciar_processo.ps1" -FilePath "%RAIZP%\cloudflared.exe" -Args "tunnel|--url|http://localhost:%PORT%|--no-autoupdate" -WorkingDirectory "%RAIZP%" -StdOutFile "%TUNEL_LOG%" -StdErrFile "%RAIZP%\tunel.err.log" -PidFile "%RAIZP%\tunel.pid" >nul

REM espera a URL aparecer no log do cloudflared
for /l %%i in (1,1,30) do (
    if not defined TUNEL_URL (
        for /f "usebackq tokens=*" %%u in (`powershell -NoProfile -ExecutionPolicy Bypass -File "%SCRIPTS_DIR%\ler_url_tunel.ps1" -LogFile "%TUNEL_LOG%" -LogFile2 "%RAIZP%\tunel.err.log"`) do set "TUNEL_URL=%%u"
        if not defined TUNEL_URL powershell -NoProfile -Command "Start-Sleep -Milliseconds 1000" >nul
    )
)

if not defined TUNEL_URL goto :TUNEL_FALHOU

echo       URL publica: %TUNEL_URL%
REM grava a URL no .env (sem BOM) para o servidor e os e-mails usa-la
powershell -NoProfile -ExecutionPolicy Bypass -File "%SCRIPTS_DIR%\gravar_public_url.ps1" -EnvFile "%RAIZP%\.env" -Url "%TUNEL_URL%" >nul
if errorlevel 1 (
    echo       AVISO: nao foi possivel gravar PREP_PUBLIC_URL no .env
) else (
    echo       PREP_PUBLIC_URL gravado no .env
)
goto :FIM_TUNEL

:TUNEL_FALHOU
echo       AVISO: nao foi possivel ler a URL do tunel. Veja %TUNEL_LOG%
goto :FIM_TUNEL

:SEM_TUNEL
echo       Tunel: cloudflared.exe nao encontrado na raiz do curso.
echo       Rode setup_ngrok.bat ou baixe o cloudflared para acesso externo.

:FIM_TUNEL

REM ------------------------------------------------------------
REM [5/5] Resumo dos enderecos
REM ------------------------------------------------------------
echo.
echo ========================================================
echo  PAINEL GERENCIAL da professora: http://localhost:%PORT%/admin
echo  PORTAO DO ALUNO:               http://localhost:%PORT%/
echo  Acesso na rede local:          http://%COMPUTERNAME%:%PORT%/
if not defined TUNEL_URL goto :FIM_RESUMO
echo  ACESSO DE QUALQUER LUGAR:
echo    Aluno:      %TUNEL_URL%/
echo    Professora: %TUNEL_URL%/admin
:FIM_RESUMO
echo ========================================================
echo.
echo  Pressione qualquer tecla para encerrar o servidor...
pause >nul

REM encerra SOMENTE o servidor e o tunel deste projeto
powershell -NoProfile -ExecutionPolicy Bypass -File "%SCRIPTS_DIR%\encerrar_processo.ps1" -PidFile "%RAIZP%\servidor.pid" >nul
powershell -NoProfile -ExecutionPolicy Bypass -File "%SCRIPTS_DIR%\encerrar_processo.ps1" -PidFile "%RAIZP%\tunel.pid" -ProcessName "cloudflared" -MatchPath "%RAIZP%" >nul
for /f "tokens=5" %%p in ('netstat -ano ^| findstr /r /c:":%PORT% .*LISTENING"') do (
    if not "%%p"=="0" taskkill /F /PID %%p >nul 2>&1
)
endlocal
