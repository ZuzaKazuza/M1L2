import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

from bot_logic import gen_pass
from bot_logic import flip_coin

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def password(ctx):
    await ctx.send(f'gen_pass(7)')

@bot.command()
async def FlipCoin(ctx):   
    await ctx.send(f'FlipCoin')                    
   

bot.run("")
