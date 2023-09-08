import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

# removes default help command
bot.remove_command('help')

TOKEN = os.getenv('TOKEN')

website = "https://www.google.com/"

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='made by: 1814sam'))

@bot.command()
async def ping(ctx):
    await ctx.send('BOT ping: {} ms'.format(round(bot.latency * 1000)))

@bot.command()
async def help(ctx):
    user = ctx.message.author
    await user.send(f"Here is our website for more information: {website}")
    await ctx.reply('I sent you a DM!', mention_author=True)

bot.run(TOKEN)