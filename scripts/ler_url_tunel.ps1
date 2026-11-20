<#
    ler_url_tunel.ps1
    Le o log do cloudflared e escreve a URL publica em stdout.
    Aceita dois arquivos (stdout e stderr) porque o cloudflared escreve
    a URL em qualquer um dos dois.

    Usa Get-Content -Raw: o PowerShell abre o arquivo com FileShare
    ReadWrite, entao funciona mesmo com o cloudflared escrevendo no log.
    ([System.IO.File]::ReadAllText exigiria acesso exclusivo e falharia.)

    Uso:
      powershell -File ler_url_tunel.ps1 -LogFile "<tunel.log>" [-LogFile2 "<tunel.err.log>"]
#>
param(
    [Parameter(Mandatory = $true)][string]$LogFile,
    [string]$LogFile2 = ''
)

$ErrorActionPreference = 'SilentlyContinue'
$url = ''

$arquivos = @($LogFile)
if ($LogFile2) { $arquivos += $LogFile2 }

foreach ($f in $arquivos) {
    if ($url) { break }
    if (-not (Test-Path -LiteralPath $f)) { continue }
    $txt = ''
    try {
        $txt = Get-Content -LiteralPath $f -Raw -ErrorAction Stop
    } catch {
        $txt = ''
    }
    if (-not $txt) { continue }
    $m = [regex]::Match($txt, 'https://[-a-z0-9]+\.trycloudflare\.com')
    if ($m.Success) { $url = $m.Value }
}

Write-Output $url
