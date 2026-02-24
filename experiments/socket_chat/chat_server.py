import socket
import threading

HOST = "0.0.0.0"
PORT = 8080


def handle_client(client_socket: socket.socket, addr: tuple[str, int]) -> None:
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            message = data.decode("utf-8", errors="replace")
            print(f"[{addr[0]}:{addr[1]}] {message}")
    finally:
        client_socket.close()


def start_server() -> None:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"[*] Server listening on {HOST}:{PORT}")

    try:
        while True:
            client, addr = server.accept()
            print(f"[*] Connection accepted from {addr[0]}:{addr[1]}")
            client_handler = threading.Thread(
                target=handle_client,
                args=(client, addr),
                daemon=True,
            )
            client_handler.start()
    except KeyboardInterrupt:
        print("\n[*] Stopping socket server")
    finally:
        server.close()


if __name__ == "__main__":
    start_server()
