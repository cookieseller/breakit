from src.process.step_validator.step_validator import StepValidator
from src.process.variable_storage.variable_storage import VariableStorage


class BadRequestResponseGate(StepValidator):

    def __init__(self, variable_storage: VariableStorage):
        self.variable_storage = variable_storage

    def is_valid(self) -> bool:
        # TODO remove has value
        if not self.variable_storage.has_value("response_code"):
            return False

        return self.variable_storage.get_value("response_code") == 400
