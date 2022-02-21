from abc import ABC, abstractmethod


class ResponseParser(ABC):
    @abstractmethod
    def parse(self, expression) -> bool:
        pass

    @abstractmethod
    def is_valid(self) -> bool:
        pass
