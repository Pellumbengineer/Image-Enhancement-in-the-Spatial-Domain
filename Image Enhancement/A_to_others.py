import cv2 as cv
import scipy.misc
from PIL import Image
import numpy as np
import math
import matplotlib.pyplot as plt


im = Image.open('A.tif') # Can be many different formats.
pix = im.load()
width, height = im.size
for x in range(width):
    for y in range(height):
        pix[x,y]=255-pix[x,y]

im.show()

im = Image.open('A.tif') # Can be many different formats.
pix = im.load()
width, height = im.size
print(width,height)

for x in range(width):
    for y in range(height):

        pix[x,y]=int(210 + pix[x,y]/6)

im.show()


im = Image.open('A.tif').convert("L") # Can be many different formats.
a = np.asarray(im)
dst = cv.equalizeHist(a)
dst = scipy.misc.toimage(dst)
dst.show()
