import cv2 as cv

img = cv.imread('Resources/Photos/park.jpg')  # Read the image from file
cv.imshow(winname='Image', mat=img)  # Create a window with the name 'Cats' and show the image in it

#converting image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blur the image
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# how to create Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# dilate the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow("Dilated", dilated)

# Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

# resize the image
resized = cv.resize(img,(500,500),interpolation=cv.INTER_LINEAR)
cv.imshow('Resized Image', resized)

#cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)  