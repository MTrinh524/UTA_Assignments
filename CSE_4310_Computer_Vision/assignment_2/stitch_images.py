import matplotlib.pyplot as plt
import numpy as np
from skimage import io
from skimage.measure import ransac
# from skimage import measure
from skimage.color import rgb2gray, rgba2rgb
from skimage.feature import match_descriptors, plot_matches, SIFT
import math
from copy import copy
import random

# Performs keypoint matching of 2 images using a brute force method
def kp_matching(kp1, kp2, d1, d2):

    matching_pairs = []
    threshold = 0.8

    for i in range(len(kp1)):
        closest_index = 0 # used to store the nearest index
        closest_match_dist = float('inf') # used to comapre if the distance is less than this
        for j in range(len(kp2)):
            distance = math.dist(d1[i], d2[j]) # euclidean distance calculation
            if distance < closest_match_dist:
                second_closest_match_dist = closest_match_dist # sets the second nearest distance
                closest_match_dist = distance # sets nearest distance
                closest_index = j # sets the nearest index
        ratio = closest_match_dist / second_closest_match_dist
        if ratio < threshold:
            print(tuple((i, closest_index)))
            matching_pairs.append(tuple((i, closest_index))) # gets the index of of mathing points

    np_matching_pairs = np.array(matching_pairs) # converts to an appropriate 2D array

    return np_matching_pairs

# plots the keypoints detected in each image
def plot_kp_matches(img1, img2, kp1, kp2, matches):
    fig, ax = plt.subplots()
    plot_matches(ax, img1, img2, kp1, kp2, matches)
    ax.axis('off')
    plt.show()

# computes the estimated affined transformation matrix
def compute_affine_transform(src, dst):

    # Placeholders for when the transformation matrix and the destination keypoints are vectorized
    A = np.zeros((len(src)*2, 6))
    b = np.zeros((len(dst)*2, 1))

    count = 0

    # Computes the values for matrix A
    for x in range(len(src)):
        A[count] = np.array([src[x][0], src[x][1], 1, 0, 0, 0])
        A[count+1] = np.array([0, 0, 0, src[x][0], src[x][1], 1])
        count += 2

    count = 0
    # computes the values for column vector b
    for x in range(len(dst)):
        b[count] = np.array([dst[x][0]])
        b[count+1] = np.array([dst[x][1]])
        count += 2

    # computes to get the affine matrix
    ATA = np.linalg.inv(np.dot(A.transpose(), A)) # gets the inverse of A^TA
    ATAAT = np.dot(ATA, A.transpose())
    tform = np.dot(ATAAT, b)

    tform = tform.reshape(2, 3)
    tform = np.concatenate((tform, np.array([[0, 0, 1]])))

    print("Affine Transformation Matrix")
    print(tform)

    return tform

# computes the estimated projective transformation matrix
def compute_projective_transform(src, dst):

    A = np.zeros((len(src)*2, 8))
    b = np.zeros((len(dst)*2, 1))

    count = 0

    for x in range(len(src)):
        A[count] = np.array([src[x][0], src[x][1], 1, 0, 0, 0, -(src[x][0]*dst[x][0]), -(src[x][1]*dst[x][0])])
        A[count+1] = np.array([0, 0, 0, src[x][0], src[x][1], 1, -(src[x][0]*dst[x][1]), -(src[x][1]*src[x][1])])
        count += 2

    count = 0

    for x in range(len(dst)):
        b[count] = np.array([dst[x][0]])
        b[count+1] = np.array([dst[x][1]])
        count += 2

    ATA = np.linalg.inv(np.dot(A.transpose(), A)) # gets the inverse of A^TA
    ATAAT = np.dot(ATA, A.transpose())
    tform = np.dot(ATAAT, b)

    tform = np.concatenate((tform, np.array([[1]])))
    tform = tform.reshape(3, 3)

    print("Projective Transformation Matrix")
    print(tform)

    return tform

def ransac(data, min_samples, residual_threshold, max_trials):

    iterations = 0
    model = compute_affine_transform # sets the transformation matrix function
    bestFit = None
    bestErr = float('inf')

    # print(data[0])

    while iterations < 1: #max_trials:
        maybeInliers = np.random.choice(data[0].shape[0], size=min_samples, replace=False) # gets "min_samples" of random indices of the keypoints
        x = []
        y = []

        # sets the maybeInliers into respective x and y
        for inl_count in range(len(maybeInliers)):
            x.append(data[0, maybeInliers[inl_count]])
            y.append(data[1, maybeInliers[inl_count]])

        x = np.array(x)
        y = np.array(y)
        # print(x)
        # print(y)

        maybeModel = model(x, y) # fits the model to the maybeInliers and stores as maybeModel
        # print(maybeModel)

        x_hat = maybeModel@x
        # x_hat = x_hat.reshape(2, 3)
        # x_hat = np.concatenate([x_hat, [[0, 0, 1]]])
        # print(x_hat)

        err = np.linalg.norm(x_hat - y, ord=2)
        # print(err)

        confirmedInliers = [] # placeholder to store the for sure inliers

        # x_hat = maybeModel@data[0, 0]
        print(data[0, 0])

        for idx in range(len(maybeInliers)):
            x_hat = maybeModel@x
            err = np.linalg.norm(x_hat - y, ord=2)
            if err < residual_threshold:
                confirmedInliers.append(idx)


        iterations += 1

    return

# MAIN

img1 = io.imread("img/campus_000.jpg")
img2 = io.imread("img/campus_001.jpg")

# Detect and Extract keypoints from image using SIFT
sift = SIFT()

img1_gray = rgb2gray(img1) # img1 gray scaled
sift.detect_and_extract(img1_gray) # obtains keypoints of img1_gray
# keypoints and descriptors of img1
keypoints1 = sift.keypoints
descriptors1 = sift.descriptors

img2_gray = rgb2gray(img2) # img2 gray scaled
sift.detect_and_extract(img2_gray) # obtains keypoints of img2_gray
# keypoints and descriptors of img2
keypoints2 = sift.keypoints
descriptors2 = sift.descriptors

# matching descriptors btwn img1 and img2
matches_temp = match_descriptors(descriptors1, descriptors2, cross_check=True, max_ratio=0.8)

# list of matching pairs of indices
kp_matches = kp_matching(keypoints1, keypoints2, descriptors1, descriptors2)

# plots the the matching keypoints of img1 and img2 side by side
# plot_kp_matches(img1, img2, keypoints1, keypoints2, kp_matches)
plot_kp_matches(img1, img2, keypoints1, keypoints2, kp_matches)

# gets set of points from the source image and their matching points in the destinagtion image
# dst = keypoints1[kp_matches[:, 0]][:, ::-1]
# src = keypoints2[kp_matches[:, 1]][:, ::-1]
src = keypoints1[kp_matches[:, 0]][:, ::-1]
dst = keypoints2[kp_matches[:, 1]][:, ::-1]

# # estimates the affine matrix for image stitching
compute_affine_transform(src, dst)

# # estimages the projective matrix for image stitching
compute_projective_transform(src, dst)

max_trials = 100
min_samples = 3
residual_threshold = 1
data = np.array([src, dst])
# print(data)

# stitches img1 and img2 together given a specified transformation matrix
# ransac(data, min_samples, residual_threshold, max_trials)


