from abc import ABC, abstractmethod


class StepValidator(ABC):
    def __init__(self, parsed_response):
        self.parsed_response = parsed_response

    @abstractmethod
    def is_valid(self) -> bool:
        pass
