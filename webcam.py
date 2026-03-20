import cv2 #Imports OpenCV library
cap=cv2.VideoCapture(0) # opens the webcamera and 0 is our default laptop camera here
# cap = object that controls your camera
while True: # infinite loop because video= continuous frames
    ret, frame=cap.read() # frame = the NumPy array image and the ret = whether the frame was captured sucessfully
    #ret = did it work?  &  frame = the image
    if not ret:
        break
     # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Show grayscale frame
    cv2.imshow("Webcam", gray)
    #We convert to grayscale because face detection focuses on facial 
    #structures (like edges and shapes), not colors. 
    #Grayscale reduces data, making processing faster, 
    #and Haar Cascade models are trained on 
    #grayscale images, so they perform better with this input.
    #cv2.imshow("Webcam", frame) # displays each frame
    if cv2.waitKey(1)==27: # Did user press ESC? The ascii of ESC is 27
        break
    if cv2.getWindowProperty("Webcam", cv2.WND_PROP_VISIBLE) < 1:
        # cv2.getWindowProperty("Webcam", cv2.WND_PROP_VISIBLE): check if the window named 'Webcame' is visible
        break
cap.release() # turns off camera
cv2.destroyAllWindows() # closes window
#Your webcam opens ; Live video appears; Press ESC → closes
 # Exit if window is closed (❌)
