import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2)

def get_bounding_box(landmarks):
    x_coordinates = [landmark.x for landmark in landmarks]
    y_coordinates = [landmark.y for landmark in landmarks]
    return (min(x_coordinates), min(y_coordinates), max(x_coordinates), max(y_coordinates))

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)

    if results.multi_hand_landmarks:
        # Find the hand with the largest bounding box
        largest_bbox = (0, 0, 0, 0)
        largest_landmarks = None
        for landmarks in results.multi_hand_landmarks:
            bbox = get_bounding_box(landmarks.landmark)
            bbox_area = (bbox[2]-bbox[0]) * (bbox[3]-bbox[1])
            largest_bbox_area = (largest_bbox[2]-largest_bbox[0]) * (largest_bbox[3]-largest_bbox[1])

            if bbox_area > largest_bbox_area:
                largest_bbox = bbox
                largest_landmarks = landmarks

        # Process only the largest (closest) hand for pointing direction
        if largest_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(frame, largest_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Check if all four fingers are extended
            fingers_extended = [
                largest_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y <
                largest_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y,
                largest_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y <
                largest_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y,
                largest_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y <
                largest_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y,
                largest_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y <
                largest_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y,
            ]

            if all(fingers_extended):
                # Calculate average x position of the finger tips and finger bases (MCP joints)
                avg_x_tip = sum([
                    largest_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x,
                    largest_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x,
                    largest_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x,
                    largest_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x
                ]) / 4.0

                avg_x_base = sum([
                    largest_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].x,
                    largest_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x,
                    largest_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].x,
                    largest_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].x
                ]) / 4.0

                # Check direction of pointing (left or right)
                if avg_x_tip > avg_x_base:
                    cv2.putText(frame, 'Pointing Right', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                else:
                    cv2.putText(frame, 'Pointing Left', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow('Hand Tracking', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
