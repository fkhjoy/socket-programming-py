import socket

import socket

BUFFER_SIZE = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECT"
SERVER = "192.168.0.113"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send_msg(msg):
    msg = msg.encode(FORMAT)
    msg_length = len(msg)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' '* (BUFFER_SIZE - len(send_length))
    client.send(send_length)
    client.send(msg)

send_msg("Hello World!")

send_msg(DISCONNECT_MSG)
    