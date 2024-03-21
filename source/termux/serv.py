import socket
import os
import time

def position(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', port))
    server_socket.listen(1)
    print(f"Listening on port {port}...")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")
    time.sleep(0.5)
    os.system('clear')

    try:
        print('\n ')
        while True:
            data = conn.recv(500)
            if not data:
                break
            print(f"   viewangles: {data.decode('utf-8').strip()}          ", end='\r')
            time.sleep(1)
    finally:
        conn.close()
        server_socket.close()

if __name__ == "__main__":
    port = 1337
    position(port)