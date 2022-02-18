from src.testserver.routing.Route import Route
from src.testserver.routing.Router import Router
from src.testserver.routing.route_response import RouteResponse


class TestingRouter(Router):
    def get_routes(self) -> dict:
        return {
            'GET':    {
                "/":     TestingRouter.Default,
                "/test": TestingRouter.Test,
            },
            'POST':   {},
            'DELETE': {},
        }

    class Default(Route):
        def execute(self, params: str) -> RouteResponse:
            return RouteResponse(200, 'My default route')

    class Test(Route):
        def execute(self, params: str) -> RouteResponse:
            return RouteResponse(200, 'My Test route')
