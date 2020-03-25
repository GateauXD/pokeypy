import random
import asyncio
import requests
import json
import imagehash

from PIL import Image
from io import BytesIO

import discord
from discord.ext import commands

class BotHandler(discord.Client):
    async def on_ready(self):
        print("Logged in as :" + self.user)
    
    async def on_message(self, message):
        # Handles check if pokemon appers
        if self.pokeypy.check_message(message):
            await self.pokeypy.get_pokemon_name(message)
            return

        await self.client.process_commands(message)