import socket

client_socket = None
def init_socket():
    global client_socket
    # target_ip = "0.0.0.0"
    target_ip = "192.168.1.8"
    target_port = 9999
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((target_ip, target_port))
        print("client connected")
        return client_socket
    except socket.error:
        print('Init socket fail')
        pass


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