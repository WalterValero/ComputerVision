from numpy import array
from PIL import Image

#get pixels from image

def getPixels(imageName):
    imagePixels = Image.open(imageName)
    pixels = array(imagePixels)
    return pixels

nameFile = "example.png"
print getPixels(nameFile)
