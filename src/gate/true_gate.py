from src.gate.gate import Gate


class TrueGate(Gate):
    def gate(self, expression) -> bool:
        return expression()

