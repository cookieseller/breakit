from src.process.step.step import Step
from src.request.request_factory import RequestFactory


class GetRequestStep(Step):

    def __init__(self, url: str) -> None:
        self.url = url
        self.request = RequestFactory().create_post_request(url)

    def get_identifier(self) -> str:
        return f"{self.get_name()}{self.url}"

    def execute(self):
        return self.request()
