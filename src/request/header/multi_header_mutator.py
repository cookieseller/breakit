from typing import List

from src.request.header.header_mutator import HeaderMutator


class MultiHeaderMutator(HeaderMutator):

    def __init__(self, common_headers: List[HeaderMutator]):
        self.header_mutators = common_headers

    def mutate(self, mutateable=None):
        mutator = self.header_mutators.pop()
        self.header_mutators.append(mutator)

        return mutator.mutate(mutateable)
