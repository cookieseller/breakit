from src.process.response_parsers.response_parser import ResponseParser


class ResponseCodeExtractor(ResponseParser):
    def __init__(self):
        self.response_code = None

    def parse(self, response) -> None:
        self.response_code = response.status_code
