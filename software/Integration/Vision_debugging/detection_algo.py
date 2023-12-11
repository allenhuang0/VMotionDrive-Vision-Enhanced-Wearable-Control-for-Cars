#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 16:21:59 2023

@author: qianguanyu
"""

import mediapipe as mp
import math

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2)

def get_bounding_box(landmarks):
    x_coordinates = [landmark.x for landmark in landmarks]
    y_coordinates = [landmark.y for landmark in landmarks]
    return (min(x_coordinates), min(y_coordinates), max(x_coordinates), max(y_coordinates))


def get_closest_hand_landmarks(hand_landmarks_list):
    largest_bbox = (0, 0, 0, 0)
    largest_landmarks = None
    for landmarks in hand_landmarks_list:
        bbox = get_bounding_box(landmarks.landmark)
        bbox_area = (bbox[2] - bbox[0]) * (bbox[3] - bbox[1])
        largest_bbox_area = (largest_bbox[2] - largest_bbox[0]) * (largest_bbox[3] - largest_bbox[1])

        if bbox_area > largest_bbox_area:
            largest_bbox = bbox
            largest_landmarks = landmarks
    return largest_landmarks


def get_translated_landmarks(landmarks):
    wrist_x = landmarks.landmark[mp_hands.HandLandmark.WRIST].x
    wrist_y = landmarks.landmark[mp_hands.HandLandmark.WRIST].y

    translated_landmarks = [mp.solutions.pose.PoseLandmark(i) for i in range(21)]
    for i, landmark in enumerate(landmarks.landmark):
        translated_landmarks[i].x = landmark.x - wrist_x
        translated_landmarks[i].y = landmark.y - wrist_y
    return translated_landmarks

def get_angle(x, y):
    angle = math.degrees(math.atan2(y, x))
    return angle if angle >= 0 else 360 + angle


def detect_gesture(angle, landmark_coordinate):
    
    if 310 <= angle <= 360 or 0 <= angle < 90:
        
        return "left"
    
    elif 100 <= angle < 240:
        
        return "right"
    
    elif 250 <= angle < 300:
        
        if landmark_coordinate[4].x > landmark_coordinate[20].x :
            
            return "backward"
    
        else:
            
            return "forward"
    
    else:
        return "other"
    
    
    


