from abc import ABC, abstractmethod


class Step(ABC):
    def get_name(self) -> str:
        return type(self).__name__

    @abstractmethod
    def get_identifier(self) -> str:
        pass

    @abstractmethod
    def execute(self):
        pass