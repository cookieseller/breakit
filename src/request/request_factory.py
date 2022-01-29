import requests


class RequestFactory:
    def create_get_request(self, url, headers=None, params=None):
        def wrapper():
            return requests.get(url=url, params=headers)
        return wrapper

    def create_post_request(self, url, headers=None, params=None):
        def wrapper():
            return requests.post(url=url, params=headers)
        return wrapper


    def create_delete_request(self, url, headers=None, params=None):
        def wrapper():
            return requests.delete(url=url, params=headers)
        return wrapper

