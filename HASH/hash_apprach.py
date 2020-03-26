import string
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
    with open('constants.json') as s:
        constants = json.load(s)

    print(f'{client.user.name} logged in!')
    channel = client.get_channel(constants["allowed_channels_ids"][0])
    while True:
        letters = string.ascii_lowercase
        spam_text = ''.join(random.choice(letters) for i in range(random.randint(5,20)))
        await channel.send(spam_text)
        await asyncio.sleep(random.uniform(0,2))

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
                    pokemon_name = HashHandler(url).get_pokemon_name()

                    if pokemon_name != None:
                        await asyncio.sleep(random.randint(1,3))
                        await message.channel.send("p!catch " + pokemon_name)
                    else:
                        print("We already have " + pokemon_name)    
        await client.process_commands(message)

client.run(token,bot=False)