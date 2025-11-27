from backend.http_server import Server
from backend.http_handler import HttpRequest, HttpResponse


def home(http_request: HttpRequest):
    return HttpResponse(200, 'OK', 'Hello, World!')

def about(http_request: HttpRequest):
    return HttpResponse(200, 'OK', 'Hello, Abdalrhman!', )

# middleware user authentication
def user_auth(request: HttpRequest, view):
    username = request.headers.get('username', None)
    if username != 'abdalrhman':
        # over write on the view(route) request by specific request according to the `username` section in the headers
        return HttpResponse(401, 'Unauthorized', '<h1>not Unauthorized</h1>')
    else:
        # what happen without the middleware
        return view(request)

def profile(request: HttpRequest):
    username = request.headers.get('username')
    return HttpResponse(
        200,
        'OK',
        f'<h1>{username}</h1>'
    )

middlewares = [
    user_auth
]


app = Server({'/': home,
    '/about': about,
    '/profile': profile
}, middlewares=middlewares)

if __name__ == "__main__":
    app.run('0.0.0.0', 8080)
