from treelib import Tree

from src.process.step.step import Step


class Process:

    def __init__(self) -> None:
        self.last_added = None
        self.tree = Tree()

    def execute(self):
        pass

    def add_step(self, step: Step):
        self.tree.create_node(step, step.get_name(), parent=self.last_added)
        self.last_added = step

    def add_step(self, step: Step, gate):
        self.tree.create_node(step, step.get_name(), parent=self.last_added)

        self.last_added = step.get_name()
