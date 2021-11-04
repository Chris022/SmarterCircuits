import numpy
from PIL import Image

#create an independent copy of a numpy array
def createIndependetCopy(img):
    newImg = numpy.empty_like(img)
    newImg[:] = img
    return newImg

#turns an image with first x than y cooridates into an image with first y than x and the other way around
def flipImage(image):
    image = createIndependetCopy(image)
    return numpy.transpose(image)

# Function that loads an black and white image and changes the color values so that 0 is white and 1 is black
# Output Image is a array with first index X and second index Y coorodiante
def load1BitBWImage(path,name):
    image = Image.open('{path}/{name}'.format(path=path,name=name)).convert('L')
    testData = (255 - numpy.asarray(image))/255
    return testData

# Function that loads an rgb image and changes the color values
# Output Image is a array with first index X and second index Y coorodiante
def loadRGBImage(path,name):
    image = Image.open('{path}/{name}'.format(path=path,name=name))
    testData = numpy.asarray(image)
    return createIndependetCopy(testData)
