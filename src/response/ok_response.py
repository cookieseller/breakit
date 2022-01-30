class OkResponse:
    def is_valid_response(self, response):
        return response.status_code == 200

