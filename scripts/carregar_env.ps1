<#
    carregar_env.ps1
    Le um arquivo .env e gera um .cmd com linhas "set "KEY=VALUE""
    para o CMD consumir sem corromper valores (espacos, "!", "&", etc.).

    Uso:
      powershell -File carregar_env.ps1 -EnvFile "<arquivo.env>" -OutFile "<saida.cmd>"
#>
param(
    [Parameter(Mandatory = $true)][string]$EnvFile,
    [Parameter(Mandatory = $true)][string]$OutFile
)

$ErrorActionPreference = 'Stop'
$lines = New-Object System.Collections.Generic.List[string]

if (Test-Path -LiteralPath $EnvFile) {
    foreach ($raw in [System.IO.File]::ReadAllLines($EnvFile)) {
        $t = $raw.Trim()
        if ($t -eq '' -or $t.StartsWith('#') -or $t -notmatch '=') { continue }
        $i = $t.IndexOf('=')
        $key = $t.Substring(0, $i).Trim()
        $val = $t.Substring($i + 1).Trim()
        # remove aspas envolventes, se houver
        if ($val.Length -ge 2 -and $val.StartsWith('"') -and $val.EndsWith('"')) {
            $val = $val.Substring(1, $val.Length - 2)
        }
        if (-not $key) { continue }
        # aspas duplas dentro do valor quebrariam o set do CMD
        $val = $val.Replace('"', '""')
        $lines.Add('set "' + $key + '=' + $val + '"')
    }
}

# grava SEM BOM (PS 5.1 -Encoding UTF8 adicionaria BOM e corromperia a 1a chave)
$enc = New-Object System.Text.UTF8Encoding($false)
[System.IO.File]::WriteAllLines($OutFile, $lines, $enc)
Write-Output ("GERADOS=" + $lines.Count)
