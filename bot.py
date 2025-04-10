import os
import requests
from twitchio.ext import commands
from cryptography.fernet import Fernet

# Carregar a chave secreta
with open("secret.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

# Ler e descriptografar o conteúdo do .env.enc
with open(".env.enc", "rb") as encrypted_file:
    decrypted = fernet.decrypt(encrypted_file.read()).decode()

# Transformar linhas em variáveis de ambiente
for line in decrypted.strip().splitlines():
    if line and not line.startswith("#"):
        key, value = line.split("=", 1)
        os.environ[key.strip()] = value.strip()

# Acessar normalmente
TOKEN = os.getenv("TOKEN")
CANAL = os.getenv("CANAL")

bot = commands.Bot(
    token=TOKEN,
    prefix='!',
    initial_channels=[CANAL]
)

# Função para buscar o appid do jogo
def buscar_appid(nome_jogo):
    url = f"https://steamcommunity.com/actions/SearchApps/{nome_jogo}"
    response = requests.get(url)
    if response.status_code == 200:
        resultados = response.json()
        if resultados:
            return resultados[0]["appid"]
    return None

# Função para buscar o nome, preço e link do jogo
def buscar_info_steam(appid):
    url = f"https://store.steampowered.com/api/appdetails?appids={appid}&cc=br&l=portuguese"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data and str(appid) in data and data[str(appid)]["success"]:
            jogo = data[str(appid)]["data"]
            nome = jogo["name"]
            preco = "Gratuito"
            if "price_overview" in jogo:
                valor = jogo["price_overview"]["final"] / 100
                preco = f"R$ {valor:.2f}"
            link = f"https://store.steampowered.com/app/{appid}"
            return f"{nome} - {preco} - {link}"
    return "Jogo não encontrado ou sem informações disponíveis."

# trocando para !game
@bot.command(name="game")
async def game(ctx):
    nome_jogo = ctx.message.content.replace("!game", "").strip()
    if not nome_jogo:
        await ctx.send("Use o comando assim: !game nome_do_jogo")
        return

    appid = buscar_appid(nome_jogo)
    if not appid:
        await ctx.send("Jogo não encontrado na Steam.")
        return

    info = buscar_info_steam(appid)
    await ctx.send(info)

@bot.event
async def event_ready():
    print(f"✅ Bot conectado como {bot.nick}")

bot.run()
