import socket
import json

socket_server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
    )

HOST = '0.0.0.0'
PORT = 8080

socket_server.bind((HOST, PORT))

print(f"The server is run at http://{HOST}:{PORT}")

socket_server.listen()

def create_response(msg, response_statutes="200 OK"):
    return f"""HTTP/1.1 {response_statutes}
content-type: text/html

{msg}
        """

while True:
    try:
        client, addr = socket_server.accept()
        packets = client.recv(1024)

        # to see the raw text
        # print(packets, end='\n\n\n\n\n')

        http_request = packets.decode()
        print(http_request)

        status_line = http_request.split('\n')[0]
        path = status_line.split(' ')[1]

        http_response = ''

        if path == '/':
            http_response = create_response('<h1> Hello, Root! <h1>')
        elif path == '/home':
            http_response = create_response('<h1> Hello, Home! <h1>')
        else:
            http_response = create_response('<h1> Error Page Not Found :(<h1>', '404 Not Found')

        client.send(http_response.encode())

        client.close()
    except KeyboardInterrupt:
        print("\nBey Bey...")
        break

# solve this problem `search about the reason`
# TODO: OSError: [Errno 98] Address already in use
