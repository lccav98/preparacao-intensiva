@echo off
chcp 65001 >nul
setlocal EnableDelayedExpansion

echo ========================================================
echo  SETUP NGROK - Tunel Publico para o Painel do Aluno MV
echo ========================================================
echo.

set "NGROK_ZIP=ngrok-stable-windows-amd64.zip"
set "NGROK_EXE=ngrok.exe"

if exist "%NGROK_EXE%" (
    echo [OK] ngrok ja esta instalado: %~dp0%NGROK_EXE%
    goto :configurar
)

echo [1/3] Baixando ngrok (isso pode levar alguns minutos)...
powershell -Command "Invoke-WebRequest -Uri 'https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-windows-amd64.zip' -OutFile '%NGROK_ZIP%'"
if %errorlevel% neq 0 (
    echo ERRO: Falha ao baixar o ngrok. Baixe manualmente em https://ngrok.com/download
    pause
    exit /b 1
)

echo [2/3] Extraindo ngrok ...
powershell -Command "Expand-Archive -Path '%NGROK_ZIP%' -DestinationPath . -Force"
del "%NGROK_ZIP%" 2>nul

if not exist "%NGROK_EXE%" (
    echo ERRO: ngrok.exe nao encontrado apos extrair.
    pause
    exit /b 1
)
echo [OK] ngrok instalado em: %~dp0%NGROK_EXE%

:configurar
echo.
echo [3/3] Configuracao de tunel ...
echo.
echo Para expor o painel na internet:
echo   1. Rode:      %NGROK_EXE% http 8090
echo   2. Copie a URL publica (ex: https://abc123.ngrok.io)
echo   3. Cole em PREP_PUBLIC_URL no .env (opcional, para cookies Secure)
echo   4. Compartilhe a URL com o aluno para acesso de qualquer lugar
echo.
echo O aluno acessa: <URL_ngrok>/  (portal do aluno)
echo                <URL_ngrok>/admin (painel da professora)
echo.
pause
