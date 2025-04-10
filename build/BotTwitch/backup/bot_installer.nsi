!define APP_NAME "BotTwitch"
!define INSTALL_DIR "$PROGRAMFILES\${APP_NAME}"
!define EXE_NAME "IniciarBot.bat"

SetCompressor lzma
RequestExecutionLevel admin

Name "${APP_NAME}"
OutFile "Setup_BotTwitch.exe"
InstallDir "${INSTALL_DIR}"
ShowInstDetails show

Section "Instalar"
    SetOutPath "$INSTDIR"
    File /r "bot.py"
    File /r ".env.enc"
    File /r "secret.key"
    File /r "IniciarBot.bat"
    File /r "requirements.txt"
    File /r "README.md"
    File /r "encrypt_env.py"
    File /r "generate_key.py"

    ; Criar atalho na área de trabalho
    CreateShortCut "$DESKTOP\${APP_NAME}.lnk" "$INSTDIR\${EXE_NAME}"
SectionEnd
