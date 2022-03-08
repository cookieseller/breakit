from abc import ABC, abstractmethod


class Mutator(ABC):
    @abstractmethod
    def mutate(self, mutateable):
        pass
