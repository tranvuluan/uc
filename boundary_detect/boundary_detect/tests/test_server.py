import pyautogui
import math
import time


def move_cursor():
    # Set the center of the circle
    center_x = 500
    center_y = 500

    # Set the radius of the circle
    radius = 200

    # Move the cursor in a circular motion
    for angle in range(0, 360):
        x = center_x + radius * math.cos(math.radians(angle))
        y = center_y + radius * math.sin(math.radians(angle))
        pyautogui.moveTo(x, y)
        time.sleep(0.01)  # Add a short delay to control the speed of the cursor

move_cursor()