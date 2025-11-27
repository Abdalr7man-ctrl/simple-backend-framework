import socket
import json
from .http_handler import HttpRequest, HttpResponse


class Server:
    def __init__(self, URLs: dict, middlewares: list) -> None:
        self.socket_server = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
            )
        self.socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.URLs = URLs
        self.middlewares = middlewares

    def run(self, HOST: str, PORT: int):
        self.socket_server.bind((HOST, PORT))
        self.socket_server.listen()
        print(f"The server is run at http://{HOST}:{PORT}")

        while True:
            try:
                client, addr = self.socket_server.accept()
                packets = client.recv(1024)

                http_request = packets.decode()
                request = HttpRequest(http_request)

                try:
                    # http_response = self.URLs[request.path](request)
                    for middleware in self.middlewares:
                        view = self.URLs[request.path]
                        http_response = middleware(request, view)
                except KeyError:
                    http_response = HttpResponse(404, 'Not Found', '<h1>Not Found Page 404</h1>')

                print(request.method, request.path, "HTTP/1.1")

                client.send(http_response.to_http_response.encode())

                client.close()
            except KeyboardInterrupt:
                print("\nBey Bey...")
                break
