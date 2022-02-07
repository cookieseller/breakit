from typing import Final

from treelib import Tree

from src.gate.gate import Gate
from src.process.step.step import Step


class Process:

    ROOT_IDENTIFIER: Final[str] = "root"

    def __init__(self) -> None:
        self.tree = Tree()
        self.root = self.tree.create_node(identifier=self.ROOT_IDENTIFIER)
        self.last_added_identifier = self.ROOT_IDENTIFIER

    def execute(self) -> None:
        try:
            for step in self.tree.children(self.ROOT_IDENTIFIER):
                process_data = step.data
                result = process_data.get_step().execute()
                process_data.get_gate().gate(result)
        except AttributeError:
            #should never happen if a step was added
            pass

    def add_next_step(self, step: Step, gate) -> None:
        self.tree.create_node(step.get_name(), step.get_identifier(), data=self._ProcessStep(step, gate), parent=self.last_added_identifier)
        self.last_added_identifier = step.get_identifier()

    def add_root_step(self, step: Step, gate) -> None:
        self.tree.create_node(step.get_name(), step.get_identifier(), data=self._ProcessStep(step, gate), parent=self.ROOT_IDENTIFIER)
        self.last_added_identifier = step.get_identifier()

    def add_step_after(self, step: Step, previous_step: Step, gate) -> None:
        self.tree.create_node(step.get_name(), step.get_identifier(), data=self._ProcessStep(step, gate), parent=previous_step.get_identifier())
        self.last_added_identifier = step.get_identifier()

    class _ProcessStep:
        def __init__(self, step: Step, gate: Gate) -> None:
            super().__init__()
            self.step = step
            self.gate = gate

        def get_step(self):
            return self.step

        def get_gate(self):
            return self.gate
