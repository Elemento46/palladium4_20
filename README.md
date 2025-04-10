# 🎮 BotTwitch

**BotTwitch** é um bot de chat para Twitch desenvolvido em Python, capaz de buscar e exibir **nome, preço e link de jogos da Steam** diretamente no chat da live com o comando `!game`.

![Badge Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Badge TwitchIO](https://img.shields.io/badge/TwitchIO-2.7-purple)
![Badge License](https://img.shields.io/badge/license-MIT-green)
![Badge Status](https://img.shields.io/badge/status-Em%20desenvolvimento-yellow)

---

## 🧠 Funcionalidades

- ✅ Comando `!game nome_do_jogo`
- 🔎 Busca de AppID na Steam
- 💸 Consulta de preço atual e link direto da loja
- 🔐 Uso de `.env.enc` e `secret.key` para proteção de tokens
- 🖱️ Executável `.exe` com instalador e atalho na área de trabalho

---

## 🚀 Instalação

### 📦 Instalar com o `.exe` (recomendado)

> Vá para a aba [**Releases**](../../releases) e baixe a versão mais recente.

1. Execute `Setup_BotTwitch.exe`
2. O bot será instalado em `C:\BotTwitch`
3. Use o atalho criado na área de trabalho

---

### 🧪 Instalação manual (modo desenvolvedor)

```bash
git clone https://github.com/seu-usuario/BotTwitch.git
cd BotTwitch
pip install -r requirements.txt
python bot.py
