import random
from abc import abstractmethod

from src.request.header.header_mutator import HeaderMutator


class CommonHeaderMutator(HeaderMutator):

    def __init__(self, *common_headers: HeaderMutator):
        self.header_mutators = common_headers

    def mutate(self, mutateable=None):
        return self.header_mutators[0].mutate(mutateable)
