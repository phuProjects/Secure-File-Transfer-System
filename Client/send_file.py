import socket
from encrypt import encrypt_data
import struct

#Reads and encrypt file

def read_and_encrypt(file):
    with open(file, "rb") as f:
        f_data = f.read()
    return encrypt_data(f_data)

filename = "tiny_image.png"
filename_bytes = filename.encode()
encrypted_data = read_and_encrypt(filename)


#host & port
HOST = "127.0.0.1"
PORT = 5001

#Create client socket object
client_socket = socket.socket()

#Connect to server
client_socket.connect((HOST,PORT))

#Send data to server
client_socket.sendall(struct.pack('>I', len(filename_bytes))) #convert len of filename into bytes then sending via sendall
client_socket.sendall(filename_bytes)

client_socket.sendall(struct.pack('>I', len(encrypted_data))) #convert len of encrypted data into bytes then sending via sendall
client_socket.sendall(encrypted_data)

#Close socket
client_socket.close()