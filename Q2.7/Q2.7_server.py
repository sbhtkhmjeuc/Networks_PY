import socket
import glob
import time
import os
import shutil
import subprocess
import pyautogui

def IMAGE_SENDER():
    file = open('image.jpg', "rb+")
    image_data = file.read(2048)
    num3 = os.stat('image.jpg').st_size
    print(num3)
    time.sleep(1)
    num4 = num3/10
    client_socket.send(str(num3).encode())
    time.sleep(2)
    while num3 > 0:
        client_socket.send(image_data)
        image_data = file.read(int(num4))
        num3 -= num4
    print('Loading SERVER')

def SENDER(file_path, num=1):
    client_socket.send(str(num).encode())
    if num > 1:
        while num - 1 > 0:
            num -= 1
            for file in file_path:
                client_socket.send(str(len(file)).encode())
                time.sleep(1)
                client_socket.send(file.encode())
    elif file_path == 'SEND':
        client_socket.send(f'{file_path}'.encode())
        IMAGE_SENDER()
    else:
        client_socket.send(f'{file_path}'.encode())

def RECIVER():
    data = client_socket.recv(32).decode()
    if data is None or int(data) > 4294967296:
        client_socket.send("Error number".upper().encode())
        return None
    new_data_size = int(data)
    data = client_socket.recv(new_data_size).decode()
    return data


s = socket.socket()
s.bind(("127.0.0.1", 8820))
s.listen()
client_socket, a = s.accept()

while True:
    try:
        data = RECIVER()
        if data.find("DIR") == 0:
            command_file = data.rsplit()
            file_path = glob.glob(rf'{command_file[1]}\*.*')
            file_path_num = len(file_path)
            SENDER(file_path, file_path_num)

        elif data.find("DELETE") == 0:
            command_file = data.rsplit()
            os.remove(rf'{command_file[1]}')
            SENDER('File Removed')

        elif data.find("COPY") == 0:
            command_file = data.rsplit()
            shutil.copy(rf'{command_file[1]}', rf'{command_file[2]}')
            SENDER('File Copied')

        elif data.find("EXECUTE") == 0:
            command_file = data.rsplit()
            subprocess.run(rf'python "{command_file[1]}"', shell=True)
            SENDER('Executed')

        elif data == 'EXIT':
            SENDER("Disconnected".upper())
            time.sleep(1)
            client_socket.close()

        elif data.find("SCREENSHOT") == 0:
            image5 = pyautogui.screenshot()
            image5.save('image.jpg')
            SENDER('Took Image')

        elif data == "SEND":
            SENDER('SEND')

        else:
            SENDER('FALSE COMMEND')
            time.sleep(1)

    except OSError:
        print('Client Disconnected')
        s.close()
        break
