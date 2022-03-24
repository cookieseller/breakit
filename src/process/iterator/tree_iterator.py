from abc import ABC, abstractmethod

from treelib import Tree


class TreeIterator(ABC):
    @abstractmethod
    def get_next_step(self, tree: Tree, previous_step_identifier):
        pass