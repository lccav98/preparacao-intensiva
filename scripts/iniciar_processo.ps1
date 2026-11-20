<#
    iniciar_processo.ps1
    Inicia um processo em background com redirecionamento de saida e
    grava o PID em arquivo (para encerrar exatamente aquele processo
    depois, sem matar processos de terceiros).

    Os argumentos sao passados como UMA string separada por "|", porque o
    `powershell -File` do CMD nao faz o parse de arrays: um caminho com
    barra invertida final (ex.: "%~dp0") faria o parser engolir todos os
    argumentos seguintes num unico valor.

    Uso:
      powershell -File iniciar_processo.ps1 -FilePath "<exe>" -Args "a|b|c" ^
                 -WorkingDirectory "<dir>" -StdOutFile "<log>" -StdErrFile "<log.err>" -PidFile "<pid>"
#>
param(
    [Parameter(Mandatory = $true)][string]$FilePath,
    [string]$Args = '',
    [Parameter(Mandatory = $true)][string]$WorkingDirectory,
    [string]$StdOutFile = '',
    [string]$StdErrFile = '',
    [string]$PidFile = ''
)

$ErrorActionPreference = 'Stop'

# Remove barras invertidas finais: "%~dp0" do CMD sempre termina com "\"
$wd = $WorkingDirectory.Trim().TrimEnd('\')
if (-not (Test-Path -LiteralPath $wd)) {
    throw ("WorkingDirectory inexistente: " + $wd)
}

$argList = @()
if ($Args -ne '') {
    $argList = @($Args -split '\|' | Where-Object { $_ -ne '' })
}

$psi = @{
    FilePath        = $FilePath
    WorkingDirectory = $wd
    WindowStyle     = 'Hidden'
    PassThru        = $true
}
if ($argList.Count -gt 0) { $psi['ArgumentList'] = $argList }
if ($StdOutFile) { $psi['RedirectStandardOutput'] = $StdOutFile }
if ($StdErrFile) { $psi['RedirectStandardError'] = $StdErrFile }

$p = Start-Process @psi

if ($PidFile) {
    $enc = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::WriteAllText($PidFile, [string]$p.Id, $enc)
}
Write-Output $p.Id
