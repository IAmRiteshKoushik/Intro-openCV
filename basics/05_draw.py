import cv2 as cv
import numpy as np

# Create a blank image using numpy
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Point the image a certain color
blank[200:300, 300:400] = 0, 0, 255
cv.imshow('Red', blank)

# 2. We can color an entire portion by not specifying the limits
blank[:] = 0, 0, 255
cv.imshow('Red', blank)

# 3. Draw a rectangle
# Parameters = window, diagonal coords-1, diagonal coords-2, thickness
# If we need a fully filled rectangle, thickness = -1
# or thickness = cv.FILLED [ this is just an attribute which returns -1 ]
cv.rectangle(blank, (200, 200), (250, 250), (0, 255, 0), thickness=-1)
cv.imshow('Rectangle', blank)

# In the coordinate system we should probably use values like 
# x-coord : blank.shape[1]
# y-coord : blank.shape[0]

# 4. Draw a circle
cv.circle(blank, (250, 250), 7, (255, 0, 0), thickness=3)
cv.imshow('Circle', blank)

# 5. Draw a line
blank2 = np.zeros((500, 500, 3), dtype='uint8')
cv.line(blank, (30, 30), (100, 100), (230, 232, 23), thickness=4)
cv.imshow('Line', blank)

# 6. Adding text

blank2 = np.zeros((500, 1000, 3), dtype='uint8')
cv.putText(blank2, 'Hello, I am Ritesh Koushik', (255, 255), cv.FONT_HERSHEY_TRIPLEX, 
           fontScale=1.0, color=(0, 255, 0), thickness=2)
cv.imshow('Text', blank2)
# Wait for an infinite amount of time before key is pressed
cv.waitKey(0)  