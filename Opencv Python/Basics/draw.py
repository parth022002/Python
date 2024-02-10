import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow("Blank", blank)

# paint the image a certain colour
blank[:] = 255,255,255
cv.imshow('white', blank)


# drawing the rectangle 
cv.rectangle(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2),(0,255,0),thickness=-1) # green color
cv.imshow('Rectangle', blank)

# drawing a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow( 'Circle', blank )

# draw a line
cv.line(blank, (100,250), (blank.shape[1]//2, blank.shape[0]//2),(0,0,0),thickness=3)
cv.imshow( 'Line', blank )

# text on a image
cv.putText(blank, 'Opencv', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,0,0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)