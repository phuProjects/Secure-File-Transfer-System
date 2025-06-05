#receive_file.py
import socket
from decrypt import decrypt_data
import struct
import argparse

#Host & Port
parser = argparse.ArgumentParser()
parser.add_argument("-H", "--host", required=True, help="Host to bind to (default aka local: 127.0.0.1)")
parser.add_argument("-P", "--port", required=True, help="Port to listen on (default 5001)")
args = parser.parse_args()
HOST = args.host
PORT = args.port

#server socket object using default parameters (IPv4 + TCP)
server_socket = socket.socket()

#Bind socket to specific host and port
server_socket.bind((HOST,PORT))

#Start listening for incoming connections (Allowing only one at a time)
server_socket.listen(1)
print(f"[+]Listening on {HOST}:{PORT}...")

#Accept connection from client
conn, addr = server_socket.accept()
print(f"[+]Connection established with {addr}")

#Step 1: Receive length of filename 
filename_len_bytes = conn.recv(4)
filename_len = struct.unpack("!I", filename_len_bytes)[0]

#Step 2: Receive filename
filename_bytes = conn.recv(filename_len)
filename = filename_bytes.decode()
#---------------------
#Receive length of encrypted data
#---------------------
data_len_bytes = conn.recv(4)
data_len = struct.unpack("!I", data_len_bytes)[0]

#---------------------
#Receive encrypted data in chunks
#---------------------
encrypted_data = b""
while len(encrypted_data) < data_len:
    packet = conn.recv(min(4096, data_len - len(encrypted_data)))
    if not packet:
        break
    encrypted_data += packet
print("[+]Data has been received")
#---------------------
#Decrypt and save data
#---------------------
decrypted_data = decrypt_data(encrypted_data)

with open(filename, "wb") as file:
    file.write(decrypted_data)
print("[+]Successfully saved data")
#---------------------
#Close connection & Socket
#---------------------
conn.close()
server_socket.close()