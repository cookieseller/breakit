from src.process.step_validator.step_validator import StepValidator


class BadRequestResponseGate(StepValidator):
    def __init__(self):
        self.status_code = None

    def is_valid(self) -> bool:
        return self.status_code == 400
