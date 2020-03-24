import requests
import numpy as np
from keras.models import load_model
from PIL import Image
from io import BytesIO

def get_model():
    model = load_model('InceptionV3_Pokemon.h5')
    return model

def get_image(url = None):
    url = "https://cdn.discordapp.com/attachments/690877083714322457/692125751667064912/PokecordSpawn.jpg"
    response = requests.get(url)
    response_img = Image.open(BytesIO(response.content))
    return response_img

# Crops images to 160x160x3 for the model's size
def crop_image(this_image):
    img = this_image.resize((160, 160))
    img_array = np.array(img)
    img_array = img_array[...,:3]
    img = Image.fromarray(img_array)
    img.show()
    return img_array

def predict_pokemon(model, image):
    pred = model.predict(image)
    return np.argmax(pred, axis=1).tolist()[0]

image = get_image()
img_array = crop_image(image)
model = get_model()
print(predict_pokemon(model, img_array))