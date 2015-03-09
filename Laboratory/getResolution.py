from PIL import Image

#get resolution from a image width x high

def getResolution(imageName):
    image = Image.open(imageName)
    return image.size

nameFile = "example.png"
print getResolution(nameFile)

