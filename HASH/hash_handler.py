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
    
    def get_image(self):
        image_url = requests.get(self.url)
        self.image = Image.open(BytesIO(image_url.content))

    def hash_image(self):
        self.hash = str(imagehash.dhash(self.image))
    
    def get_pokemon_name(self):
        self.pokemon_name = self.pokemon_json[self.hash]
        print("The pokemon name is: " + self.pokemon_name)

    def start(self):
        self.get_image()
        self.hash_image()
        self.get_pokemon_name()
        return self.pokemon_name
    
