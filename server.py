import socket
import threading

BUFFER_SIZE = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())

ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"New connection {addr}")

    connected = True 

    while connected:
        msg_length = int(conn.recv(BUFFER_SIZE).decode(FORMAT))
        msg = conn.recv(msg_length).decode(FORMAT)

        if msg == DISCONNECT_MSG:
            connected = False 
        
        print(f"{addr} {msg}")

    conn.close()


def start():
    server.listen()
    print(f"Server is listening on {SERVER}")
    
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"Active connections {threading.activeCount() - 1}")


print("Server is starting....")
start()