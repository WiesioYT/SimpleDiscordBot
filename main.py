import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
  print(f'We have logged in as {bot.user}')


@bot.event
async def on_message(message):
  print('on_message')
  if message.author == bot.user:
    return
  if message.content.startswith('Hello'):
    await message.channel.send('Hello!')

  await bot.process_commands(message)


@bot.command()
async def ping(ctx):
  try:
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')
  except Exception as e:
    print(e)


bot.run(
    'MTE2NjQ3NjU5Njg3ODc3MDI0Ng.GW-iBo.ngxCGDrPT4utIqZobhSOEb2qF_TjPAlb-P6nyU')
