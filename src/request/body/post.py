from src.request.body.body import Body


class Post(Body):
    def __init__(self, body: dict):
        self.body = body

    def get_body(self) -> dict:
        return self.body