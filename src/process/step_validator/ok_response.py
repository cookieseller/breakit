from src.process.step_validator.step_validator import StepValidator


class OkResponseGate(StepValidator):
    def __init__(self, parsed_response):
        self.status_code = parsed_response.status_code

    def is_valid(self) -> bool:
        return self.status_code == 200
