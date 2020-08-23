import random, string
import discord
from discord.ext import commands
from termcolor import colored
from colorama import init
from colorama import Fore, Back, Style

init()
title = ('𝙉𝙞𝙩𝙧𝙤')
embed=discord.Embed(title="𝙉𝙞𝙩𝙧𝙤", color=0x000001)
embed.set_thumbnail(url="https://zupimages.net/up/20/14/5an2.gif")
embed.add_field(name="𝙉𝙞𝙩𝙧𝙤 𝙂𝙚𝙣𝙚𝙧𝙖𝙩𝙤𝙧", value="𝘾𝙤𝙙𝙚𝙙 𝙗𝙮 𝙉𝙞𝙜𝙝𝙩𝙮#1560", inline=False)
bot = commands.Bot(command_prefix='!')
@bot.event
async def on_ready():
    print('[LOGS]' + Fore.LIGHTGREEN_EX + ' Nitro est en ligne\n' + Fore.RESET)
    await bot.change_presence(status=discord.Status.idle,
            activity=discord.Game('𝙉𝙞𝙜𝙝𝙩𝙮#1560'))
@bot.command()
async def info(ctx):
    await ctx.send(embed=embed)
    print(Fore.LIGHTMAGENTA_EX + 'Info  Generated' + Fore.RESET)
@bot.command()
async def nitro(ctx):
    nitro = 'https://discordapp.com/gifts/%s' % (('').join(random.choices(string.ascii_letters + string.digits, k=16)))
    nitro1 = nitro
    nitro2 = nitro1
    await ctx.send(nitro2)
    print(Fore.LIGHTCYAN_EX + 'Nitro Generated' + Fore.RESET)
@bot.command()
async def nitroinfinite(ctx):
    while True:
        nitro = 'https://discordapp.com/gifts/%s' % (('').join(random.choices(string.ascii_letters + string.digits, k=16)))
        nitro1 = nitro
        nitro2 = nitro1
        await ctx.send(nitro2)
        print(Fore.LIGHTCYAN_EX + 'Nitro Generated' + Fore.RESET)
    
bot.run('NzQ3MTI2NDE3MTkxNjAwMTc4.X0KVsg.jHcb5so7H9TkJBDqcgB0rSHKkWg')