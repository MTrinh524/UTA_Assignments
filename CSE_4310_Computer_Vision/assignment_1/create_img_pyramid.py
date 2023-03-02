import numpy as np
import skimage.io as io
import skimage.color as color
from skimage import transform
import math
import matplotlib.pyplot as plt

img = io.imread("img/yosemite1.jpg") # reads the specified img file

pyra_height = 4 # the amount of images wanted to be scaled

for loop in range(pyra_height):
    (resize_height, resize_width) = img.shape[0]/pow(2,loop), img.shape[1]/pow(2,loop) # gets new dimensions of the images using a scale factor of n^2
    new_img = transform.resize(img, (resize_height, resize_width), order=0) # resizes the images according to new dimensions using "nearest neighbor interpolation"
    file_name = "yosemite1" # the name of the file I'm using... only appropirate with this specific image

    io.imshow(new_img)
    io.show()
    if loop != 0:
        io.imsave(file_name+"_"+str(pow(2,loop))+"x.jpg", new_img) # saves the newly resized images
