@echo off
cd /d "%~dp0"

:: Verifica se o executável existe
if exist "dist\BotTwitch.exe" (
    start dist\BotTwitch.exe
) else (
    echo Executável não encontrado. Certifique-se de que BotTwitch.exe está na pasta dist.
    pause
)
