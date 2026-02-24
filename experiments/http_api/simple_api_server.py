from http.server import BaseHTTPRequestHandler, HTTPServer
import json

HOST = "127.0.0.1"
PORT = 8000

USERS = [
    {"id": 1, "name": "User1"},
    {"id": 2, "name": "User2"},
]


def build_response(message: str) -> str:
    lower = message.lower()
    if any(word in lower for word in ["hola", "buenas", "hello"]):
        return "Hola. Soy un chatbot API basico."
    if any(word in lower for word in ["precio", "comprar", "pago"]):
        return "Aun no tengo catalogo, pero puedo conectarme a una base de datos despues."
    if any(word in lower for word in ["error", "ayuda", "soporte"]):
        return "Contame el error y lo registramos como siguiente mejora."
    return "Mensaje recibido. Esta es una respuesta basica de experimento."


class SimpleAPIHandler(BaseHTTPRequestHandler):
    def _send_json(self, status_code: int, payload: dict) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        if self.path == "/" or self.path == "/health":
            self._send_json(200, {"status": "ok", "service": "simple_api_server"})
            return

        if self.path == "/users":
            self._send_json(200, {"users": USERS})
            return

        self._send_json(404, {"error": "Not found"})

    def do_POST(self) -> None:
        if self.path != "/chat":
            self._send_json(404, {"error": "Not found"})
            return

        try:
            content_length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            self._send_json(400, {"error": "Invalid content length"})
            return

        if content_length <= 0:
            self._send_json(400, {"error": "Body is required"})
            return

        raw_body = self.rfile.read(content_length)

        try:
            payload = json.loads(raw_body.decode("utf-8"))
        except json.JSONDecodeError:
            self._send_json(400, {"error": "Invalid JSON"})
            return

        message = str(payload.get("message", "")).strip()
        if not message:
            self._send_json(400, {"error": "Field 'message' is required"})
            return

        response = build_response(message)
        self._send_json(200, {"message": message, "response": response})


def run() -> None:
    server_address = (HOST, PORT)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print(f"Starting HTTP chatbot API on http://{HOST}:{PORT}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
