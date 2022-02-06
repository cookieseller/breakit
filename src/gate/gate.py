from abc import ABC, abstractmethod


class Gate(ABC):
    @abstractmethod
    def gate(self, expression) -> bool:
        pass
