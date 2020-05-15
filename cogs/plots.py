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

  @commands.group(invoke_without_command=True, aliases = ['pline'])
  async def plotline(self, ctx):
    await ctx.send('Plot a Line:\n.plotline si <slope> <y-intercept>\n.plotline st <xcoef> <ycoef> <const>')
  @plotline.command(aliases = ['slopeintercept'])
  async def si(self, ctx, slope, yint):
    m = float(slope)
    b = float(yint)
    x = np.linspace(-10, 10, 100)
    y = m*x+b
    fig, ax = plt.subplots()
    ax.set(xlim=(-10, 10), ylim=(-10, 10))
    xax = [-10, 10]
    yax = [0, 0]
    xyax = [0, 0]
    yyax = [-10, 10]
    ax.plot(xax, yax, color='black')
    ax.plot(xyax, yyax, color='black')
    ax.plot(x,y)
    ax.plot()
    ax.set_title(f'{ctx.message.author}\'s Line')
    ax.set_xlabel('X-Axis')
    ax.set_ylabel('Y-Axis')
    ax.grid()
    fig.savefig('line.png')
    await ctx.send(file=discord.File('line.png'))
    ax.cla()
    os.remove('line.png')
  @si.error
  async def si_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embed=discord.Embed(title='Slope-Intercept Plot command usage:', description='`.plotline si <slope> <y-intercept>`')
      await ctx.send(embed=embed)
    else:
      raise error
  @plotline.command(aliases = ['standard'])
  async def st(self, ctx, xcoef, ycoef, const):
    xcoefficient = float(xcoef)
    ycoefficient = float(ycoef)
    constant = float(const)
    slope = -xcoefficient/ycoefficient
    yintercept = constant/ycoefficient
    x = np.linspace(-10, 10, 100)
    y = slope*x+yintercept
    fig, ax = plt.subplots()
    ax.set(xlim=(-10, 10), ylim=(-10, 10))
    xax = [-10, 10]
    yax = [0, 0]
    xyax = [0, 0]
    yyax = [-10, 10]
    ax.plot(xax, yax, color='black')
    ax.plot(xyax, yyax, color='black')
    ax.plot(x,y)
    ax.plot()
    ax.set_title(f'{ctx.message.author}\'s Line')
    ax.set_xlabel('X-Axis')
    ax.set_ylabel('Y-Axis')
    ax.grid()
    fig.savefig('line.png')
    await ctx.send(file=discord.File('line.png'))
    ax.cla()
    os.remove('line.png')
  @st.error
  async def st_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embed=discord.Embed(title='Standard Form Plot command usage:', description='`.plotline st <xcoefficient> <ycoefficient> <constant>`')
      await ctx.send(embed=embed)
    else:
      raise error

def setup(client):
  client.add_cog(Graphing(client))