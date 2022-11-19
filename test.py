import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

from nltk_teste import Nltk as nl


nl_instance = nl()
nl_instance.calc()


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)

@client.event
async def on_member_join(member):
    response = 'mais um bobão entrou no chat'
    await message.channel.send(response)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    response = nl_instance.receive(message.content)
    await message.channel.send(response)
    
client.run(TOKEN)
