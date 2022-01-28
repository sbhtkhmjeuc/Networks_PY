import socket


def SENDER(msg):
    msg_length = len(msg)
    my_socket.send(str(msg_length).encode())
    my_socket.send(str(msg).encode())
    data = my_socket.recv(100000).decode()
    print(data)
    if data == 'DISCONNECTED':
        my_socket.close()
        return 'DISCONNECTED'


my_socket = socket.socket()
my_socket.connect(("127.0.0.1", 8820))

while True:
    user_input = input("Command : ")
    mess = SENDER(user_input)
    if mess == 'DISCONNECTED':
        break


