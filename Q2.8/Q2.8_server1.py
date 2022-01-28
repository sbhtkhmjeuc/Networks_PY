import socket
import time

socket2 = socket.socket()
socket2.bind(('127.0.0.1', 8810))
socket2.listen()
c, a = socket2.accept()
data = input('mes : ' + str(8810) + ' ')
c.send(data.encode())
c.close()
socket2.close()
time.sleep(1)

socket1 = socket.socket()
socket1.connect(('127.0.0.1', 8820))
data = socket1.recv(2048).decode()
print(data)