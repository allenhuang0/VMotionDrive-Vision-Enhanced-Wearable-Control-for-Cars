#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 18:36:29 2023

@author: qianguanyu
"""


import cv2
import mediapipe as mp
import websocket
import json

# Initialize the pose estimation
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Initialize WebSocket connection
ws_url = "ws://raspberrypi.local:65432"  # Replace with your Raspberry Pi's IP and the chosen port
ws = websocket.WebSocket()
ws.connect(ws_url)

# For demonstration, capturing video from the default camera
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    # Process the frame for pose estimation
    results = pose.process(frame)

    if results.pose_landmarks:
        # Convert pose landmarks to a dictionary and serialize to JSON
        data_to_send = {
            'landmarks': [[landmark.x, landmark.y, landmark.z] for landmark in results.pose_landmarks.landmark]
        }
        ws.send(json.dumps(data_to_send))

    # For visualization, you can also show the processed frame on your laptop
    annotated_frame = frame.copy()
    mp.solutions.drawing_utils.draw_landmarks(annotated_frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    cv2.imshow('MediaPipe Pose', annotated_frame)
    
    # Press 'q' to exit the loop and close the video feed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
ws.close()
