from src.response_parsers.response_parser import ResponseParser


class VariableExtractor(ResponseParser):
    def __init__(self):
        self.variables = None

    def parse(self, response) -> None:
        pass
