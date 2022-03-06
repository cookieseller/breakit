from src.process.step_validator.step_validator import StepValidator


class BadRequestResponseGate(StepValidator):
    def is_valid(self) -> bool:
        response_code = self.parsed_response["response_code"] if "response_code" in self.parsed_response else None
        return response_code == 400
