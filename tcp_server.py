import socket

# Server configuration
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 65432
BUFFER_SIZE = 1024  # Same as client
END_MARKER = '<END>'

def receive_message(client_socket):
    full_message = ''
    while True:
        chunk = client_socket.recv(BUFFER_SIZE).decode()
        if END_MARKER in chunk:
            full_message += chunk.replace(END_MARKER, '')
            break
        full_message += chunk
    return full_message

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(1)

    print(f"Server listening on {SERVER_HOST}:{SERVER_PORT}...")
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connected to {client_address}")
        
        message = receive_message(client_socket)
        print(f"Received message: {message}")

        client_socket.close()

if __name__ == "__main__":
    main()
