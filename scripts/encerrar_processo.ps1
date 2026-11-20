<#
    encerrar_processo.ps1
    Encerra o processo cujo PID esta no arquivo indicado (sem matar
    processos de terceiros que por acaso tenham o mesmo nome).

    Quando -ProcessName e -MatchPath sao usados juntos, so encerra os
    processos cujo executavel esteja dentro de -MatchPath (ex.: o
    cloudflared.exe desta pasta), preservando tuneis de outros projetos.

    Uso:
      powershell -File encerrar_processo.ps1 -PidFile "<arquivo.pid>" ^
                 [-ProcessName "cloudflared" -MatchPath "<pasta>"]
#>
param(
    [string]$PidFile = '',
    [string]$ProcessName = '',
    [string]$MatchPath = ''
)

$ErrorActionPreference = 'SilentlyContinue'

if ($PidFile -and (Test-Path -LiteralPath $PidFile)) {
    try {
        $pidTxt = [System.IO.File]::ReadAllText($PidFile).Trim()
        if ($pidTxt) {
            $procId = [int]$pidTxt
            Stop-Process -Id $procId -Force -ErrorAction SilentlyContinue
            Write-Output ("ENCERRADO_PID=" + $procId)
        }
    } catch {
    }
    Remove-Item -LiteralPath $PidFile -Force -ErrorAction SilentlyContinue
}

if ($ProcessName) {
    foreach ($p in @(Get-Process -Name $ProcessName -ErrorAction SilentlyContinue)) {
        if ($MatchPath) {
            # so encerra se o executavel estiver dentro de MatchPath
            $exe = ''
            try { $exe = $p.Path } catch { continue }
            if (-not $exe) { continue }
            $raiz = $MatchPath.TrimEnd('\')
            if ($exe.ToLower().StartsWith($raiz.ToLower())) {
                Stop-Process -Id $p.Id -Force -ErrorAction SilentlyContinue
                Write-Output ("ENCERRADO_PROC=" + $p.Id)
            }
        } else {
            Stop-Process -Id $p.Id -Force -ErrorAction SilentlyContinue
            Write-Output ("ENCERRADO_PROC=" + $p.Id)
        }
    }
}
exit 0
