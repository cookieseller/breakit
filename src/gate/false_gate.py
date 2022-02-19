from src.gate.responseparser import ResponseParser


class FalseGate(ResponseParser):
    def gate(self, expression) -> bool:
        return not expression()
