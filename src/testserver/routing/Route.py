from abc import ABC, abstractmethod


class Route(ABC):

    @abstractmethod
    def execute(self, params: dict):
        pass
