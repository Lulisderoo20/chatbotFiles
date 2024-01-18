import socket

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 8080))

    while True:
        message = input("Escribe tu mensaje: ")
        client.send(message.encode('utf-8'))

if __name__ == "__main__":
    start_client()
