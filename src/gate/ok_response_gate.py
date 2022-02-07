from src.gate.gate import Gate


class OkResponseGate(Gate):
    def gate(self, response) -> bool:
        return response.status_code == 200
