from typing import Final

from treelib import Tree
from treelib.exceptions import DuplicatedNodeIdError

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
                for gate in process_data.get_gates():
                    if gate.gate(result):
                        self.tree.children(step.get_identifier())

        except AttributeError:
            #should never happen if a step was added
            pass

    def add_root_step(self, step: Step):
        process_step = self.ProcessStep(step)
        self.tree.create_node(step.get_name(), step.get_identifier(), data=process_step, parent=self.ROOT_IDENTIFIER)
        self.last_added_identifier = step.get_identifier()

        return process_step

    def add_next_step(self, step: Step):
        process_step = self.ProcessStep(step)
        try:
            self.tree.create_node(step.get_name(), step.get_identifier(), data=process_step, parent=self.last_added_identifier)
        except DuplicatedNodeIdError:
            pass  # This step already existed, don't add it again

        self.last_added_identifier = step.get_identifier()

        return process_step

    def add_step_after(self, step: Step, previous_step: Step):
        process_step = self.ProcessStep(step)
        try:
            self.tree.create_node(step.get_name(), step.get_identifier(), data=process_step, parent=previous_step.get_identifier())
        except DuplicatedNodeIdError:
            pass  # This step already existed, don't add it again

        self.last_added_identifier = step.get_identifier()

        return process_step

    class ProcessStep:
        def __init__(self, step: Step) -> None:
            super().__init__()
            self.step = step
            self.gates = []

        def add_expected_response(self, gate: Gate):
            self.gates.append(gate)

        def get_step(self):
            return self.step

        def get_gates(self):
            return self.gates
