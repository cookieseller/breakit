from abc import ABC, abstractmethod


class BodyMutator(ABC):
    @abstractmethod
    def mutate(self, mutateable):
        pass
