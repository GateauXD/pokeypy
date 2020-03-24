import numpy as np
from keras.models import load_model
from PIL import Image

def get_model():
    model = load_model('InceptionV3_Pokemon.h5')
    return model

# Crops images to 160x160x3 for the model's size
def cropImage(url = None):
    size = 160, 160,
    img = Image.open("PokecordSpawn.jpg")
    img.thumbnail(size)
    img = img.convert("RGB")
    img = np.asarray(img, dtype=np.float32) / 255
    img = img[:, :, :3]
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def predict_pokemon(model, image):
    pred = model.predict(image)
    return np.argmax(pred, axis=1).tolist()[0]

image = cropImage()
model = get_model()

print(predict_pokemon(model, image))