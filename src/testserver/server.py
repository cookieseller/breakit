import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Type
from urllib.parse import parse_qs, urlparse

from src.testserver.TestingRouter.testing_router import TestingRouter
from src.testserver.routing.route import Route
from src.testserver.routing.router import Router
from src.testserver.routing.route_response import RouteResponse

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

    @staticmethod
    def get_route(method: str, path: str) -> Type[Route]:
        return Server.routes[method][path]

    def write_response(self, route_response: RouteResponse):
        self.send_response(route_response.response_code)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(route_response.response_json).encode('utf-8'))

    def do_GET(self):
        parsed_url = urlparse(self.path)
        query_components = parse_qs(parsed_url.query)

        route = self.get_route('GET', parsed_url.path)
        route_response = route().execute(query_components)
        self.write_response(route_response)


if __name__ == "__main__":

    webServer = HTTPServer((hostName, serverPort), Server)
    Server.register_routes([TestingRouter()])
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
