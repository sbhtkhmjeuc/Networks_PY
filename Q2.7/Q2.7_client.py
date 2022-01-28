import socket
import time

def IMAGE_RECIVER():
    file = open('image_from_server.jpg', "wb+")
    time.sleep(2)
    num3 = int(my_socket.recv(64).decode())
    print(num3)
    num4 = num3 / 10
    while num3 > 0:
        image_chanck = my_socket.recv(int(num4))
        file.write(image_chanck)
        num3 -= num4
    print('Loading CLIANT')
    return None


def RECIVER():
    global data2
    data = my_socket.recv(64).decode()
    if int(data) > 1:
        data1 = int(data)
        while data1 > 0:
            data27 = my_socket.recv(64).decode()
            data2 = my_socket.recv(int(data27)).decode()
            print(data2)
            data1 -= 1
    else:
        data = my_socket.recv(64).decode()
    return data


def SENDER(msg):
        msg_length = len(msg)
        my_socket.send(str(msg_length).encode())
        my_socket.send(str(msg).encode())
        data3 = RECIVER()
        if data3 == 'DISCONNECTED':
            my_socket.close()
            print('DISCONNECTED FROM THE SERVER')
            return 'DISCONNECTED'
        elif data3 == 'SEND':
            IMAGE_RECIVER()
        else:
            print(data3)


my_socket = socket.socket()
my_socket.connect(("127.0.0.1", 8820))

while True:
    user_input = input("Command : ")
    mess = SENDER(user_input)
    if mess == 'DISCONNECTED':
        break


