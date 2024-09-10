import socket

# Client configuration
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 65432
BUFFER_SIZE = 1024  # Adjust as needed
END_MARKER = '<END>'

def send_message(message, client_socket):
    total_sent = 0
    while total_sent < len(message):
        chunk = message[total_sent:total_sent + BUFFER_SIZE]
        client_socket.sendall(chunk.encode())
        total_sent += BUFFER_SIZE
    client_socket.sendall(END_MARKER.encode())  # Send end marker to indicate end of message

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    message = "A" * 2000000
    send_message(message, client_socket)
    
    client_socket.close()

if __name__ == "__main__":
    main()
