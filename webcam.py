import cv2 #Imports OpenCV library
cap=cv2.VideoCapture(0) # opens the webcamera and 0 is our default laptop camera here
# cap = object that controls your camera

# Load Haar Cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True: # infinite loop because video= continuous frames
    ret, frame=cap.read() # frame = the NumPy array image and the ret = whether the frame was captured sucessfully
    #ret = did it work?  &  frame = the image
    if not ret:
        break
     # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw rectangles
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, "Person Ahead", (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)
    cv2.imshow("Webcam", frame)
    # Show grayscale frame
    #cv2.imshow("Webcam", gray)
    #We convert to grayscale because face detection focuses on facial 
    #structures (like edges and shapes), not colors. 
    #Grayscale reduces data, making processing faster, 
    #and Haar Cascade models are trained on 
    #grayscale images, so they perform better with this input.
    #cv2.imshow("Webcam", frame) # displays each frame
    if cv2.waitKey(1) & 0xFF == 27: # Did user press ESC? The ascii of ESC is 27
        break
    if cv2.getWindowProperty("Webcam", cv2.WND_PROP_VISIBLE) < 1:
        # cv2.getWindowProperty("Webcam", cv2.WND_PROP_VISIBLE): check if the window named 'Webcame' is visible
        break
cap.release() # turns off camera
cv2.destroyAllWindows() # closes window
#Your webcam opens ; Live video appears; Press ESC → closes
 # Exit if window is closed (❌)