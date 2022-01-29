from request.request_factory import RequestFactory

def print_hello_there():
    print(f'Hello there, thank you for running breakit')


if __name__ == '__main__':
    factory = RequestFactory()

    get_request = factory.create_get_request('https://google.com')
    print(get_request())

