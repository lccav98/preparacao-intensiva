<#
    aguardar_saude.ps1
    Aguarda o servidor responder em /health. Retorna "OK" ou a mensagem
    de erro. Nao usa 'timeout' do CMD (que falha com stdin redirecionado).

    Uso:
      powershell -File aguardar_saude.ps1 -Url "http://127.0.0.1:8090/health" -Tentativas 20 -EsperaSeg 1
#>
param(
    [Parameter(Mandatory = $true)][string]$Url,
    [int]$Tentativas = 20,
    [int]$EsperaSeg = 1
)

for ($i = 1; $i -le $Tentativas; $i++) {
    try {
        $r = Invoke-WebRequest -Uri $Url -UseBasicParsing -TimeoutSec 4
        if ($r.StatusCode -eq 200) {
            Write-Output ('OK=' + $r.Content)
            exit 0
        }
    } catch {
        $last = $_.Exception.Message
    }
    Start-Sleep -Milliseconds ($EsperaSeg * 1000)
}
Write-Output ('FALHOU=' + $(if ($last) { $last } else { 'sem resposta' }))
exit 1
