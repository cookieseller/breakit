from abc import ABC, abstractmethod


class ResponseParser(ABC):
    @abstractmethod
    def gate(self, expression) -> bool:
        pass
