from http.server import HTTPServer, BaseHTTPRequestHandler
import json
estudiantes=[
    {
        "id":1,
        "nombre":"P",
        "apellido":"G",
        "carrera":"Sistemas",
    },
]
class RESTRequestHandler(BaseHTTPRequestHandler):
    def do_Get(self):
        if self.path == "/lista_estudiantes":
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode('utf-8'))
        else:
            self.send_response(404)
def run_server(port = 8000):
    try:
        server_address=('',port)
        httpd= HTTPServer(server_address, RESTRequestHandler)
        print(f'Iniciando servidor web en http://localhost:{port}/')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor WEB")
        httpd.socket.close()

if __name__=="__main__":
    run_server()