from abc import ABC, abstractmethod


class ResponseParser(ABC):
    @abstractmethod
    def parse(self, expression):
        pass
