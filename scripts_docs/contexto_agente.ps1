# =============================================================================
# contexto_agente.ps1
# Genera un bloque de contexto listo para pegar al agente IA al inicio de
# jornada. Muestra fecha/hora, proyecto, rama, ultimo commit y estado Git.
# Uso: .\contexto_agente.ps1   (ejecutar desde la raiz del proyecto)
# Compatible con pwsh (Windows y Linux)
# =============================================================================

# El script vive en scripts_docs/ — subir un nivel para obtener la raíz del proyecto
$ProjectRoot = Split-Path $PSScriptRoot -Parent
Set-Location $ProjectRoot

# Datos del repo
$Proyecto    = Split-Path -Leaf $ProjectRoot
$Rama        = git rev-parse --abbrev-ref HEAD 2>$null
$UltimoCommit = git log -1 --pretty=format:"%s (%h)" 2>$null
$FechaHora   = Get-Date -Format "yyyy-MM-dd HH:mm"

# Estado git: separar modificados y sin trackear
$StatusLineas = git status --porcelain 2>$null

$Modificados   = $StatusLineas | Where-Object { $_ -match '^\s*M' }
$SinTrackear   = $StatusLineas | Where-Object { $_ -match '^\?\?' }
$Eliminados    = $StatusLineas | Where-Object { $_ -match '^\s*D' }
$Agregados     = $StatusLineas | Where-Object { $_ -match '^\s*A' }

# Salida
Write-Host ""
Write-Host "--- CONTEXTO PARA EL AGENTE ---"
Write-Host "FECHA/HORA   : $FechaHora"
Write-Host "PROYECTO     : $Proyecto"
Write-Host "RAMA         : $Rama"
Write-Host "ULTIMO COMMIT: $UltimoCommit"
Write-Host ""

if ($Modificados) {
    Write-Host "MODIFICADOS (M):"
    $Modificados | ForEach-Object { Write-Host "   $_" }
    Write-Host ""
}

if ($Agregados) {
    Write-Host "AGREGADOS (A):"
    $Agregados | ForEach-Object { Write-Host "   $_" }
    Write-Host ""
}

if ($Eliminados) {
    Write-Host "ELIMINADOS (D):"
    $Eliminados | ForEach-Object { Write-Host "   $_" }
    Write-Host ""
}

if ($SinTrackear) {
    Write-Host "SIN TRACKEAR (??):"
    $SinTrackear | ForEach-Object { Write-Host "  $_" }
    Write-Host ""
}

if (-not $Modificados -and -not $Agregados -and -not $Eliminados -and -not $SinTrackear) {
    Write-Host "ESTADO: nada que commitear, working tree limpio"
    Write-Host ""
}

# Diferencia con origin
$Ahead  = [int](git rev-list --count "origin/$Rama..$Rama" 2>$null)
$Behind = [int](git rev-list --count "$Rama..origin/$Rama" 2>$null)
if ($Ahead -gt 0 -or $Behind -gt 0) {
    Write-Host "SYNC ORIGIN  : +$Ahead adelante / -$Behind atrás"
    Write-Host ""
} else {
    Write-Host "SYNC ORIGIN  : al dia con origin/$Rama"
    Write-Host ""
}
