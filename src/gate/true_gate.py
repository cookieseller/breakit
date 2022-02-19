from src.gate.responseparser import ResponseParser


class TrueGate(ResponseParser):
    def gate(self, expression) -> bool:
        return expression()

