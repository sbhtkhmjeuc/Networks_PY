import socket
import time

socket2 = socket.socket()
socket2.connect(('127.0.0.1', 8810))
data = socket2.recv(2048).decode()
print(data)
socket2.close()
socket2.close()
time.sleep(1)

socket1 = socket.socket()
socket1.bind(('127.0.0.1', 8820))
socket1.listen()
c, a = socket1.accept()
data = input('mes : ' + str(8820))
c.send(data.encode())