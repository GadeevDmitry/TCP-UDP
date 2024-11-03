import socket

def Print_message_from_server(sock):
    message = sock.recv(100)
    if not message:
        return False

    print(message)
    return True

Welcome_from_server = Print_message_from_server
Response_on_attempt = Print_message_from_server

def Client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost", 1000))

    try:
        while True:
            if not Welcome_from_server(sock):
                break

            while True:
                client_attempt = input()[: 100]
                sock.sendall(client_attempt)

                if not Response_on_attempt(sock):
                    break
            break
    finally:
        sock.close()

if __name__ == "__main__":
    Client()
