import cv2 as cv

# Small and big cat images
# OpenCV does not have geometric properties to deal with
# controlling image sizes and generates windows which encapsulate
# the resolution of the image. 
img = cv.imread('Photos/cat.jpg')
img = cv.imread('Photos/cat_large.jpg')

cv.imshow('Cat', img)

# Waits for an infinite amount of time for a key to be pressed
# inorder for the windows to close. 
cv.waitKey(0)

