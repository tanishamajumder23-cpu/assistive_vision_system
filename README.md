Project Progress Documentation (Till Now)
Project Title

Real-Time Face Detection using OpenCV and NumPy

Objective

To build a system that captures live video from a webcam and processes each frame in order to detect faces in real time.

Step-by-Step Learning and Implementation
Step 4: Capturing Webcam Input

Implementation:

ret, frame = cap.read()
Step 6: Controlling Program Exit

Implementation:

Exit using ESC key:

if cv2.waitKey(1) & 0xFF == 27:
    break

Exit when window is closed:

if cv2.getWindowProperty("Webcam", cv2.WND_PROP_VISIBLE) < 1:
    break
Step 7: Releasing Resources

Implementation:

cap.release()
cv2.destroyAllWindows()
Step 8: Converting Frames to Grayscale

Implementation:

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
Step 10: Loading Haar Cascade for Face Detection

Implementation:

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
Step 11: Detecting Faces

Implementation:

faces = face_cascade.detectMultiScale(gray, 1.1, 4)
Step 12: Drawing Bounding Boxes

Implementation:

for (x, y, w, h) in faces:
    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
Step 13: Adding Semantic Meaning to Detection

Implementation:

cv2.putText(frame, "Person Ahead", (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)
Step 14: Introducing Audio Feedback (Text-to-Speech)

Implementation:

import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

Used inside detection loop:

speak("Person ahead")
Current Status
Webcam feed successfully implemented
Frame processing established
Grayscale conversion completed
Face detection implemented
Bounding boxes displayed in real time
Basic semantic labeling added
Audio feedback introduced
Next Direction

The system currently detects and announces faces, but it lacks control and additional environmental awareness.

Next steps will focus on:

Preventing repeated speech (cooldown mechanism)
Detecting obstacles in addition to faces
Identifying spatial position (left, right, center)
Making the system more stable and usable in real-time scenarios
