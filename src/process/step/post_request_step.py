from src.process.step.step import Step
from src.request.body.mutator.body_mutator import BodyMutator
from src.request.header.header_mutator import HeaderMutator
from src.request.request_factory import RequestFactory


class GetRequestStep(Step):

    def __init__(self, url: str, header_mutator: HeaderMutator = None, body_mutator: BodyMutator = None) -> None:
        self.url = url
        self.request = RequestFactory().create_post_request(url)
        self.header_mutator = header_mutator
        self.body_mutator = body_mutator

    def get_identifier(self) -> str:
        return f"{self.get_name()}{self.url}"

    def execute(self):
        return self.request()
