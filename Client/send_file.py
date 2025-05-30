import socket
from encrypt import encrypt_data


#Reads and encrypt file
def read_and_encrypt(filename):
    with open(filename, "rb") as file:
        file_data = file.read()
    return encrypt_data(file_data)

encrypted_data = read_and_encrypt("tiny_image.png")

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