from http.server import HTTPServer, BaseHTTPRequestHandler
import json

# Base de datos simulada de vehículos
chocolates = {}


class Chocolate:
    def __init__(self, chocolate_type,weight, flavor,stuffed):
        self.chocolate_type = chocolate_type
        self.weight = weight
        self.flavor = flavor
        self.stuffed=stuffed

class Tablet(Chocolate):
    def __init__(self,weight, flavor):
        super().__init__("tablet",weight, flavor,None)
class Bombon(Chocolate):
    def __init__(self,weight,flavor, stuffed):
        super().__init__("bombon",weight, flavor,stuffed)
class Truffle(Chocolate):
    def __init__(self,weight, flavor, stuffed):
        super().__init__("truffle",weight, flavor,stuffed)




class ChocolateFactory:
    @staticmethod
    def create_chocolate(chocolate_type,weight,flavor, stuffed):
        if chocolate_type == "tablet":
            return Tablet(weight,flavor)
        elif chocolate_type == "bombon":
            return Bombon(weight,flavor,stuffed)
        elif chocolate_type == "truffle":
            return Truffle(weight,flavor,stuffed)
        else:
            raise ValueError("Tipo de chocolate no válido")


class HTTPDataHandler:
    @staticmethod
    def handle_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))

    @staticmethod
    def handle_reader(handler):
        content_length = int(handler.headers["Content-Length"])
        post_data = handler.rfile.read(content_length)
        return json.loads(post_data.decode("utf-8"))


class ChocolateService:
    def __init__(self):
        self.factory = ChocolateFactory()

    def add_chocolate(self, data):
        chocolate_type = data.get("chocolate_type", None)
        weight = data.get("weight",None)
        flavor = data.get("flavor",None)
        stuffed = data.get("stuffed",None)
        chocolate = self.factory.create_chocolate(
            chocolate_type,weight,flavor,stuffed
        )
        #max_valor = max(chocolates, key=lambda x: x["id"])
        if(len(chocolates)==0):
            chocolates[1]=chocolate
        else:
            max_valor = max(chocolates, key=int)
            chocolates[max_valor+1] = chocolate
        #chocolates[len(chocolates) + 1] = chocolate
        return chocolate

    def list_chocolate(self):
        return {index: chocolate.__dict__ for index, chocolate in chocolates.items()}

    def update_chocolate(self, chocolate_id, data):
        if chocolate_id in chocolates:
            chocolate = chocolates[chocolate_id]
            weight = data.get("weight",None)
            flavor = data.get("flavor",None)
            stuffed = data.get("stuffed",None)
            if weight:
                chocolate.weight = weight
            if flavor:
                chocolate.flavor = flavor
            if stuffed :
                chocolate.stuffed = stuffed
            return chocolate
        else:
            raise None

    def delete_chocolate(self, chocolate_id):
        if chocolate_id in chocolates:
            del chocolates[chocolate_id]
            return {"message": "Chocolate eliminado"}
        else:
            return None


class ChocolateRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.chocolate_service = ChocolateService()
        super().__init__(*args, **kwargs)

    def do_POST(self):
        if self.path == "/chocolates":
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.chocolate_service.add_chocolate(data)
            HTTPDataHandler.handle_response(self, 201, response_data.__dict__)
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_GET(self):
        if self.path == "/chocolates":
            response_data = self.chocolate_service.list_chocolate()
            HTTPDataHandler.handle_response(self, 200, response_data)
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_PUT(self):
        if self.path.startswith("/chocolates/"):
            chocolate_id = int(self.path.split("/")[-1])
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.chocolate_service.update_chocolate(chocolate_id, data)
            if response_data:
                HTTPDataHandler.handle_response(self, 200, response_data.__dict__)
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"message": "Chocolate no encontrado"}
                )
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_DELETE(self):
        if self.path.startswith("/chocolates/"):
            chocolate_id = int(self.path.split("/")[-1])
            response_data = self.chocolate_service.delete_chocolate(chocolate_id)
            if response_data:
                HTTPDataHandler.handle_response(self, 200, response_data)
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"message": "chocolate no encontrado"}
                )
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )


def main():
    try:
        server_address = ("", 8000)
        httpd = HTTPServer(server_address, ChocolateRequestHandler)
        print("Iniciando servidor HTTP en puerto 8000...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor HTTP")
        httpd.socket.close()


if __name__ == "__main__":
    main()
