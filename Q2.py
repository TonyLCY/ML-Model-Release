import sys
import math
from PIL import Image

if len(sys.argv) < 2:
    print('Not enough arguments')

filename = sys.argv[1]
im = Image.open(filename)
pixelMap = im.load()

img = Image.new(im.mode, im.size)
pixelsNew = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        c1 = math.floor(pixelMap[i, j][0] / 2)
        c2 = math.floor(pixelMap[i, j][1] / 2)
        c3 = math.floor(pixelMap[i, j][2] / 2)
        pixelsNew[i, j] = (c1, c2, c3)

img.save('Q2.png')
