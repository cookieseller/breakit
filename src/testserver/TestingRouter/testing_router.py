import os
import random
import string

from src.testserver.routing.route import Route
from src.testserver.routing.route_response import RouteResponse
from src.testserver.routing.router import Router


class TestingRouter(Router):
    def get_routes(self) -> dict:
        return {
            'GET':    {
                "/":              TestingRouter.Default,
                "/start":         TestingRouter.Start,
                "/gettoken":      TestingRouter.GetToken,
                "/validatetoken": TestingRouter.ValidateToken,
                "/end":           TestingRouter.End,
            },
            'POST':   {},
            'DELETE': {},
        }

    class Default(Route):
        def execute(self, params: dict) -> RouteResponse:
            return RouteResponse(200, {'message': 'This is the default route'})

    class Start(Route):
        def execute(self, params: dict) -> RouteResponse:
            return RouteResponse(200, {'message': 'Start route'})

    class GetToken(Route):
        def execute(self, params: dict) -> RouteResponse:
            token = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            f = open("tokens", "a")
            f.writelines([token])
            f.close()

            return RouteResponse(200, {'message': token})

    class ValidateToken(Route):
        def execute(self, params: dict) -> RouteResponse:
            with open("tokens", "r") as f:
                lines = f.readlines()
                for line in lines:
                    if line == params['token'][0]:
                        f.close()
                        return RouteResponse(200, {'message': 'Valid token'})

            f.close()
            return RouteResponse(400, {'message': 'Invalid token'})

    class End(Route):
        def execute(self, params: dict) -> RouteResponse:
            os.remove('tokens')
            return RouteResponse(200, {'message': 'Deleted all tokens'})
