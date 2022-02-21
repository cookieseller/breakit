from src.response_parsers.responseparser import ResponseParser


class VariableExtractor(ResponseParser):
    def __init__(self):
        self.variables = None

    def parse(self, response) -> None:
        pass

    def is_valid(self) -> bool:
        pass
