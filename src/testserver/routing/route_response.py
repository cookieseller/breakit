class RouteResponse:
    def __init__(self, code: int, message: dict):
        self.response_code = code
        self.response_json = message
