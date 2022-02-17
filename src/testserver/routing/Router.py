from abc import ABC, abstractmethod


class Router(ABC):

    @abstractmethod
    def get_routes(self) -> dict:
        pass
