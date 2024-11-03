import random
import socket

NUMBER_MIN = 1
NUMBER_MAX = 100

def Welcome_client(sock, client_addr):
    welcome_message = f"Welcome, UDP-client!\nGuess the number from {NUMBER_MIN} to {NUMBER_MAX}."
    sock.sendto(str.encode(welcome_message), client_addr)

def Handle_client_attempt(sock, client_addr, hidden_number, client_attempt):
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
    sock.sendto(str.encode(response_message), client_addr)

    return is_guessed

def Start_new_game():
    return random.randint(NUMBER_MIN, NUMBER_MAX)

def Server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("localhost", 1000))

    try:
        while True:
            client_message, client_address = sock.recvfrom(100)
            client_message = client_message.decode("utf-8")

            if client_message == "Start new game":
                Welcome_client(sock, client_address)
                hidden_number = Start_new_game()
            elif Handle_client_attempt(sock, client_address, hidden_number, client_message):
                hidden_number = Start_new_game()
    finally:
        sock.close()

if __name__ == "__main__":
    Server()
