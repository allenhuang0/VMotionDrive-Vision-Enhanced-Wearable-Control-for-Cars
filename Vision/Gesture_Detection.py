#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 16:32:42 2023

@author: qianguanyu
"""
import cv2



from detection_algo import *

from sender_portal import *


ws_url = "ws://raspberrypi.local:65432"
ws = initialize_socket(ws_url)




#Main loop
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)

    largest_bbox = (0, 0, 0, 0)
    largest_landmarks = None

    if results.multi_hand_landmarks:
        largest_landmarks = get_closest_hand_landmarks(results.multi_hand_landmarks)

        if largest_landmarks:
            # Process only the largest (closest) hand
            mp.solutions.drawing_utils.draw_landmarks(frame, largest_landmarks, mp_hands.HAND_CONNECTIONS)

            translated_landmarks = get_translated_landmarks(largest_landmarks)
            
            angle_landmark_12 = get_angle(translated_landmarks[12].x, translated_landmarks[12].y)
            
            direction = detect_gesture(angle_landmark_12, translated_landmarks)
        
            angle_text =  direction
            
            cv2.putText(frame, angle_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
            
            
            send_direction(ws, direction)

    cv2.imshow('Hand Tracking', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
ws.close()