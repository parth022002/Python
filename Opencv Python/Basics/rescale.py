import cv2 as cv

def rescaleFrame(frame, scale=0.75): # can be used for image, video, live video 
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('Resources/Photos/cat.jpg')  # Read the image from file
# The function returns a numpy array containing the pixel values of the image, which we can then manipulate using NumPy functions
resized_image = rescaleFrame(img)

cv.imshow(winname='Cat', mat=img)
cv.imshow('Image', resized_image)  # Create a window with the name 'Cats' and show the image in it


cv.waitKey(0)  # Wait for a key event indefinitely (0 ms)