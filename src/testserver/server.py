import socketserver
from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080


class Server(BaseHTTPRequestHandler):


    def do_GET(self):
        routes = {
            "/":        {"message": "Hello World", "status": 200},
            "/test":    {"message": "Invalid World", "status": 400},
            "/goodbye": {"message": "Goodbye World", "status": 200}
        }

        self.send_response(routes[self.path]["status"])
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<tml><head><title>Breakit flow test server</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes(f"<p> {routes[self.path]['message']}.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), Server)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
