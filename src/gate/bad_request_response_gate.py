from src.gate.gate import Gate


class BadRequestResponseGate(Gate):
    def gate(self, response) -> bool:
        return response.status_code == 400
