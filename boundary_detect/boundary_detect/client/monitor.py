# pylint: disable=C0116,C0411,C0301,C0303
import pyautogui
import pygetwindow as gw
import time
import socket
import pyautogui
from screeninfo import get_monitors
import math

# target_ip = "0.0.0.0"
target_ip = "10.10.10.110"
target_port = 9999
client_socket = None

def init_socket():
    global client_socket
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((target_ip, target_port))
        print("client connected")
    except socket.error:
        print('Init socket fail')
        pass

def calculate_speed(start_pos, end_pos, elapsed_time):
    # Calculate the distance between the two positions
    distance = math.sqrt((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2)
    # Calculate the speed (distance / time)
    speed = distance / elapsed_time
    return speed

def get_cursor_speed():
    # Get the initial position and time
    start_pos = pyautogui.position()
    start_time = time.time()

    # Wait for a short interval
    time.sleep(0.1)  # 100 milliseconds

    # Get the final position and time
    end_pos = pyautogui.position()
    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = end_time - start_time

    # Calculate the speed of the cursor
    speed = calculate_speed(start_pos, end_pos, elapsed_time)
    return speed

def on_cursor_reach_edge(x, y):
    print(f"Cursor has reached the edge of the screen at position: ({x}, {y})\n")

def monitor_cursor():
    while True:
        x, y = pyautogui.position()
        speed = get_cursor_speed()
        print('speed: ', speed)
        screen_width, screen_height = pyautogui.size()
        
        # Check if cursor is at the edge of the screen or in negative space
        if x <= 0 or y <= 0 or x >= screen_width - 1 or y >= screen_height - 1:
            on_cursor_reach_edge(x, y)

        time.sleep(1)


def send_cursor_position(x, y):
    # Send the cursor position
    data = f"{x},{y}".encode("utf-8")
    if client_socket:
        try:
            client_socket.sendall(data)
        except socket.error:
            pass
    else:
        print("Socket not initialized")
    # client_socket.close()


# def on_cursor_reach_edge(pos_x, pos_y):
#     # print("Cursor has reached the edge of the screen!")
#     # Send cursor to the adjacent device's screen
#     send_cursor_position(pos_x, pos_y)


if __name__ == "__main__":
    # init_socket()
    monitor_cursor()
