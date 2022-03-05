from src.process.step_validator.step_validator import StepValidator


class BadRequestResponseGate(StepValidator):
    def __init__(self, parsed_response):
        self.status_code = parsed_response["response_code"] if "response_code" in parsed_response else None

    def is_valid(self) -> bool:
        return self.status_code == 400
