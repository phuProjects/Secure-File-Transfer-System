import socket
from encrypt import encrypt_data
import struct
import argparse

#Reads and encrypt file
def read_and_encrypt(file):
    with open(file, "rb") as f:
        f_data = f.read()
    return encrypt_data(f_data)

#Create parse object
parser = argparse.ArgumentParser()
#Add arguments to parse object
parser.add_argument("-f", "--filename", required=True, help="Name of the file to encrypt and send")
parser.add_argument("-H", "--host", required=True, help="Host to connect to")
parser.add_argument("-P", "--port", required=True, type=int, help="Choose a port")

args = parser.parse_args()

filename = args.filename
filename_bytes = filename.encode()
encrypted_data = read_and_encrypt(filename)


#host & port
HOST = args.host
PORT = args.port

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