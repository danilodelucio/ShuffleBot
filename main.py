import discord
import random
import math
from discord.ext import commands
from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound
from tabulate import tabulate

client = commands.Bot(command_prefix = "!sb ", case_insensitive = True, help_command=None)
activity = discord.Game(name="!sb help")
color = 0x782396

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='!sb help'))
    print(f"{client.user} está online!")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, MissingRequiredArgument):
        await ctx.send("Por favor, insira os argumentos necessários! 😬") # Please, send all arguments
    elif isinstance(error, CommandNotFound):
        await ctx.send(f"Desculpe {ctx.author.mention}, eu não conheço este comando! 😅") # Sorry, I don't know this command! Please try again
    else:
        pass

# SERVER COUNTS
@client.command()
async def servers(ctx):
    amount = len(client.guilds)
    if amount == 1:
        await ctx.send(f"Este Bot está rodando em {amount} servidor.")
    elif amount > 1:
        await ctx.send(f"Este Bot está rodando em {amount} servidores.")

# HELLO MESSAGE
@client.command(help="Só uma simples e educada mensagem de saudações.") # It's a simple and polite greetings message
async def oi(ctx):
 await ctx.send(f"E aí {ctx.author.mention}, vamos embaralhar! 😎") # Hello, let's shuffle

# 2 TEAMS
@client.command(help="Cria 2 times embaralhando vários nomes.") # Make 2 teams shuffling a bunch of names
async def times(ctx, *msg):
    # CONVERTING TUPLE TO LIST, AND MAKING SUB-LISTS
    msg_list = list(msg)
    msg_sublist = []
    for i in msg_list:
        msg_sublist.append([i])

    # NUMBER LIST
    num_list = len(msg)

    # SHUFFLING THE DATA
    random.shuffle(msg_sublist)

    # FINDING THE HALF VALUE
    half_value = math.ceil(num_list / 2)

    # CREATING TEAMS
    team01 = msg_sublist[:half_value]
    team02 = msg_sublist[half_value:]

    # TABULATING DATA
    team01_tab = tabulate(team01, tablefmt='plain')
    team02_tab = tabulate(team02, tablefmt='plain')

    # CREATING EMBED
    if len(team01) == 1:
        await ctx.send(f"Olá {ctx.author.mention}, não foi possível criar dois times porque é necessário ter pelo menos 3 nomes! 😄")

    elif len(team01) == 0:
        await ctx.send(f"Olá {ctx.author.mention}, não foi possível criar dois times. Por favor insira alguns nomes separados por espaço! 😄")

    else:
        embed = discord.Embed(title = "ShuffleBot | Times", color = color)
        embed.add_field(name="TIME-01", value=f"```\n{team01_tab}\n```", inline=False)
        embed.add_field(name="TIME-02", value=f"```\n{team02_tab}\n```", inline=False)

        await ctx.send(embed=embed)

# SHUFFLE DATA
@client.command(help="Faz uma lista embaralhada com os nomes dados.") # Make a sorted list with all names given
async def embaralhar(ctx, *msg):
    # CONVERTING TUPLE TO LIST, AND MAKING SUB-LISTS
    msg_list = list(msg)
    msg_sublist1 = []
    msg_sublist2 = []
    for i in msg_list:
        msg_sublist1.append([i])
        msg_sublist2.append([i])
    orig_list = tabulate(msg_sublist1, tablefmt="plain")

    # SHUFFLING THE DATA
    random.shuffle(msg_sublist2)
    shuffle_list = tabulate(msg_sublist2, tablefmt="plain")

    embed = discord.Embed(title = "ShuffleBot | Embaralhar", color = color)
    embed.add_field(name="Nomes registrados:", value=f"```\n{orig_list}\n```", inline=False) # Names registered
    embed.add_field(name="Nomes embaralhados:", value=f"```\n{shuffle_list}\n```", inline=False) # Shuffle data

    await ctx.send(embed=embed)

# START PLAYER
@client.command(help="Seleciona um jogador embaralhando vários nomes.") # Select a player to start the game, shuffling a bunch of names
async def jogador(ctx, *msg):
    msg_list = list(msg)
    msg_sublist = [""]
    for i in msg_list:
        msg_sublist.append([i])
    names = tabulate(msg_sublist, tablefmt="plain")

    random.shuffle(msg_list)
    player = msg_list[0]

    embed = discord.Embed(title = "ShuffleBot | Jogador", color = color)
    embed.add_field(name="Nomes registrados:", value=f"```\n{names}\n```", inline=False)
    embed.add_field(name="Jogador selecionado:", value=f"```\n{player}\n```", inline=False)

    await ctx.send(embed=embed)

# CREDITS
@client.command(help="Exibe os créditos sobre essa ferramenta.") # Just show the credits about this tool
async def creditos(ctx):
    embed = discord.Embed(
        title = "ShuffleBot | Créditos",
        description="Obrigado por usar meu humilde Bot! 🤖", #Thanks for using my simple and humble tool
        color = color
    )
    embed.add_field(name="Desenvolvido por:", value="Danilo de Lucio", inline=False)
    embed.set_footer(text="www.danilodelucio.com")

    await ctx.send(embed=embed)

# CUSTOM HELP
@client.command()
async def help(ctx):
    help_list = [["creditos", "- Exibe os créditos sobre essa ferramenta."],
                 ["embaralhar", "- Faz uma lista embaralhada com os nomes dados."],
                 ["jogador", "- Seleciona um jogador embaralhando vários nomes."],
                 ["oi", "- Só uma simples e educada mensagem de saudações."],
                 ["times", "- Cria 2 times embaralhando vários nomes."]]
    help_tab = tabulate(help_list, tablefmt="plain")

    embed = discord.Embed(
        title = "ShuffleBot | Help",
        description='Para utilizar os comandos abaixo, siga o seguinte modelo:\n'
                    '```!sb <comando> <nomes>```\n'
                    'Exemplo:\n'
                    '```!sb times Nome1 Nome2 Nome3...```'
                    '', #Thanks for using my simple and humble tool
        color = color
    )
    embed.add_field(name="Comandos:", value=f"```\n{help_tab}\n```")
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)

    await ctx.send(embed=embed)


client.run("")
