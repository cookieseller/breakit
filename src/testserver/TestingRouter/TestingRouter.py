from src.testserver.routing.Route import Route
from src.testserver.routing.Router import Router


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
        def execute(self, params: str):
            pass

    class Test(Route):
        def execute(self, params: str):
            pass
