from src.process.response_parsers.response_parser import ResponseParser


class ResponseCodeExtractor(ResponseParser):

    def parse(self, response) -> dict:
        return {"response_code": response.status_code}
