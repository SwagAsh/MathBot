import discord
import os
import keep_alive
from discord.ext import commands

cprefix = {}
prefix = ['.']

async def determine_prefix(bot, message):
    guild = message.guild
    if guild:
        return cprefix.get(guild.id, prefix)
    else:
        return prefix

token = os.environ.get("DISCORD_BOT_SECRET")
bot = commands.Bot(command_prefix=determine_prefix)

@bot.command()
@commands.guild_only()
async def setprefix(ctx, *, prefixes=""):
    if prefixes is None:
      await ctx.send("You entered no parameters")
    else:
      cprefix[ctx.guild.id] = prefixes.split() or prefix
      await ctx.send("Prefix set to `" + prefixes + "`")

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