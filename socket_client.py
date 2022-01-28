import socket
my_socket = socket.socket()
my_socket.connect(("127.0.0.1",8820))

user_input = input("Please write something to the server: ")
my_socket.send(user_input.encode())
data = my_socket.recv(1024).decode()
print(data)
my_socket.close()
user_input.close()
