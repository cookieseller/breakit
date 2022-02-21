from typing import Final, List

from treelib import Tree
from treelib.exceptions import DuplicatedNodeIdError

from src.response_parsers.responseparser import ResponseParser
from src.process.step.step import Step


class Process:

    ROOT_IDENTIFIER: Final[str] = "root"

    def __init__(self) -> None:
        self.tree = Tree()
        self.root = self.tree.create_node(identifier=self.ROOT_IDENTIFIER)
        self.last_added_identifier = self.ROOT_IDENTIFIER

    def execute(self, node_identifier: str = ROOT_IDENTIFIER) -> None:
        try:
            for step in self.tree.children(node_identifier):
                process_data = step.data
                result = process_data.get_step().execute()
                for response_parser in process_data.get_response_parsers():
                    response_parser.parse(result)
                    if response_parser.is_valid():
                        self.execute(process_data.get_step().get_identifier())

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
            self.response_parsers = []

        def add_response_handler(self, response_parser: ResponseParser):
            self.response_parsers.append(response_parser)
            return self

        def add_response_parser(self, response_parser: ResponseParser):
            self.response_parsers.append(response_parser)
            return self

        def get_step(self) -> Step:
            return self.step

        def get_response_parsers(self) -> List[ResponseParser]:
            return self.response_parsers
