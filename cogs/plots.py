import discord
import matplotlib.pyplot as plt
import os
import numpy as np
from itertools import groupby
from discord.ext import commands

class Graphing(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def plot(self, ctx, xvals, yvals):
    try:
      xList = []
      yList = []
      for varx in xvals:
        xList.append(varx)
      for vary in yvals:
        yList.append(vary)
      newX = ["".join(group) for k, group in groupby(xList, lambda c: c!=' ') if k]
      newY = ["".join(group) for k, group in groupby(yList, lambda c: c!=' ') if k]
      x = np.array(newX).astype(np.float)
      y = np.array(newY).astype(np.float)
      fig, ax = plt.subplots()
      ax.set(xlim=(np.amin(x), np.amax(x)), ylim=(np.amin(y), np.amax(y)))
      ax.plot(x,y)
      ax.set_title(f'{ctx.message.author}\'s Graph')
      fig.savefig('plot.png')
      await ctx.send(file=discord.File('plot.png'))
      await ctx.channel.purge(limit=1)
      ax.cla()
      os.remove('plot.png')
    except ValueError:
      await ctx.send('Either you inputted an invalid number or you didn\'t match the amount of x values and y values.')
  @plot.error
  async def plot_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embed = discord.Embed(title='Plot Command Usage', description='`.plot "x values" "y values"`')
      await ctx.send(embed=embed)
    elif isinstance(error, commands.ExpectedClosingQuoteError):
      await ctx.send('You didn\'t close the quotes properly.')
    else:
      raise error

def setup(client):
  client.add_cog(Graphing(client))