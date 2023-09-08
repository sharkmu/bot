import discord
from discord.ext import commands
import requests
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

TOKEN = os.getenv('TOKEN')

@bot.command()
async def ping(ctx):
    await ctx.send('BOT ping: {} ms'.format(round(bot.latency * 1000)))

bot.run(TOKEN)