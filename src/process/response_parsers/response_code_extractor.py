from src.process.response_parsers.response_parser import ResponseParser
from src.process.variable_storage.variable_storage import VariableStorage


class ResponseCodeExtractor(ResponseParser):

    def __init__(self, variable_storage: VariableStorage):
        self.variable_storage = variable_storage

    def parse(self, response):
        self.variable_storage.set_value("response_code", response.status_code)
