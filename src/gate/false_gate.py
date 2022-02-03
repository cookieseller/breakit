class FalseGate:
    def gate(self, expression, next_gate):
        if not expression():
            next_gate()
