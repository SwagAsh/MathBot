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
      ax.plot(x,y,marker='o')
      ax.set_title(f'{ctx.message.author}\'s Graph')
      fig.savefig('plot.png')
      await ctx.send(file=discord.File('plot.png'))
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
    ax.set(xlim=(-10, 10), ylim=(b-10, b+10))
    plt.axhline(y=0, color='black', linestyle='-')
    plt.axvline(x=0, color='black', linestyle='-')
    ax.plot(x,y)
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
    ax.set(xlim=(-10, 10), ylim=(yintercept-10, yintercept+10))
    plt.axhline(y=0, color='black', linestyle='-')
    plt.axvline(x=0, color='black', linestyle='-')
    ax.plot(x,y)
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
  @commands.group(invoke_without_command=True)
  async def plotquad(self, ctx):
    await ctx.send("Plotting Quadratics:\n.plotquad vf <coefficient> <xcoordinate> <ycoordinate>\n.plotquad st <coefficient1> <coefficient2> <constant>")
  @plotquad.command(aliases = ['vertexform'])
  async def vf(self, ctx, coeff, xcoord, ycoord):
    a = float(coeff)
    h = float(xcoord)
    k = float(ycoord)
    x = np.linspace(h-10, h+10, 100)
    y = a*(x-h)**2 + k
    fig, ax = plt.subplots()
    ax.set(xlim=(h-10, h+10), ylim=(k-10, k+10))
    plt.axhline(y=0, color='black', linestyle='-')
    plt.axvline(x=0, color='black', linestyle='-')
    ax.plot(x,y)
    ax.set_title(f'{ctx.message.author}\'s Quadratic')
    ax.set_xlabel('X-Axis')
    ax.set_ylabel('Y-Axis')
    ax.grid()
    fig.savefig('quad.png')
    await ctx.send(file=discord.File('quad.png'))
    ax.cla()
    os.remove('quad.png')
  @plotquad.command(aliases = ['standardform'])
  async def st(self, ctx, acoef, bcoef, ccoef):
    a = float(acoef)
    b = float(bcoef)
    c = float(ccoef)
    d = b**2 - 4*a*c
    x = np.linspace((-b/2*a) - 50, (-b/2*a) + 50, 500)
    y = a*x**2+b*x+c
    fig, ax = plt.subplots()
    ax.set(xlim=(-b/(2*a) - 10, -b/(2*a) + 10), ylim=(-d/(4*a)-10, -d/(4*a)+10))
    plt.axhline(y=0, color='black', linestyle='-')
    plt.axvline(x=0, color='black', linestyle='-')
    ax.plot(x,y)
    ax.set_title(f'{ctx.message.author}\'s Quadratic')
    ax.set_xlabel('X-Axis')
    ax.set_ylabel('Y-Axis')
    ax.grid()
    fig.savefig('quads.png')
    await ctx.send(file=discord.File('quads.png'))
    ax.cla()
    os.remove('quads.png')


def setup(client):
  client.add_cog(Graphing(client))