import socket

# Server configuration
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 65432
BUFFER_SIZE = 1024  # Same as client
END_MARKER = '<END>'

def receive_message(server_socket):
    full_message = ''
    while True:
        chunk, _ = server_socket.recvfrom(BUFFER_SIZE)
        chunk = chunk.decode()
        if END_MARKER in chunk:
            full_message += chunk.replace(END_MARKER, '')
            break
        full_message += chunk
    return full_message

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((SERVER_HOST, SERVER_PORT))

    print(f"Server listening on {SERVER_HOST}:{SERVER_PORT}...")
    while True:
        message = receive_message(server_socket)
        print(f"Received message: {message}")

if __name__ == "__main__":
    main()
