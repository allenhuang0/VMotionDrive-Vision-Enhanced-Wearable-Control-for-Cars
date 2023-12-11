import cv2
import threading
import queue
import mediapipe as mp
from Motor import *
from detection_algo import *
from data_processing import *




def calculate_direction(largest_landmarks):
    direction = "stop"
    translated_landmarks = get_translated_landmarks(largest_landmarks)
    angle_landmark_12 = get_angle(translated_landmarks[12].x, translated_landmarks[12].y)
    distance_12 = get_dist(translated_landmarks[12].x, translated_landmarks[12].y)
    distance_11 = get_dist(translated_landmarks[11].x, translated_landmarks[11].y)
    if distance_12 > distance_11:
        direction = detect_gesture(angle_landmark_12, translated_landmarks)
    return direction



# setting parameter for cam.
class CameraStream:
    def __init__(self, src=0):
        self.capture = cv2.VideoCapture(src, cv2.CAP_V4L2)
        self.capture.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
        self.capture.set(cv2.CAP_PROP_FPS, 20)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

        self.q = queue.Queue()
        self.stopped = False
        self.thread = threading.Thread(target=self.update, args=())
        self.thread.daemon = True

    def start(self):
        self.thread.start()
        return self

    def update(self):
        while True:
            if self.stopped:
                return

            (grabbed, frame) = self.capture.read()
            if not grabbed:
                self.stop()
                return

            with self.q.mutex:
                self.q.queue.clear()
            self.q.put(frame)

    def read(self):
        return self.q.get()

    def stop(self):
        self.stopped = True
        self.thread.join()
        self.capture.release()

# Initialize MediaPipe hand module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1,
                       min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Initialize the camera
stream = CameraStream(src=0).start()

PWM = Motor()

try:
    while True:
        frame = stream.read()
        if frame is None:
            break

        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)

        largest_landmarks = None
        direction_result = "stop"

        if results.multi_hand_landmarks:
            largest_landmarks = get_closest_hand_landmarks(results.multi_hand_landmarks)

            if largest_landmarks:
                mp_drawing.draw_landmarks(frame, largest_landmarks, mp_hands.HAND_CONNECTIONS)
                direction_result = calculate_direction(largest_landmarks)
                
        s=data_main(direction_result)
        
        if s!=0:
            sp= abs(4000-s)
        else:
            sp=0
            
        print(s,sp)
        if direction_result == "left":
            PWM.setMotorModel(-int(0.8*s),-int(0.8*s),int(0.8*s),int(0.8*s))         
                
        elif direction_result == "right":

            PWM.setMotorModel(int(0.8*sp),int(0.8*sp),-int(0.8*sp),-int(0.8*sp))
                
        elif direction_result == 'backward':
       
            PWM.setMotorModel(sp,sp,sp,sp)
            
        elif direction_result == 'forward':
                    
            PWM.setMotorModel(-s,-s,-s,-s)
        else:
            PWM.setMotorModel(0,0,0,0)
            
        print(direction_result)

        cv2.imshow('Hand Tracking', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    stream.stop()
    cv2.destroyAllWindows()
    hands.close()


