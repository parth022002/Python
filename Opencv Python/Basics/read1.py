#reading videos
import cv2 as cv

capture = cv.VideoCapture(0) # for reading the video from the web cam
#capture = cv.VideoCapture('Resources/Videos/dog.mp4') # read the video already present in the directory

while True:
    isTrue, frame = capture.read()

    cv.imshow('Video',frame)
    
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
