import discord
from discord.ext import commands

from secret import DISCORD_TOKEN

bot = commands.Bot(command_prefix='/')

@bot.command()
async def test(ctx):
    print('サーバーでの発言を検知')
    await ctx.send("がらい杯の時間だああ")

print("bot running...")
bot.run(DISCORD_TOKEN)
