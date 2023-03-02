import numpy as np
import skimage.io as io
import skimage.color as color
from skimage import transform
import sys
import matplotlib.pyplot as plt
from numpy.lib import stride_tricks

def random_crop(img, size):
    height, width = img.shape[0], img.shape[1]

    # Check to see if the crop size is feasible given the imput image size
    if(size not in range(0, min(width, height))):
        print("WARNING: The crop size chosen is not feasbile with the input image size")
        exit()

    # The furthest the row and column that can be accessed accround to the size
    right_col = width-size
    bot_row = height-size

    # Gets the random left-most column and top_most row
    left_col = np.random.randint(0, right_col)
    top_row = np.random.randint(0, bot_row)

    # crops the image
    crop_image = img[top_row : top_row + size, left_col : left_col + size]

    return crop_image

def extract_patch(img, num_patches):
    height, width = img.shape[0], img.shape[1] # height and width of image
    rows, cols = height // num_patches, width // num_patches # gets the amount of rows and columns needed for the patches
    patches = np.zeros((rows, cols, num_patches, num_patches)) # placeholder to store the patches later

    # Creates the patches for the given image
    for x in range(rows):
        for y in range(cols):
            patches = img[num_patches*x:num_patches*(x+1), num_patches*y:num_patches*(y+1)]

    return patches

def resize_img(img, factor):
    (resize_width, resize_height) = img.shape[0]/factor, img.shape[1]/factor # gets the new width and heights given the inputted scale factor
    new_img = transform.resize(img, (resize_height, resize_width), order=0) # resizes the image to given dimensions using "nearest neighbor interpolation"

    return new_img

def color_jitter(img, hue, saturation, value):
    # getting random values less than or equal to the hsv given
    h = np.random.randint(0, hue)
    s = np.random.uniform(0, saturation)
    v = np.random.uniform(0, value)

    # storing the hsv values into the given image array
    img[:, :, 0] = img[:, :, 0] + h
    img[:, :, 1] = img[:, :, 1] + s
    img[:, :, 2] = img[:, :, 2] + v
    h = img[:, :, 0]
    s = img[:, :, 1]
    v = img[:, :, 2] 

    c = v*s # chroma
    hue_prime = h/60.0 # normalizing hue
    X = c * (1-np.abs(hue_prime % 2 - 1)) # second largest component of the color
    m = v-c # difference of chroma from value

    # Calculates the conversion of HSV to RGB
    R_prime, G_prime, B_prime = 0,0,0
    for i in range(len(img)):
        for j in range(len(img[i])):
            if(hue_prime[i,j] >= 0 and hue_prime[i,j] < 1):
                (R_prime, G_prime, B_prime) = (c[i,j], X[i,j], 0)
            elif(hue_prime[i,j] >= 1 and hue_prime[i,j] < 2):
                (R_prime, G_prime, B_prime) = (X[i,j], c[i,j], 0)
            elif(hue_prime[i,j] >= 2 and hue_prime[i,j] < 3):
                (R_prime, G_prime, B_prime) = (0, X[i,j], c[i,j])
            elif(hue_prime[i,j] >= 3 and hue_prime[i,j] < 4):
                (R_prime, G_prime, B_prime) = (0, X[i,j], c[i,j])
            elif(hue_prime[i,j] >= 4 and hue_prime[i,j] < 5):
                (R_prime, G_prime, B_prime) = (X[i,j], 0, c[i,j])
            elif(hue_prime[i,j] >= 5 and hue_prime[i,j] < 6):
                (R_prime, G_prime, B_prime) = (c[i,j], 0, X[i,j])

            img[i,j,0] = float(R_prime) + float(m[i,j])
            img[i,j,1] = float(G_prime) + float(m[i,j])
            img[i,j,2] = float(B_prime) + float(m[i,j])
    
    return img

# Main

img = io.imread("img/yosemite1.jpg") # reads the specified img file

# Displays the original image
io.imshow(img)
io.show()

# Displays the specified size random cropping of the image
size = 120
crop_img = random_crop(img, size)
io.imshow(crop_img)
io.show()

# Displays the image after performing patch extraction
num_patches = 8
# Reusing Cropped image from earlier since it is a square image
patches_img = extract_patch(crop_img, num_patches)
io.imshow(patches_img)
io.show()

# Displays the newly resized image based off scaling factor
factor = 4
resized_img = resize_img(img, factor)
io.imshow(resized_img)
io.show()

# Randomly perturbs the HSV values on an input image
hue = 360
saturation = 1
value = 1
color_jitter_img = color_jitter(img, hue, saturation, value)
io.imshow(color_jitter_img)
io.show()