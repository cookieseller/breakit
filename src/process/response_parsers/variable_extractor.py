import ast

from src.process.response_parsers.response_parser import ResponseParser


class VariableExtractor(ResponseParser):
    def __init__(self):
        self.variables = None

    def parse(self, response) -> None:
        content = response.content
        self.variables = ast.literal_eval(content.decode('utf-8'))
