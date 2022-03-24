from treelib import Tree

from src.process.iterator.tree_iterator import TreeIterator


class DFSTreeIterator(TreeIterator):

    def get_next_step(self, tree: Tree, previous_step_identifier):
        for step in tree.children(previous_step_identifier):
            yield step.data



