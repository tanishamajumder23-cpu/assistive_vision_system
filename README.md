# image-watermarking-tool

Real-time face detection using OpenCV (Haar cascades) and NumPy on live webcam video streams

DOCUMENTING MY LEARNING AND THE EXPERIMENTATIONS AT VARIOUS STAGES:

import cv2 # import the OpenCV library
img = cv2.imread("test.jpg") # reads the image and returns a NumPy array 
# (OpenCV opened the file, converted it into a NumPy array and then stored it in img)
cv2.imshow("Image",img) # displays the image in a window
cv2.waitKey(0) # waits until we press a key
cv2.destroyAllWindows() # Closes window
# In one line, I loaded an image into memory and displayed it using OpenCV
