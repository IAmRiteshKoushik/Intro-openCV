import cv2 as cv

def resizeImage(frame, scale=0.20):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width, height) 
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Reading Videos 
capture = cv.VideoCapture(r'Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = resizeImage(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    # Without the closing conditions, OpenCV tends to misbehave
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

# Alternate method
# Capture.set() method
def changeRes(width, height):
    # Works only for live-video (external camera or webcam)
    # Not going to work on standalone videos or images.
    capture.set(3, width)
    capture.set(4, height)

    # You can also change the brightness using the set method
     