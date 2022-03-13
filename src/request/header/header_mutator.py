from abc import ABC, abstractmethod


class HeaderMutator(ABC):
    @abstractmethod
    def mutate(self, mutateable):
        pass
