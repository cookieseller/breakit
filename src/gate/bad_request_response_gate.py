from src.gate.responseparser import ResponseParser


class BadRequestResponseGate(ResponseParser):
    def gate(self, response) -> bool:
        return response.status_code == 400
