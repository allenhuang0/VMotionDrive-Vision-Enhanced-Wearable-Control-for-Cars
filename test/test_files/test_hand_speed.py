import cv2
import mediapipe as mp
import time
import numpy as np

# Initialize MediaPipe Hand module.
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands()

# Initialize previous landmark position and time.
prev_x, prev_y, prev_time = None, None, None

# List to store the speeds.
speeds = []

# Record the start time.
start_time = time.time()

# Start capturing video from the first webcam device.
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # Check the total time elapsed to ensure it's within the 10-second window.
    if time.time() - start_time > 10:
        break

    success, image = cap.read()
    if not success:
        continue

    # Flip the image horizontally for a later selfie-view display, and convert the BGR image to RGB.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Get the index fingertip landmark.
            landmark = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            x, y = int(landmark.x * image.shape[1]), int(landmark.y * image.shape[0])

            if prev_time is not None:  # Ensure there is a previous timestamp to compare against.
                time_diff = time.time() - prev_time
                if time_diff > 0:  # Check that time_diff is greater than zero to avoid division by zero.
                    distance = np.sqrt((x - prev_x) ** 2 + (y - prev_y) ** 2)
                    speed = distance / time_diff
                    speeds.append(speed)  # Add the calculated speed to the list of speeds.

            # Update the previous landmark position and timestamp.
            prev_x, prev_y, prev_time = x, y, time.time()

            # Draw the hand landmarks on the image.
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Display the image.
    cv2.imshow('Hand Movement Speed', image)

    if cv2.waitKey(5) & 0xFF == 0x71:  # 'q' to quit.
        break

# Clean up.
cap.release()
cv2.destroyAllWindows()

# Calculate and display the average speed.
if speeds:  # Ensure there are recorded speeds to calculate the average.
    average_speed = np.mean(speeds)
    print(f"Average speed: {average_speed:.2f} pixels/second over the 10-second window.")
else:
    print("No hand movement detected or too fast to track reliably.")
