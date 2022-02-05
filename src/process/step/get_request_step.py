from src.process.step.step import Step
from src.request.request_factory import RequestFactory


class GetRequestStep(Step):

    def __init__(self, url: str) -> None:
        self.request = RequestFactory().create_get_request(url)

    def execute(self):
        return self.request()
