import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

from nltk_teste import Nltk as nl
from bot import Bot
from env import Env


nl_instance = nl()
nl_instance.calc()

TOKEN = Env.get_env('DISCORD_TOKEN')
COMMAND_PREFIX = Env.get_env('COMMAND_PREFIX')


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=COMMAND_PREFIX,intents=intents)

@bot.command('start')
async def start(ctx):
    Bot.start()
    await ctx.send("Hi Sir ! Rogério Rocambot reporting to duty !")

@bot.command('stop')
async def stop(ctx):
    Bot.stop()
    await ctx.send("See you soon !")


@bot.event
async def on_ready():
    return 

@bot.event
async def on_member_join(member):
    response = 'mais um bobão entrou no chat'
    await message.channel.send(response)

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    
    if (Bot.is_command(bot.commands,message.content)):
        return 
    
    if not(Bot.is_turned_on()):
        return

    if message.author == bot.user:
        return

    response = nl_instance.receive(message.content)
    await message.channel.send(response)
    
bot.run(TOKEN)
