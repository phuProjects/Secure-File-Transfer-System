import socket

from encrypt import encrypted_message

#host & port
HOST = "127.0.0.1"
PORT = 5001

#Create client socket object
client_socket = socket.socket()

#Connect to server
client_socket.connect((HOST,PORT))

#Send data to server
client_socket.sendall(encrypted_message)
print("Sending encrypted message: " + encrypted_message.decode())

#Close socket
client_socket.close()