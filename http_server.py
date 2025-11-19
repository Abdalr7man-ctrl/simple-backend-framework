import socket
import json
from http_handler import HttpRequest, HttpResponse # XXX: .http_handler


class Server:
    def __init__(self, URLs: dict) -> None:
        self.socket_server = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
            )
        self.URLs = URLs

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
                    http_response = self.URLs[request.path](request=request)
                except KeyError:
                    http_response = HttpResponse(404, 'Not Found', '<h1>Not Found Page 404</h1>')

                print(request.method, request.path, "HTTP/1.1")

                client.send(http_response.body.encode())

                client.close()
            except KeyboardInterrupt:
                print("\nBey Bey...")
                break


# solve this problem `search about the reason`
# TODO: OSError: [Errno 98] Address already in use
# TODO: use strip() to remove the space in the values in the headers in http_requests
# TODO: is there space in the path URL solve it
