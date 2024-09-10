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
        client_socket.sendto(chunk.encode(), (SERVER_HOST, SERVER_PORT))
        total_sent += BUFFER_SIZE
    client_socket.sendto(END_MARKER.encode(), (SERVER_HOST, SERVER_PORT))  # Send end marker to indicate end of message

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    message = "A"*100000
    send_message(message, client_socket)

    client_socket.close()

if __name__ == "__main__":
    main()
