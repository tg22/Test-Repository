#
# coding: utf-8
"""This function takes in images, runs K-means on them and then posterizes them based on how many means the user selects. It's cool!"""
# hw8pr1.py - the k-means algorithm -- with pixels...
#

# import everything we need...
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import utils
import math
import cv2

# choose an image...
#IMAGE_NAME = "./jp.png"  # Jurassic Park
#IMAGE_NAME = "./batman.png"
#IMAGE_NAME = "./hmc.png"
#IMAGE_NAME = "./ozil.jpg"
#IMAGE_NAME = "./puma.jpg"
IMAGE_NAME = "testwallpaper.jpg"
image = cv2.imread(IMAGE_NAME, cv2.IMREAD_COLOR)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# reshape the image to be a list of pixels
image_pixels = image.reshape((image.shape[0] * image.shape[1], 3))

# choose k (the number of means) in  NUM_MEANS
# and cluster the pixel intensities
NUM_MEANS = 4
clusters = KMeans(n_clusters = NUM_MEANS)
clusters.fit(image_pixels)

# After the call to fit, the key information is contained
# in  clusters.cluster_centers_ :
count = 0
for center in clusters.cluster_centers_:
    print("Center #", count, " == ", center)
    # note that the center's values are floats, not ints!
    center_integers = [int(p) for p in center]
    print("   and as ints:", center_integers)
    count += 1

# build a histogram of clusters and then create a figure
# representing the number of pixels labeled to each color
hist = utils.centroid_histogram(clusters)
bar = utils.plot_colors(hist, clusters.cluster_centers_)


# in the first figure window, show our image
plt.figure()
plt.axis("off")
plt.imshow(image)

# in the second figure window, show the pixel histograms 
#   this starter code has a single value of k for each
#   your task is to vary k and show the resulting histograms
# this also illustrates one way to display multiple images
# in a 2d layout (fig == figure, ax == axes)
#
fig, ax = plt.subplots(nrows=2, ncols=2, sharex=False, sharey=False)
title = str(NUM_MEANS)+" means"
ax[0,0].imshow(bar);    ax[0,0].set_title(title)
ax[0,1].imshow(bar);    ax[0,1].set_title(title)
ax[1,0].imshow(bar);    ax[1,0].set_title(title)
ax[1,1].imshow(bar);    ax[1,1].set_title(title)
for row in range(2):
    for col in range(2):
        ax[row,col].axis('off')
plt.show(fig)

def closestmean (r,g,b):
    location = []
    centers = []
    for center in clusters.cluster_centers_:
        r1 = r - center[0]
        g1 = g - center[1]
        b1 = b - center[2]
        total = math.sqrt(r1**2 + g1**2 +b1**2)
        location += [total]
        centers += [center]
    for x in range(len(location)):
        if location[x] == min(location):
            count = x
    close_center = centers[count]

    return close_center



def posterize (IMAGE_NAME=IMAGE_NAME):
    #IMAGE_NAME = "./puma.jpg"
    image = cv2.imread(IMAGE_NAME, cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    num_rows, num_cols, num_chans = image.shape

    for row in range(num_rows):
        for col in range(num_cols):
            r, g, b = image[row,col]
            r1, g1, b1 = closestmean(r,g,b)
            r, g, b = r1, g1, b1 
            image[row, col] = r, g, b

    newimage = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # convert back!
    cv2.imwrite( "posterized.png", newimage )
    print("The file posterized.png was written...")
    print("Also returning that image...") 
    # ni = posterize (lmao)
    # plt.imshow(ni) 
    # print("hi")
    plt.show()

    return image

#
# comments and reflections on hw8pr1, k-means and pixels
"""
 + Which of the paths did you take:  
    + posterizing or 
    + algorithm-implementation

 + How did it go?  Which file(s) should we look at?
 + Which function(s) should we try...
"""
#
#
