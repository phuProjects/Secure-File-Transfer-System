import socket

#Host & Port
HOST = "127.0.0.1" #Localhost
PORT = 5001 #Arbitrarily chosen port

#Create a server socket object using default parameters (IPv4 + TCP)
server_socket = socket.socket()

#Bind socket to specific host and port
server_socket.bind((HOST,PORT))

#Start listening for incoming connections (Allowing only one at a time)
server_socket.listen(1)
print(f"[*] Listening on {HOST}:{PORT}...")

#Accept connection from client
conn, addr = server_socket.accept()
print(f"[+] Connection established with {addr}")

#Receive up to 1024 bytes of data from client
data = conn.recv(1024)
print(f"[+] Received encrypted message: {data}")

#Close connection
conn.close()

#Close socket
server_socket.close()