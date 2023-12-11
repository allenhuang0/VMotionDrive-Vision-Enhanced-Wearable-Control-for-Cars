import cv2
import time
import numpy as np
import mediapipe as mp

from servo import Servo
from detection_algo import *
from Motor import *

'''
# Initialize MediaPipe hand module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils
'''



def calculate_direction(largest_landmarks):
    direction = "stop"
    if largest_landmarks:
        translated_landmarks = get_translated_landmarks(largest_landmarks)
        angle_landmark_12 = get_angle(translated_landmarks[12].x, translated_landmarks[12].y)
        distance_12 = get_dist(translated_landmarks[12].x, translated_landmarks[12].y)
        distance_11 = get_dist(translated_landmarks[11].x, translated_landmarks[11].y)

        if distance_12 > distance_11:
            direction = detect_gesture(angle_landmark_12, translated_landmarks)
    return direction


'''
def map_hand_position_to_servo_angle(frame_width, frame_height, x, y, servo_min_angle, servo_max_angle):
    angle_x = servo_min_angle + (x / frame_width) * (servo_max_angle - servo_min_angle)
    angle_y = servo_min_angle + ((frame_height - y) / frame_height) * (servo_max_angle - servo_min_angle)
    return angle_x, angle_y
'''




# Initialize the camera
gst_pipeline = 'libcamerasrc ! video/x-raw, width=1280, height=720, framerate=30/1 ! videoconvert ! appsink'
cap = cv2.VideoCapture(gst_pipeline, cv2.CAP_GSTREAMER)

servo = Servo()
PWM = Motor()

servo.setServoPwm('0',60)
servo.setServoPwm('1', 135)

'''
speed = 1  # Adjust speed as needed
prev_angle_x, prev_angle_y = 60, 135  
'''

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)

    largest_landmarks = None
    direction_result = "stop" 

    if results.multi_hand_landmarks:
        largest_landmarks = get_closest_hand_landmarks(results.multi_hand_landmarks)

        if largest_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(frame, largest_landmarks, mp_hands.HAND_CONNECTIONS)
            direction_result = calculate_direction(largest_landmarks)
            
            #For servo control
            '''
            wrist_landmark = largest_landmarks.landmark[mp_hands.HandLandmark.WRIST]
            wrist_x, wrist_y = int(wrist_landmark.x * frame.shape[1]), int(wrist_landmark.y * frame.shape[0])
            
            target_angle_x, target_angle_y = map_hand_position_to_servo_angle(
                frame.shape[1], frame.shape[0], wrist_x, wrist_y, 0, 180)

            angle_x = np.clip(prev_angle_x + np.sign(target_angle_x - prev_angle_x) * speed, 0, 180)
            angle_y = np.clip(prev_angle_y + np.sign(target_angle_y - prev_angle_y) * speed, 0, 180)

            servo.setServoPwm('0', angle_x)
            servo.setServoPwm('1', angle_y)

            prev_angle_x, prev_angle_y = angle_x, angle_y
            '''
            
            #allen can add wearable control here
            
            if direction_result == "left":
                PWM.setMotorModel(-4000,-4000,4000,4000)  # Left
                
                time.sleep(0.1)
                PWM.setMotorModel(0,0,0,0)
                
            elif direction_result == "right":
                
                PWM.setMotorModel(1500,1500,-1500,-1500)  # Right
                time.sleep(0.1)
                PWM.setMotorModel(0,0,0,0)
                
            elif direction_result == 'stop':
                PWM.setMotorModel(0,0,0,0)  # Stop
                

    print(direction_result)

    cv2.imshow('Hand Tracking', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

