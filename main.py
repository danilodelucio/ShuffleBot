import discord
import random
import math
from discord.ext import commands
from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound


client = commands.Bot(command_prefix = ">", case_insensitive = True)
activity = discord.Game(name=">help")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='>help'))
    print("ShuffleBot está online!")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, MissingRequiredArgument):
        await ctx.send("Por favor, insira os argumentos necessários! 😬") # Please, send all arguments
    elif isinstance(error, CommandNotFound):
        await ctx.send(f"Desculpe {ctx.author.mention}, eu não conheço este comando! 😅") # Sorry, I don't know this command! Please try again
    else:
        pass

# HELLO MESSAGE
@client.command(help="Só uma simples e educada mensagem de saudações.") # It's a simple and polite greetings message
async def oi(ctx):
 await ctx.send(f"E aí {ctx.author.mention}, vamos embaralhar! 😎") # Hello, let's shuffle

# 2 TEAMS
@client.command(help="Cria 2 times embaralhando vários nomes.") # Make 2 teams shuffling a bunch of names
async def times(ctx, *msg):
    msg_list = list(msg)
    num_list = len(msg)
    str_list = ' '.join(msg_list)

    random.shuffle(msg_list)
    half_value = math.ceil(num_list / 2)

    team01 = ' | '.join(msg_list[:half_value])
    team02 = ' | '.join(msg_list[half_value:])

    embed = discord.Embed(
        title = "ShuffleBot | Times",
        color = 0x0000FF
    )
    embed.add_field(name="TIME-01", value=team01, inline=False)
    embed.add_field(name="TIME-02", value=team02, inline=False)

    await ctx.send(embed=embed)

# SHUFFLE DATA
@client.command(help="Faz uma lista embaralhada com os nomes dados.") # Make a sorted list with all names given
async def embaralhar(ctx, *msg):
    msg_list = list(msg)
    orig_list = ' | '.join(msg_list)

    random.shuffle(msg_list)
    sort_list = ' | '.join(msg_list)

    embed = discord.Embed(
        title = "ShuffleBot | Embaralhar",
        color = 0x0000FF
    )
    embed.add_field(name="Nomes registrados:", value=orig_list, inline=False) # Names registered
    embed.add_field(name="Nomes embaralhados:", value=sort_list, inline=False) # Shuffle data

    await ctx.send(embed=embed)

# START PLAYER
@client.command(help="Seleciona um jogador embaralhando vários nomes.") # Select a player to start the game, shuffling a bunch of names
async def jogador(ctx, *msg):
    msg_list = list(msg)
    names = ' | '.join(msg_list)

    random.shuffle(msg_list)
    player = msg_list[0]

    embed = discord.Embed(
        title = "ShuffleBot | Jogador",
        color = 0x0000FF
    )
    embed.add_field(name="Nomes registrados:", value=names, inline=False)
    embed.add_field(name="Jogador selecionado:", value=player, inline=False)

    await ctx.send(embed=embed)

# CREDITS
@client.command(help="Exibe os créditos sobre essa ferramenta.") # Just show the credits about this tool
async def creditos(ctx):
    embed = discord.Embed(
        title = "ShuffleBot | Créditos",
        description="Obrigado por usar minha humilde ferramenta!", #Thanks for using my simple and humble tool
        color = 0x0000FF
    )
    embed.add_field(name="Desenvolvido por:", value="Danilo de Lucio", inline=False)
    embed.set_footer(text="www.danilodelucio.com")

    await ctx.send(embed=embed)


client.run("")
