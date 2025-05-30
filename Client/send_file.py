import socket
from encrypt import encrypt_data


#Data & Encryption
with open("tiny_image.png", "rb") as file:
    file_data = file.read()

encrypted_data = encrypt_data(file_data)

#host & port
HOST = "127.0.0.1"
PORT = 5001

#Create client socket object
client_socket = socket.socket()

#Connect to server
client_socket.connect((HOST,PORT))

#Send data to server
client_socket.sendall(encrypted_data)

#Close socket
client_socket.close()