from src.gate.responseparser import ResponseParser


class OkResponseGate(ResponseParser):
    def gate(self, response) -> bool:
        return response.status_code == 200
