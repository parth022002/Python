#reading images 
import cv2 as cv


img = cv.imread('Resources/Photos/cat.jpg')  # Read the image from file
# The function returns a numpy array containing the pixel values of the image, which we can then manipulate using NumPy functions

cv.imshow(winname='Cat', mat=img)  # Create a window with the name 'Cats' and show the image in it

cv.waitKey(0)  # Wait for a key event indefinitely (0 ms)
                    # If you press any key, the program will continue to run