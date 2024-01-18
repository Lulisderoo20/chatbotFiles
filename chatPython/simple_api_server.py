from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Datos de ejemplo (simulación de una base de datos)
data = {'usuarios': [{'id': 1, 'nombre': 'Usuario1'}, {'id': 2, 'nombre': 'Usuario2'}]}

class SimpleAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Configurar encabezados de respuesta
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # Devolver datos en formato JSON
        response_data = json.dumps(data)
        self.wfile.write(response_data.encode('utf-8'))

# Configurar y ejecutar el servidor
def run():
    port = 8000
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print(f'Iniciando servidor en el puerto {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
