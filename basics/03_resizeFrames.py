import cv2 as cv
import numpy as np

# Read the image using imread function
image = cv.imread('Photos/cat.jpg')
cv.imshow('Original Image', image)

down_width = 300
down_height = 200
down_points = (down_width, down_height)
resized_down = cv.resize(image, down_points, interpolation=cv.INTER_AREA)

up_width = 600
up_height = 400
up_points = (up_width, up_height)
resized_up = cv.resize(image, up_points, interpolation=cv.INTER_AREA)

# Display images
cv.imshow('Resized down by defining height and width', resized_down)
cv.waitKey()
cv.imshow('Resized down by defining height and width', resized_up)
cv.waitKey()

# Press any key to close the windows
cv.destroyAllWindows()
