from src.response_parsers.responseparser import ResponseParser


class BadRequestResponseGate(ResponseParser):
    def __init__(self):
        self.status_code = None

    def parse(self, response) -> None:
        self.status_code = response.status_code

    def is_valid(self) -> bool:
        return self.status_code == 400
