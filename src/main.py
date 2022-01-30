from request.request_factory import RequestFactory
from src.response.ok_response import OkResponse


def print_hello_there():
    print(f'Hello there, thank you for running breakit')


if __name__ == '__main__':
    factory = RequestFactory()
    ok_response = OkResponse()

    get_request = factory.create_get_request('https://google.com')
    ok_response.is_valid_response(get_request())
    print(ok_response.is_valid_response(get_request()))

