from datetime import date
import socket
import random
import time


def RECIVER1():
    data = client_socket.recv(32).decode()
    if data is None:
        client_socket.send("Error number".upper().encode())
        time.sleep(1)
        return None
    new_data_size = int(data)
    data = client_socket.recv(new_data_size).decode()

    if data == 'TIME':
        client_socket.send(str(date.today()).encode())
    elif data == 'RAND':
        client_socket.send(str(random.randint(1, 10)).encode())
    elif data == 'EXIT':
        client_socket.send("Disconnected".upper().encode())
        time.sleep(1)
        client_socket.close()
    elif data == 'NAME':
        client_socket.send(bytes("Daniel's Server".encode()))
    else:
        client_socket.send("False Command".upper().encode())
        time.sleep(1)
        return None


sock = socket.socket()
sock.bind(('127.0.0.1', 8820))
sock.listen()
client_socket, address = sock.accept()

while True:
    try:
        RECIVER1()
    except OSError:
        print('Client Disconnected')
        sock.close()
        break
