import cv2
import time

from detection_algo import *


def calculate_direction(largest_landmarks):
    
    direction = "stop"
    translated_landmarks = get_translated_landmarks(largest_landmarks)

    angle_landmark_12 = get_angle(translated_landmarks[12].x, translated_landmarks[12].y)
    
    distance_12 = get_dist(translated_landmarks[12].x, translated_landmarks[12].y)
    distance_11 = get_dist(translated_landmarks[11].x, translated_landmarks[11].y)

    if distance_12 > distance_11:
        direction = detect_gesture(angle_landmark_12, translated_landmarks)

    return direction


#Main loop

# Initialize the camera


cap = cv2.VideoCapture(0)


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)

    largest_bbox = (0, 0, 0, 0)
    largest_landmarks = None
    
    direction_result = "stop" 
    
    if results.multi_hand_landmarks:
        largest_landmarks = get_closest_hand_landmarks(results.multi_hand_landmarks)

        if largest_landmarks:
            # Process only the largest (closest) hand
            
            
            mp.solutions.drawing_utils.draw_landmarks(frame, largest_landmarks, mp_hands.HAND_CONNECTIONS)
            
            
            direction_result= str(calculate_direction(largest_landmarks))
            
    print(direction_result)
            
            

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    time.sleep(0.1)

cap.release()
cv2.destroyAllWindows()
