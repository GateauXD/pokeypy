import imagehash
import random
import json
import requests
import os

from io import BytesIO
from PIL import Image

class HashHandler():
    def __init__(self, url):
        self.url = url
        
        with open('pokemon-hash.json') as f:
            self.pokemon_json = json.load(f)
    
    def get_pokemon_name(self):
        image_url = requests.get(self.url)
        self.image = Image.open(BytesIO(image_url.content))
        self.hash = str(imagehash.dhash(self.image))
        self.pokemon_name = self.pokemon_json[self.hash]
        print("The pokemon name is: " + self.pokemon_name)

        return self.pokemon_name
    
