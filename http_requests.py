"""
Hmmmmm
"""

class HttpRequest:
    method = None
    path = None
    headers = {}
    body = None
    params = {}

    def __init__(self, http_plaintext: str) -> None:
        http_lines = http_plaintext.split('\r\n')
        request_line = http_lines[0]
        self.method = request_line.split(' ')[0]
        self.path = request_line.split(' ')[1]
        
        start_body_index = 0

        for line in http_lines[1:]:
            if not line:
                start_body_index = http_lines.index(line) + 1
                break
            pair = line.split(': ')
            self.headers[pair[0]] = pair[1]

        self.body = http_lines[start_body_index:] # body lines in list

class HttpResponse: ...


if __name__ == "__main__":
    myRequest = HttpRequest('GET / HTTP/1.1\r\nHost: 127.0.0.1:8080\r\nUser-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:136.0) Gecko/20100101 Firefox/136.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate, br, zstd\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nSec-Fetch-Dest: document\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: cross-site\r\nPriority: u=0, i\r\n\r\n<h1> Hello World<h1>')
    print(myRequest.method)
    print(myRequest.path)
    print(myRequest.headers)
    print(myRequest.body)
    # print(myRequest.)
