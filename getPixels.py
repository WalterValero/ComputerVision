from numpy import array
from PIL import Image

#get pixels from image

def getPixels(image):
    imagePixels = Image.open(image)
    pixels = array(imagePixels)
    return pixels
