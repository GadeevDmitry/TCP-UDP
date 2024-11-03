import socket

DEBUG_PRINT = print

def Print_message_from_server(sock):
    message = sock.recv(100)
    if not message:
        return False

    print(message.decode("utf-8"))
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

                DEBUG_PRINT("DEBUG: sending attempt:\n", client_attempt, "\n======")
                sock.sendall(str.encode(client_attempt))

                if not Response_on_attempt(sock):
                    break
            break
    finally:
        DEBUG_PRINT("DEBUG: closing connection with server", "\n======")
        sock.close()

if __name__ == "__main__":
    Client()
