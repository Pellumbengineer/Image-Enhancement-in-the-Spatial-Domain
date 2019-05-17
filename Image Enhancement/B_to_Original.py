import scipy.misc
import math
import scipy.ndimage
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

src = Image.open("B.tif").convert('L')

b = scipy.ndimage.filters.median_filter(src , size = 3 , footprint = None , mode = 'reflect',
output = None , cval = 0.0 , origin = 0)

# we apply the histogram equalization
dst = cv2.equalizeHist(b)

# construct a sharpening filter
kernel = np.array((
	               [0, -1, 0] ,
	               [-1, 5, -1],
	               [0, -1, 0]), dtype="int")

# applying the sharpening kernel to the input image and displaying it.
sharpened = cv2.filter2D(dst, -1, kernel)

dst = scipy.misc.toimage(dst)
dst.save("B_median_histeq.tif")
plt.imshow(dst)
plt.show()

a = scipy.misc.toimage(sharpened)
a.save("B_median_histeq_sharpened.tif")
plt.imshow(sharpened)
plt.show()
