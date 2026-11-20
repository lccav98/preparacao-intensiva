<#
    gravar_public_url.ps1
    Atualiza (ou acrescenta) PREP_PUBLIC_URL no .env SEM BOM.

    Uso:
      powershell -File gravar_public_url.ps1 -EnvFile "<arquivo.env>" -Url "<https://...>"
#>
param(
    [Parameter(Mandatory = $true)][string]$EnvFile,
    [Parameter(Mandatory = $true)][string]$Url
)

$ErrorActionPreference = 'Stop'
$novo = 'PREP_PUBLIC_URL=' + $Url

if (Test-Path -LiteralPath $EnvFile) {
    $linhas = [System.IO.File]::ReadAllLines($EnvFile)
    $achou = $false
    $saida = New-Object System.Collections.Generic.List[string]
    foreach ($l in $linhas) {
        if ($l -match '^\s*PREP_PUBLIC_URL\s*=') {
            $saida.Add($novo)
            $achou = $true
        } else {
            $saida.Add($l)
        }
    }
    if (-not $achou) { $saida.Add($novo) }
} else {
    $saida = New-Object System.Collections.Generic.List[string]
    $saida.Add($novo)
}

$enc = New-Object System.Text.UTF8Encoding($false)
[System.IO.File]::WriteAllLines($EnvFile, $saida, $enc)
Write-Output ('GRAVADO=' + $novo)
