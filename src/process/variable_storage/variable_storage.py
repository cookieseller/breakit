from abc import ABC, abstractmethod


class VariableStorage(ABC):
    @abstractmethod
    def set_value(self, key, value):
        pass

    @abstractmethod
    def get_value(self, key):
        pass

    @abstractmethod
    def has_value(self, key):
        pass
