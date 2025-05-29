import socket
from encrypt import encrypt_message


#Data & Encryption
data_to_send = b"Sensitive info" 
encrypted_message = encrypt_message(data_to_send)

#host & port
HOST = "127.0.0.1"
PORT = 5001

#Create client socket object
client_socket = socket.socket()

#Connect to server
client_socket.connect((HOST,PORT))

#Send data to server
client_socket.sendall(encrypted_message)

#Close socket
client_socket.close()