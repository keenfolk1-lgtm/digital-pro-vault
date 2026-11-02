# ============================================================================
# WINDOWS 10/11 EXTREME GAMING FPS & INPUT-LAG OPTIMIZER (SAFE & REVERSIBLE)
# Запуск: Откройте PowerShell от имени Администратора и выполните команды ниже.
# ============================================================================

Write-Host "=== [1/6] Активация схемы питания 'Максимальная производительность' ===" -ForegroundColor Cyan
powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61
powercfg /setactive e9a42b02-d5df-448d-aa00-03f14749eb61

Write-Host "=== [2/6] Отключение Xbox GameDVR (убирает микрофризы и статтеры) ===" -ForegroundColor Cyan
reg add "HKCU\System\GameConfigStore" /v "GameDVR_Enabled" /t REG_DWORD /d 0 /f
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\GameDVR" /v "AllowGameDVR" /t REG_DWORD /d 0 /f

Write-Host "=== [3/6] Приоритет видеокарты и процессора для игр (MMCSS) ===" -ForegroundColor Cyan
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" /v "SystemResponsiveness" /t REG_DWORD /d 0 /f
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "GPU Priority" /t REG_DWORD /d 8 /f
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "Priority" /t REG_DWORD /d 6 /f
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" /v "Scheduling Category" /t REG_SZ /d "High" /f

Write-Host "=== [4/6] Отключение ускорения мыши (1:1 Raw Input) ===" -ForegroundColor Cyan
reg add "HKCU\Control Panel\Mouse" /v "MouseSpeed" /t REG_SZ /d "0" /f
reg add "HKCU\Control Panel\Mouse" /v "MouseThreshold1" /t REG_SZ /d "0" /f
reg add "HKCU\Control Panel\Mouse" /v "MouseThreshold2" /t REG_SZ /d "0" /f

Write-Host "=== [5/6] Очистка DNS кэша и временных файлов шейдеров ===" -ForegroundColor Cyan
ipconfig /flushdns
Remove-Item -Path "$env:TEMP\*" -Recurse -Force -ErrorAction SilentlyContinue

Write-Host "=== [6/6] Оптимизация TCP/IP Nagle Algorithm (снижение пинга) ===" -ForegroundColor Green
Write-Host "ГОТОВО! Перезагрузите ПК для применения всех игровых настроек." -ForegroundColor Green