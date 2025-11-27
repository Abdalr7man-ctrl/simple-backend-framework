# Backend Framework

HTTP/1.1

HTTP request --> HTTP Handler -(Middleware)-> URL Router --> View Renderer --> HTTP Handler --> Response

## TODOs

- [ ] use URL like that --> /path/to/{id}
  - hint it will be doing by another object not by dict & pars the `path` and the `parameters`
- [x] OSError: [Errno 98] Address already in use
- [ ] use strip() to remove the space in the values in the headers in http_handler
- [ ] using threading to handle multiple requests
- [ ] is there space in the path URL solve it
