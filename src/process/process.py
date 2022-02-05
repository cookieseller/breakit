from treelib import Tree

from src.process.step.step import Step


class Process:

    def __init__(self) -> None:
        self.last_added = None
        self.tree = Tree()

    def execute(self):
        try:
            step = self.tree.get_node(self.tree.root).data
            return step.execute()
        except AttributeError:
            #should never happen if a step was added
            pass

    def add_step(self, step: Step):
        self.tree.create_node(step.get_name(), step.get_name(), data=step, parent=self.last_added)
        self.last_added = step

    def add_step(self, step: Step, gate):
        self.tree.create_node(step.get_name(), step.get_name(), data=step, parent=self.last_added)

        self.last_added = step.get_name()
