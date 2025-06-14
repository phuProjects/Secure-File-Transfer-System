#receive_file.py
import socket
from decrypt import decrypt_data
import struct
import argparse

#Constants
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 5001
BUFFER_SIZE = 4096

def parse_args():
    #argparse based CLI 
    parser = argparse.ArgumentParser()
    parser.add_argument("-H", "--host", default="127.0.0.1" , help="Host to bind to (default aka local: 127.0.0.1)")
    parser.add_argument("-P", "--port", default= 5001, type=int, help="Port to listen on (default 5001)")
    return parser.parse_args()

def receive_file(conn):
    try:
        #Receive length of filename 
        filename_len_bytes = conn.recv(4)
        if len(filename_len_bytes) < 4:
            raise ValueError("Incomplete filename length received.")
        filename_len = struct.unpack("!I", filename_len_bytes)[0]

        #Receive filename
        filename_bytes = conn.recv(filename_len)
        if len(filename_bytes) < filename_len:
            raise ValueError("Incomplete filename received.")
        filename = filename_bytes.decode()

        #Receive length of encrypted data
        data_len_bytes = conn.recv(4)
        if len(data_len_bytes) < 4:
            raise ValueError("Incomplete data length received.")
        data_len = struct.unpack("!I", data_len_bytes)[0]

        #Receive encrypted data in chunks
        encrypted_data = b""
        while len(encrypted_data) < data_len:
            try:
                packet = conn.recv(min(BUFFER_SIZE, data_len - len(encrypted_data)))
                if not packet:
                    raise ConnectionError("Connection closed while receiving data")
                encrypted_data += packet
            except socket.timeout:
                print("[!] Timeout while receiving data")
                return
        print("[+]Data has been received")

        #Decrypt and save data
        try:
            decrypted_data = decrypt_data(encrypted_data)
        except Exception as e:
            print(f"[!] Failed to decrypt data: {e}")

        try:
            with open(filename, "wb") as file:
                file.write(decrypted_data)
            print("[+]Successfully saved data")
        except OSError as e:
            print(f"[!] Failed to write to file: {e}")

    except (ValueError, struct.error) as e:
        print(f"[!] Data format error: {e}")
    except ConnectionError as e:
        print(f"[!] Connection error: {e}")
    except Exception as e:
        print(f"[!] Unexpected error: {e}")


def start_server(host,port):

    server_socket = socket.socket()
    server_socket.bind((host,port))

    #Listening for connection
    server_socket.listen(1)
    print(f"[+]Listening on {host}:{port}...")

    #Accept connection from client
    conn, addr = server_socket.accept()
    print(f"[+]Connection established with {addr}")

    #Receive file/data
    receive_file(conn)

    #Close connection & Socket
    conn.close()
    server_socket.close()

def main():
    args = parse_args()
    start_server(args.host, args.port)

if __name__ == "__main__":
    main()
