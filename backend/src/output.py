#!/usr/bin/env python
# coding: utf-8

# ## Computer Vision(CS 436, CS5310, EE513) Programming Assignment#3 Part#1

# ### Currently there are lots of professional cartoonizer applications available in the market but most of the them are not freeware, you don't need powerful rendering software or even years of experience to develop such an application(as you will see in this assignment) All you need is essentially a bilateral filter and some edge detection. You are allowed to use opencv for this assigment

# ## Step#1
# ### In this step we will be applying a bilateral filter on our input image. A bilateral filter is used for smoothening images and reducing noise, while preserving edges, because a bilateral filter smooths flat regions while keeping edges sharp, it is ideally suited to convert an RGB image into a cartoon. Unfortunately, bilateral filters are orders of magnitudes slower than other smoothing operators (e.g., Gaussian blur). Thus, if speed is important, it might be a good idea to operate on a down-scaled version of the original image first and then upscale it afterwards.

# In[134]:


def cartoonifier(imagepath):
    #required imports
    import matplotlib
    from mpl_toolkits import mplot3d
    from matplotlib import pyplot as plt
    from matplotlib import cm
    from matplotlib import image as mpimg
    from matplotlib.pyplot import figure
    import cv2
    # get_ipython().run_line_magic('matplotlib', 'inline')

    #TO DO
    #step 1
    #Use bilateral filter for edge-aware smoothing.
    img = cv2.imread(imagepath)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cols, rows = img.shape[0], img.shape[1]

    num_down = 2 # number of downsampling steps 
    num_bilateral = 6 # number of bilateral filtering steps
    newimg = img

    # downsample image using Gaussian pyramid(see opencv 'pyrDown()' function)
    # Default pyrDown settings will downsample the image by (cols+1/2, rows/2) 
    for i in range(num_down):
        newimg = cv2.pyrDown(newimg)

    # repeatedly apply small bilateral filter instead of
    # applying one large filter
    # Bilateral filter takes source img, diameter of each pixel, sigmaColor and sigmaSpace as inputs
    for i in range(num_bilateral):
        newimg = cv2.bilateralFilter(newimg, 9, 20, 20)

    # Default pyrDown settings will downsample the image by (cols+1/2, rows+1/2) 
    # upsample image to original size (see opencv 'pyrUp()' function)
    for i in range(num_down):
        newimg = cv2.pyrUp(newimg)

    # Since we have 1 more extra column than the original image (due to pyrDown ki default settings), 
    # we resize the newImg file to the size of original image
    newimg = cv2.resize(img, (rows, cols))

    # ## Step#2
    # ### In this step we will blur the original image. This is considered as a pre-processing step before we move on towards the edge detection step. We will apply a median filter on the image, which replaces each pixel value with the median value of all the pixels in a small neighborhood.

    #TO DO
    #step 2
    # convert to grayscale and apply median blur
    greyscale = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    blur = cv2.medianBlur(greyscale, 7)

    # ## Step#3
    # ### In this step we will create an edge mask from the output produced in step#2 using adaptive thresholding 

    #TO DO
    #step 3
    # detect and enhance edges(see opencv 'adaptiveThreshold()' function)
    mask = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

    # ## Final Step
    # ### In this step we will combine the output produced in step#1 and step#3 using a bitwise and operator to produce our final output.(Note: You need to convert output from step#3 to color first)

    #TO DO
    #Final Step
    # convert back to color, bit-AND with color image
    colorOutput = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
    final = cv2.bitwise_and(newimg, colorOutput)
    #show output
    return final
    # figure(dpi = 100)
    # plt.imshow(final)
    # plt.show()


    # In[ ]:




