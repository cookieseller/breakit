from src.process.step_validator.step_validator import StepValidator


class DefaultValidator(StepValidator):
    def is_valid(self) -> bool:
        return True
