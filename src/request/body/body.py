from abc import ABC, abstractmethod


class Body(ABC):
    @abstractmethod
    def get_body(self) -> dict:
        pass
