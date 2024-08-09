from pynput import mouse
mouse_controller = mouse.Controller()

def on_move(x, y):
    print(f'Mouse moved to ({x}, {y})')

def on_click(x, y, button, pressed):
    print(f'{"Pressed" if pressed else "Released"} at ({x}, {y}) with {button}')

def on_scroll(x, y, dx, dy):
    print(f'Scrolled {"down" if dy < 0 else "up"} at ({x}, {y})')

def listener_mouse():
    # Create a listener for mouse events
    with mouse.Listener(
            on_move=on_move,
            on_click=on_click,
            on_scroll=on_scroll) as listener:
        listener.join()


def control_mouse(pos_x, pos_y):
    mouse_controller.position = (pos_x, pos_y)
    # Print the current position
    print(f'Mouse moved to {mouse.position}')

