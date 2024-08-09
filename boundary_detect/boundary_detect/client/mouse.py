from pynput import mouse
from pynput.mouse import Controller
from boundary_detect.client.socket_client import init_socket, send_cursor_position

delta_x = 0

def on_move(x, y):
    # print(f'Mouse moved to ({x}, {y})')
    test_flow(x, y)

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
    mouse = Controller()
    mouse.position = (pos_x, pos_y)
    # Print the current position
    print(f'Mouse moved to {mouse.position}')


def test_flow(pos_x, pos_y):
    global delta_x
    if pos_x > 1919:
        if delta_x < 1000:
            delta_x += 3
        else:
            delta_x = 0
        # print('Reach right screen: ', pos_x, pos_y)
        print(delta_x)
        send_cursor_position(delta_x, 100)
    else:
        delta_x = 0

def main():
    init_socket()
    listener_mouse()

main()