#reading videos
import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# for the resolution of the video 
def changeRes(width,height): # Only for live video
    capture.set(3, width)
    capture.set(4,height)

#capture = cv.VideoCapture(0) # for reading the video from the web cam
capture = cv.VideoCapture('Resources/Videos/dog.mp4') # read the video already present in the directory

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=.2)

    cv.imshow('Video',frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
