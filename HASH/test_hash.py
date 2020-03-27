import imagehash
import requests

from PIL import Image
from io import BytesIO

url = "https://cdn.discordapp.com/attachments/692073641021800552/692889127934230628/PokecordSpawn.jpg"
image_url = requests.get(url)
image = Image.open(BytesIO(image_url.content))
print(str(imagehash.dhash(image, 16)))