import random
import asyncio
import requests
import json

from PIL import Image
from io import BytesIO
from hash_handler import HashHandler

import discord
from discord.ext import commands

with open('constants.json') as s:
    constants = json.load(s)
client = commands.Bot(command_prefix=constants['prefix'])
token = constants["token"]

@client.event
async def on_ready():
    print(f'{client.user.name} logged in!')

@client.event
async def on_message(message):
    # Checking if the message is from pokebot
    if message.author.id == 365975655608745985:
        with open('constants.json') as s:
            constants = json.load(s)
        
        # Checking if in allowed channel
        if message.channel.id in constants["allowed_channels_ids"]:
            # Checking if there is an image embed in the message
            if message.embeds:
                if 'Guess the' in message.embeds[0].description:
                    url = message.embeds[0].image.url
                    pokemon_name = HashHandler(url).start()

                    await asyncio.sleep(random.randint(1, 5))

                    await message.channel.send("p!catch " + name)
        await client.process_commands(message)

client.run(token,bot=False)