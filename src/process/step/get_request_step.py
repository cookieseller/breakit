from src.process.step.step import Step
from src.request.header.header_mutator import HeaderMutator
from src.request.request_factory import RequestFactory


class GetRequestStep(Step):

    def __init__(self, url: str, header_mutator: HeaderMutator) -> None:
        self.url = url
        self.header_mutator = header_mutator

    def get_identifier(self) -> str:
        return f"{self.get_name()}{self.url}"

    def execute(self):
        return RequestFactory().create_get_request(self.url, self.header_mutator.mutate(''))
