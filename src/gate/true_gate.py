class TrueGate:
    def gate(self, expression, next_gate):
        if expression():
            next_gate()
