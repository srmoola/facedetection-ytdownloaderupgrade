import cv2
from ytdownupgrade import *

vidPath = switchPath(r"Enter File Path Here")
downloadVidTo(vidPath)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

videoOpen = str(input("Paste in the video path from your folder: "))
videoOpen = switchPath(videoOpen)

video = cv2.VideoCapture(videoOpen)

while video.isOpened():
    # Read the current frame
    ret, frame = video.read()

    if not ret:
        break

    # Resize the frame (optional)
    frame = cv2.resize(frame, (0, 0), fx=0.75, fy=0.75)

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform face detection
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))

    # Draw rectangles and labels around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.putText(frame, 'Face', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Face Detection', frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the windows
video.release()
cv2.destroyAllWindows()
