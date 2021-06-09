import os
import random

import discord
from discord.ext import commands

if os.path.exists('secret.py'):
    from secret import DISCORD_TOKEN
else:
    DISCORD_TOKEN = os.environ['DISCORD_TOKEN']

bot = commands.Bot(command_prefix='/')

@bot.command()
async def test(ctx):
    await ctx.send("がらい杯の時間だああ")

@bot.command()
async def faz(ctx):
    words = 'ふぁずぱい'
    s = ''
    for i in range(5):
        r = random.randrange(5)
        s += words[i]
    await ctx.send(s)
    

print("bot running...")
bot.run(DISCORD_TOKEN)
