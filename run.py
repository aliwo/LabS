from api.app import app as api_app

def dummy_app(environ, start_response):
    data = b"Hello, World!\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])

if __name__ == '__main__':
    api_app.run(host='0.0.0.0', port=8000) 