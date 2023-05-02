import cv2 as cv

# Reading videos
# The method takes in, either integer inputs or file path inputs
# Webcam and other cameras connected are referenced with integers
# Images stored in the directory are referenced using filepaths.
capture = cv.VideoCapture(r'Videos/dog.mp4')

# We read videos in while loop because it is read frame-by-frame.
# It returns a BOOLEAN informing about whether the frame has been read or
# not. And returns the FRAME object as well. 

while True:
    isTrue, frame = capture.read()

    # Shows the video frame by frame
    cv.imshow('Video', frame)
    # If after a wait of 20 milliseconds
    # If letter 'd' is pressed, break out of the loop
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

# Release the video that has been loaded in memory for playing
capture.release()
# Destroys the HighGUI windows created by OpenCV
cv.destroyAllWindows()
