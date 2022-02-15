import os
import socketserver
from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080


class Server(BaseHTTPRequestHandler):

    def default(self, status, message):
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<tml><head><title>Breakit flow test server</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes(f"<p> {message}.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
        pass

    def do_GET(self):
        routes = {
            "/":        {"function": self.default, "message": "Hello World", "status": 200},
            "/test":    {"function": self.default, "message": "Invalid World", "status": 400},
            "/goodbye": {"function": self.default, "message": "Goodbye World", "status": 200},
            "/create":  {"function": self.default, "message": "Goodbye World", "status": 200},
            "/delete":  {"function": self.default, "message": "Goodbye World", "status": 200},
            "/exists":  {"function": self.default, "message": "Goodbye World", "status": 200}
        }

        routes[self.path]["function"](routes[self.path]['status'], routes[self.path]['message'])


if __name__ == "__main__":
    if os.path.exists('tokens'):
        os.remove("tokens")

    webServer = HTTPServer((hostName, serverPort), Server)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
