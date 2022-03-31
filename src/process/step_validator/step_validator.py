from abc import ABC, abstractmethod


class StepValidator(ABC):

    @abstractmethod
    def is_valid(self) -> bool:
        pass
