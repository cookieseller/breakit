from src.gate.gate import Gate


class FalseGate(Gate):
    def gate(self, expression) -> bool:
        return not expression()
