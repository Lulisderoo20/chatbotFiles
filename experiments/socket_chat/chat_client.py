import socket

HOST = "127.0.0.1"
PORT = 8080


def start_client() -> None:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    print(f"Connected to {HOST}:{PORT}. Type 'exit' to quit.")

    try:
        while True:
            message = input("You: ").strip()
            if not message:
                continue
            if message.lower() in {"exit", "quit", "salir"}:
                break
            client.sendall(message.encode("utf-8"))
    finally:
        client.close()


if __name__ == "__main__":
    start_client()
