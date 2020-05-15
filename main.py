import discord
import os
import flask
import keep_alive
from discord.ext import commands

token = os.environ.get("DISCORD_BOT_SECRET")
bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
  act = discord.Activity(name='Math Help', type=discord.ActivityType.watching)
  await bot.change_presence(activity=act)
  print(f'MathBot ready: logged in {bot}')

@bot.command(hidden=True)
async def load(ctx, extension):
  bot.load_extension(f'cogs.{extension}')

@bot.command(hidden=True)
async def unload(ctx, extension):
  bot.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'cogs.{filename[:-3]}')

keep_alive.keep_alive()

bot.run(token)