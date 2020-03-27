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
        
        with open("caught_pokemon.json") as j:
            self.caught_json = json.load(j)
        
        with open('constants.json') as s:
            self.constants = json.load(s)
    
    def get_pokemon_name(self):
        try:
            image_url = requests.get(self.url)
            self.image = Image.open(BytesIO(image_url.content))
            self.hash = str(imagehash.dhash(self.image, 16))
            self.pokemon_name = self.pokemon_json[self.hash]
            print("The pokemon name is: " + self.pokemon_name)
        except:
            # TODO add a image hashing function here and add it to the json
            print("Image has not been hashed")
            return None
        
        # Checking if pokemon has already caught
        if self.pokemon_name in self.caught_json["list"] or self.constants["catch"] == False:
            return None
        else:
            self.caught_json["list"].append(self.pokemon_name)
            with open("caught_pokemon.json", 'w') as override_json:
                json.dump(self.caught_json, override_json)
            return self.pokemon_name
    
