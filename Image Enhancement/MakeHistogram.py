from scipy import misc
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
image  = misc.imread('A_adding210',mode="L")#put your path and name of image

# convert image into a array
image = np.asarray(image)
# put pixels in a 1D array by flattening out image array
flat = image.flatten()
# it shows the histogram
plt.hist(flat, bins=100)
plt.savefig("A_adding_210_Histogram.png")#put your path where you want to save and its name 
plt.show()
