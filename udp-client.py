import socket

def Print_message_from_server(sock):
    message, server_address = sock.recvfrom(100)
    print(message.decode("utf-8"))

Welcome_from_server = Print_message_from_server
Response_on_attempt = Print_message_from_server

def Client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ("localhost", 1000)

    try:
        sock.sendto(str.encode("Start new game"), server_address)
        Welcome_from_server(sock)

        while True:
            client_attempt = input()[: 100]
            sock.sendto(str.encode(client_attempt), server_address)
            Response_on_attempt(sock)
    finally:
        sock.close()

if __name__ == "__main__":
    Client()
