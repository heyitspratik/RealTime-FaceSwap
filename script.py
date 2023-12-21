import cv2
import dlib
import numpy as np

# Load the pre-trained face detector and shape predictor from dlib
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")  # Download this file from http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2

# Load the celebrity face image
celebrity_image = cv2.imread("robert_downey_jr.png")  # Replace with the path to your celebrity image

# Create a VideoCapture object for the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = detector(gray)

    for face in faces:
        # Get the landmarks for the detected face
        landmarks = predictor(gray, face)

        # Extract the coordinates of the eyes, nose, and mouth
        left_eye = landmarks.part(36).x, landmarks.part(36).y
        right_eye = landmarks.part(45).x, landmarks.part(45).y
        nose = landmarks.part(30).x, landmarks.part(30).y
        mouth_left = landmarks.part(48).x, landmarks.part(48).y
        mouth_right = landmarks.part(54).x, landmarks.part(54).y

        # Calculate the width and height of the face
        face_width = int(right_eye[0] - left_eye[0])
        face_height = int(mouth_left[1] - nose[1])

        # Resize the celebrity face image to match the face dimensions
        celebrity_face = cv2.resize(celebrity_image, (face_width, face_height))

        # Create a mask for the celebrity face
        mask = np.zeros_like(frame)
        mask[face.top():face.top() + face_height, face.left():face.left() + face_width] = celebrity_face

        # Replace the face in the frame with the celebrity face
        result = np.where(mask != 0, mask, frame)

    # Display the resulting frame
    cv2.imshow("Face Swapping", result)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture and close all windows
cap.release()
cv2.destroyAllWindows()
