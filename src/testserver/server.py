import os
import socketserver
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Type
from urllib.parse import parse_qs, urlparse

from src.testserver.TestingRouter.TestingRouter import TestingRouter
from src.testserver.routing.Route import Route
from src.testserver.routing.Router import Router

hostName = "localhost"
serverPort = 8080


class Server(BaseHTTPRequestHandler):

    routes = {
        'GET': {},
        'POST': {},
        'DELETE': {},
    }

    @staticmethod
    def register_routes(routers: list[Router]):
        for router in routers:
            routes = router.get_routes()
            Server.routes['GET'] |= routes['GET']
            Server.routes['POST'] |= routes['POST']
            Server.routes['DELETE'] |= routes['DELETE']

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

    def get_route(self, method: str, path: str) -> Type[Route]:
        return Server.routes[method][path]

    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)

        route = self.get_route('GET', self.path)
        route().execute(query_components)


if __name__ == "__main__":
    if os.path.exists('tokens'):
        os.remove("tokens")

    webServer = HTTPServer((hostName, serverPort), Server)
    Server.register_routes([TestingRouter()])
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
