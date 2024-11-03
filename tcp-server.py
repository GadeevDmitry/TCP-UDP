import random
import socket

NUMBER_MIN = 1
NUMBER_MAX = 100

def Welcome_client(connect_sock):
    welcome_message = f"Welcome, TCP-client!\nGuess the number from {NUMBER_MIN} to {NUMBER_MAX}."
    connect_sock.sendall(welcome_message)

def Handle_client_attempt(connect_sock, hidden_number, client_attempt):
    response_message = ""
    is_guessed       = False

    while True:
        if not client_attempt.isdigit():
            response_message = "You should print the only number"
            break
        client_number = int(client_attempt)

        if client_number < NUMBER_MIN or client_number > NUMBER_MAX:
            response_message = "Your number is out of range"

        elif client_number == hidden_number:
            response_message = "God damn!\nGame is over! Let's do it again!"
            is_guessed = True

        elif client_number < hidden_number:
            response_message = "Hidden number is larger"

        else:
            response_message = "Hidden number is lower"

        break
    connect_sock.sendall(response_message)

    return is_guessed

def Start_new_game():
    return random.randint(NUMBER_MIN, NUMBER_MAX)

def Server():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock = socket.bind(("server", 1000))

    server_sock.listen(1)
    try:
        while True:
            connect_sock, connect_addr = server_sock.accept()
            Welcome_client(connect_sock)

            try:
                hidden_number = Start_new_game()
                while True:
                    client_attempt = connect_sock.recv(100)
                    if not client_attempt:
                        break

                    if Handle_client_attempt(connect_sock, hidden_number, client_attempt):
                        hidden_number = Start_new_game()
            finally:
                connect_sock.close()
                raise
    finally:
        server_sock.close()

if __name__ == "__main__":
    Server()
