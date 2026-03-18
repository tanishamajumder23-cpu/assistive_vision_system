# image-watermarking-tool

Real-time face detection using OpenCV (Haar cascades) and NumPy on live webcam video streams

DOCUMENTING MY LEARNING AND THE EXPERIMENTATIONS AT VARIOUS STAGES:

OpenCV Image Handling – Documentation Notes
1. Importing the Library
import cv2

cv2 refers to the OpenCV library.

It provides functions for image processing, computer vision, and related tasks.

2. Reading an Image
img = cv2.imread("test.jpg")
Description:

Reads an image file from the specified path.

Returns the image as a NumPy array.

Internal Working:

The image file is opened and decoded.

Pixel values are extracted and stored in a multi-dimensional array.

The array is assigned to the variable img.

Note:

If the file path is incorrect or the image cannot be loaded, the function returns None.

3. Image Representation in Memory

An image is stored as a matrix of pixel values.

Each pixel consists of three components: Blue, Green, and Red (BGR).

Structure:
img = [
    [[B, G, R], [B, G, R], ...],
    [[B, G, R], [B, G, R], ...],
    ...
]
Key Point:

OpenCV uses BGR color format, unlike many other libraries that use RGB.

4. Displaying the Image
cv2.imshow("Image", img)
Description:

Displays the image in a window.

The first argument is the window title.

The second argument is the image array.

Internal Working:

The NumPy array is converted back into a visual image format.

A window is created and the image is rendered inside it.

5. Waiting for User Input
cv2.waitKey(0)
Description:

Waits for a key press before proceeding.

0 indicates an indefinite wait.

Purpose:

Prevents the display window from closing immediately after opening.

6. Closing the Window
cv2.destroyAllWindows()
Description:

Closes all OpenCV windows.

Frees associated resources.

7. Summary

The image is read from disk using cv2.imread().

It is stored as a NumPy array representing pixel values in BGR format.

The array is displayed using cv2.imshow().

Execution is paused using cv2.waitKey() to allow viewing.

All windows are closed using cv2.destroyAllWindows().
