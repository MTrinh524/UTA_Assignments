import numpy as np
import skimage.io as io
import skimage.color as color
from skimage import transform
import sys
import matplotlib.pyplot as plt

def RGBtoHSV(img):
    # Normalizing the RGB numpy array and storing them into specific RGB for computation later
    img = img/255.0
    R = img[:, :, 0]
    G = img[:, :, 1]
    B = img[:, :, 2]

    value = np.max(img, axis=2) # Computes value in HSV
    chroma = value - np.min(img, axis=2) # Computes chroma to be used to find the saturation in HSV later
    # Computes saturation in HSV
    if(value == 0).all():
        sat = 0
    else:
        sat = chroma/value

    # Calculates the angle of the hue hexagon that corresponds to a specific color
    hue_prime = chroma > 0
    if(chroma == 0).all():
        hue_prime = 0
    elif(value == R).all():
        hue_prime = ((G-B)/chroma)%6
    elif(value == G).all():
        hue_prime = ((B-R)/chroma)+2
    elif(value == B).all():
        hue_prime = ((R-G)/chroma)+4
    
    # Calculates the actual value of hue within the ranges of [0,360] given the angle
    hue = 60*hue_prime

    # Stores the HSV back into the Numpy representations of RGB
    img[:, :, 0] = hue
    img[:, :, 1] = sat
    img[:, :, 2] = value

    return img

def HSVtoRGB(img, hue, sat, value):
    # Storing the hsv values from the argument into the image array
    img[:, :, 0] = img[:, :, 0] + hue
    img[:, :, 1] = img[:, :, 1] + sat
    img[:, :, 2] = img[:, :, 2] + value
    h = img[:, :, 0]
    s = img[:, :, 1]
    v = img[:, :, 2] 

    c = v*s # chroma
    hue_prime = h/60.0 # normalizing hue
    X = c * (1-np.abs(hue_prime % 2 - 1)) # second largest component of the color
    m = v-c # difference of chroma from value

    # Calculates the RGB values
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

# /////Main/////

img = io.imread("img/yosemite1.jpg") # reads the specified img file

# Stores the command line arguments into its corresponding representation
filename = str(sys.argv[0])
hue = float(sys.argv[1])
sat = float(sys.argv[2])
value = float(sys.argv[3])
# Gives an error whenever the saturation and value values are not within the specified ranges and exits the program
if not 0<=sat<=1 or not 0<=value<=1:
    print("WARNING: Either saturation and/or value is not within the range [0,1]")
    exit()

# Convert to RGB from RGBA (if applicable)
if img.ndim == 3 and img.shape[2] == 4:
    img = color.rgba2rgb(img)

# Displays the original image
io.imshow(img)
io.show()

# Convert from RGB to HSV
HSV_img = RGBtoHSV(img)
io.imshow(HSV_img)
io.show()
io.imsave("color_spaces1.jpg", HSV_img)

# Convert from HSV (given arguments) to RGB
RGB_img = HSVtoRGB(img, hue, sat, value)
io.imshow(RGB_img)
io.show()
io.imsave("color_spaces2.jpg", RGB_img)