import time
import threading
from esp32_test_receiver import start_server
from data_storage import shared_data
import math


selected_plane = "XOY"

# Global state for yaw calculation
yaw_xoz = 0.0

def calculate_orientation(accel_data, gyro_data, dt):
    global yaw_xoz
    rad_to_deg = 57.29578

    # Accelerometer angles for different planes
    pitch_xoy = math.atan2(accel_data[0], math.sqrt(accel_data[1]**2 + accel_data[2]**2)) * rad_to_deg
    roll_xoy = math.atan2(accel_data[1], accel_data[2]) * rad_to_deg
    pitch_yoz = math.atan2(accel_data[0], accel_data[2]) * rad_to_deg
    roll_yoz = math.atan2(accel_data[1], math.sqrt(accel_data[0]**2 + accel_data[2]**2)) * rad_to_deg
    pitch_xoz = math.atan2(accel_data[1], math.sqrt(accel_data[0]**2 + accel_data[2]**2)) * rad_to_deg
    roll_xoz = math.atan2(accel_data[0], accel_data[2]) * rad_to_deg

    # Gyroscope rate of change of angle
    gyro_angle_change_z = gyro_data[2] * dt

    # Update yaw for XOZ plane
    yaw_xoz += gyro_angle_change_z
    yaw_xoz %= 360  # Normalize yaw to 0-360 degrees

    return roll_xoy, pitch_xoy, roll_yoz, pitch_yoz, pitch_xoz, roll_xoz, yaw_xoz

def process_data():
    global selected_plane
    data = shared_data.get_latest_data()
    if data:
        data_points = data.split(',')
        if len(data_points) == 6:
            try:
                accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z = map(float, data_points)
                roll_xoy, pitch_xoy, roll_yoz, pitch_yoz, pitch_xoz, roll_xoz, yaw_xoz = calculate_orientation((accel_x, accel_y, accel_z), (gyro_x, gyro_y, gyro_z), 0.01)

                if selected_plane == "XOY":
                    return roll_xoy, pitch_xoy
                elif selected_plane == "YOZ":
                    return roll_yoz, pitch_yoz
                elif selected_plane == "XOZ":
                    return pitch_xoz, roll_xoz, yaw_xoz
            except ValueError:
                print("Error processing data")
                return None
    return None

def map_speed(value, min_val, max_val):
    return int((value - min_val) / (max_val - min_val) * 4000)

def get_speed_control(basic_direction):
    data = process_data()
    if data is None:
        return 0

    if selected_plane in ["XOY", "YOZ"]:
        r, p = data[:2]
    else:  # "XOZ"
        p, r, _ = data

    speed = 0
    if basic_direction == "forward" and  10< r < 110:
        speed = map_speed(r, 10, 110)
    elif basic_direction == "backward" and -110 < r < -10:
        speed = map_speed(r, -110, -10)
    elif basic_direction == "right" and 10 < p < 80:
        speed = map_speed(p, 10, 80)
    elif basic_direction == "left" and -80 < p < -10:
        speed = map_speed(p, -80, -10)

    return speed

server_thread = None

def start_server_thread():
    global server_thread
    if server_thread is None or not server_thread.is_alive():
        server_thread = threading.Thread(target=start_server)
        server_thread.daemon = True
        server_thread.start()
    else:
        print("Server is already running.")

def data_main(direction):
    start_server_thread()
    speed = get_speed_control(direction)
    print(f"Calculated speed: {speed}")
    return speed

