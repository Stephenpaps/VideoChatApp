import os
from pyfiglet import Figlet
os.system("clear")
pyf = Figlet(font='puffy')
a = pyf.renderText("Video Chat app")
b = pyf.renderText("Server")
os.system("tput setaf 3")
print(a)

import socket, cv2, pickle, struct

#socket create
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print('HOST IP:', host_ip)
port = 9999
socket_address = (host_ip, port)

#socket bind
server_socket.bind(socket_address)
server_socket.listen(1)
print("Listening at:", socket_address)

#socket accept
while True:
    client_socket, addr = server_socket.accept()
    print('Connected to:', addr)
    if client_socket:
        vid = cv2.VideoCapture(0)

    while(vid.isOpened()):
        ret, image = vid.read()
        img_serialize = pickle.dumps(image)
        message = struct.pack("Q", len(img_serialize))+img_serialize
        client_socket.sendall(message)

        cv2.imshow('Video from Server', image)
        key = cv2.waitKey(10)
        if key == 13 :
            client_socket.close()



