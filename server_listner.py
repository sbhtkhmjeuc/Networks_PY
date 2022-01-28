# this code answer 2.2 and 2.3 Q's
import socket
sock = socket.socket()  # Creating a New Socket#socket.AF_INET : sending in IPv4 | socket.SOCK_STREAM : TCP Connection
sock.bind(('127.0.0.1', 8820))  # binding the new socket into an Address | "TUPLE"
sock.listen()  # become a server socket | after the connection you can print a statement on the screen |
# the number inside the listen() is representing how many connections can be waiting without being accepted
clientsocket, address = sock.accept()  # accept connections from outside
hello = "Hello "
data = clientsocket.recv(2048)  # putting the data inside if variable that can hold up to 1024 bytes
print(clientsocket)
clientsocket.send(bytes(hello.encode()) + bytes(data))  # sending the message back
sock.close()  # clearing the port of the OS to use


