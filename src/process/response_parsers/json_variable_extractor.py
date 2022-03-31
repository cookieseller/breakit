import ast

from src.process.response_parsers.response_parser import ResponseParser
from src.process.variable_storage.variable_storage import VariableStorage


class VariableExtractor(ResponseParser):
    def __init__(self, storage: VariableStorage):
        self.variables = None

    def parse(self, response):
        content = response.content
        self.variables = ast.literal_eval(content.decode('utf-8'))

        return self.variables
