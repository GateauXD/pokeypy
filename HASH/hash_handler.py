import imagehash
import random
import json
import requests
import os

class HashHandler():
    def __init__(self, url):
        self.url = url
        
        with open('pokemon-hash.json') as f:
            self.pokemon_json = json.load(f)
    
    def get_image(self):
        self.image = requests.get(self.url)

    def hash_image(self):
        self.hash = str(imagehash.dhash(image))
    
    def get_pokemon_name(self):
        try:
            self.pokemon_name = self.pokemon_json[self.hash]
            print("The pokemon name is: " + self.pokemon_name)
        except:
            "The hash could not be found"

    def start(self):
        self.get_image()
        self.hash_image()
        self.get_pokemon_name()
        return self.pokemon_name
    
