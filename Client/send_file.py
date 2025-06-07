#send_file.py
import socket
from encrypt import encrypt_data
import struct
import argparse

#Reads and encrypt file
def read_and_encrypt(file):
    try:
        with open(file, "rb") as f:
            f_data = f.read()
        return encrypt_data(f_data)
    except FileNotFoundError:
        print(f"[!] File not found: {file}")
    except PermissionError:
        print(f"[!] Permission Denied: {file}")
    except Exception as e:
        print(f"[!] Failed to read or encrypt: '{file}': {e}")


#Create parse object
parser = argparse.ArgumentParser()
#Add arguments to parse object
parser.add_argument("-f", "--filename", required=True, help="Name of the file to encrypt and send")
parser.add_argument("-H", "--host", default="127.0.0.1", help="Host to connect to (default: 127.0.0.1)")
parser.add_argument("-P", "--port", default=5001, type=int, help="Choose a port (default: 5001)")
args = parser.parse_args()

filename = args.filename
filename_bytes = filename.encode()
encrypted_data = read_and_encrypt(filename)
if encrypted_data is None:
    print("[!] Abort: could not read or encrypyt file.")
    exit(1) #Exit program (1) = failed

#host & port
HOST = args.host
PORT = args.port


def send_encrypted_file(filename_bytes, encrypted_data, HOST, PORT):
    try:
        #Create client socket object
        client_socket = socket.socket()
        client_socket.settimeout(5) #Set time for connect/send/recv

        #Connect to server
        client_socket.connect((HOST,PORT))

        #Send data to server
        client_socket.sendall(struct.pack('>I', len(filename_bytes))) #convert len of filename into bytes then sending via sendall
        client_socket.sendall(filename_bytes)

        client_socket.sendall(struct.pack('>I', len(encrypted_data))) #convert len of encrypted data into bytes then sending via sendall
        client_socket.sendall(encrypted_data)

    except ConnectionRefusedError:
        print(f"[!] Connection was refused: recheck server")
    
    except socket.gaierror:
        print("[!] Failed to connect: Invalid host name")
    
    except socket.timeout:
        print("[!] Connection timed out")
    
    except OverflowError:
        print("[!] Invalid port number: must be between 0-65535")

    except Exception as e:
        print(f"[!] Failed to send data: {e}")

    finally: #Always making sure socket is closed after
        client_socket.close()

send_encrypted_file(filename_bytes, encrypted_data, HOST, PORT)