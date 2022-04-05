import ast

from src.process.response_parsers.response_parser import ResponseParser
from src.process.variable_storage.variable_storage import VariableStorage


class VariableExtractor(ResponseParser):
    def __init__(self, storage: VariableStorage):
        self.variable_storage = storage

    def parse(self, response):
        content = response.content
        variables = ast.literal_eval(content.decode('utf-8'))

        for key, value in variables.items():
            self.variable_storage.set_value(key, value)
