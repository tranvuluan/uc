# pylint: disable=C0116,C0411,C0301,C0303
import pyautogui
import pygetwindow as gw
import time
import socket
import pyautogui
from screeninfo import get_monitors

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
        pass

def get_cursor_position():
    x, y = pyautogui.position()
    monitors = get_monitors()
    for monitor in monitors:
        if monitor.width != 1920:
            continue
        print("monitor: ", monitor)
        print("position: ", x, y)
        # Calculate the global cursor position by adjusting for the monitor's origin
        if monitor.x <= x < monitor.x + monitor.width and monitor.y <= y < monitor.y + monitor.height:
            return x + monitor.x, y + monitor.y

    return x, y

def on_cursor_reach_edge(x, y):
    print(f"Cursor has reached the edge of the screen at position: ({x}, {y})\n")

def monitor_cursor():
    while True:
        x, y = get_cursor_position()
        print(f"Current cursor position: ({x}, {y})")
        
        screen_width, screen_height = pyautogui.size()
        
        # Check if cursor is at the edge of the screen or in negative space
        if x <= 0 or y <= 0 or x >= screen_width - 1 or y >= screen_height - 1:
            on_cursor_reach_edge(x, y)

        time.sleep(0.2)


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


def on_cursor_reach_edge(pos_x, pos_y):
    # print("Cursor has reached the edge of the screen!")
    # Send cursor to the adjacent device's screen
    send_cursor_position(pos_x, pos_y)


if __name__ == "__main__":
    init_socket()
    monitor_cursor()
