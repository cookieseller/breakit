import random
import string
from abc import ABC, abstractmethod


class StringLengthMutator(ABC):
    @abstractmethod
    def mutate(self, mutateable):
        letters = string.ascii_lowercase
        mutateable.join(random.choice(letters))

        return mutateable
