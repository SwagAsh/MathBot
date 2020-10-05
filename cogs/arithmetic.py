import discord
from discord.ext import commands

class Arithmetic(commands.Cog):
  def __init__(self, client):
    self.client = client
  
  @commands.command()
  async def add(self, ctx, num1:float, num2:float, *nums:float):
    sum = num1 + num2
    for num in nums:
      sum += num
    strum = str(sum)
    if strum.endswith('.0'):
      await ctx.send(strum[:-2])
    else:
      await ctx.send(strum)
  @add.error
  async def add_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embed = discord.Embed(title='Add Command Usage', description='`.add <num1> <num2> *[nums...]`')
      embed.set_footer(text='Parameters with * in front of it are optional')
      await ctx.send(embed=embed)
    elif isinstance(error, commands.BadArgument):
      await ctx.send('Please input a decimal or an integer value')
    else:
      raise error
  
  @commands.command(aliases = ['sub'])
  async def subtract(self, ctx, num1:float, num2:float, *nums:float):
    dif = num1 - num2
    for num in nums:
      dif -= num
    strif = str(dif)
    if strif.endswith('.0'):
      await ctx.send(strif[:-2])
    else:
      await ctx.send(strif)
  @subtract.error
  async def subtract_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embed = discord.Embed(title='Subtract Command Usage', description='`.subtract <num1> <num2> *[nums...]`')
      embed.set_footer(text='Parameters with * in front of it are optional')
      await ctx.send(embed=embed)
    elif isinstance(error, commands.BadArgument):
      await ctx.send('Please input a decimal or an integer value')
    else:
      raise error

  @commands.command(aliases = ['mult'])
  async def multiply(self, ctx, num1:float, num2:float, *nums:float):
    mult = num1 * num2
    for num in nums:
      mult *= num
    strult = str(mult)
    if strult.endswith('.0'):
      await ctx.send(strult[:-2])
    else:
      await ctx.send(strult)
  @multiply.error
  async def multiply_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embed = discord.Embed(title='Multiply Command Usage', description='`.multiply <num1> <num2> *[nums...]`')
      embed.set_footer(text='Parameters with * in front of it are optional')
      await ctx.send(embed=embed)
    elif isinstance(error, commands.BadArgument):
      await ctx.send('Please input a decimal or an integer value')
    else:
      raise error

  @commands.command(aliases = ['div'])
  async def divide(self, ctx, num1:float, num2:float, *nums:float):
    divid = num1 / num2
    for num in nums:
      divid /= num
    stride = str(divid)
    if stride.endswith('.0'):
      await ctx.send(stride[:-2])
    else:
      await ctx.send(stride)
  @divide.error
  async def divide_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embed = discord.Embed(title='Divide Command Usage', description='`.divide <num1> <num2> *[nums...]`')
      embed.set_footer(text='Parameters with * in front of it are optional')
      await ctx.send(embed=embed)
    elif isinstance(error, commands.BadArgument):
      await ctx.send('Please input a decimal or an integer value')
    else:
      raise error

  @commands.command(aliases=['exp'])
  async def exponent(self, ctx, num1:float, num2:float, *nums:float):
    expen = num1**num2
    for num in nums:
      expen = expen**num
    strexp = str(expen)
    if strexp.endswith('.0'):
      await ctx.send(strexp[:-2])
    else:
      await ctx.send(strexp)
  @exponent.error
  async def exponent_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embed = discord.Embed(title='Exponent Command Usage', description='`.exponent <num1> <num2> *[nums...]`')
      embed.set_footer(text='Parameters with * in front of it are optional')
      await ctx.send(embed=embed)
    elif isinstance(error, commands.BadArgument):
      await ctx.send('Please input a decimal or an integer value')
    else:
      raise error

def setup(client):
  client.add_cog(Arithmetic(client))