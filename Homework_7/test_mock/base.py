import json

import pytest
from client.client import Client
from utils.builder import Builder
from mock.mock import USERS


class Base:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, client_logger):
        self.client = Client()
        self.builder = Builder()
        self.client.create_client(client_logger)

    def request(self, request_type, params):
        self.client.send_request(request_type, params)
        return self.client.get_response()

    @pytest.fixture()
    def user(self):
        data = self.builder.user()
        yield data

    def create_user(self, user):
        USERS[user.name] = user.surname

    def check_request_existent_user(self, response, expected_response):
        return json.loads(response[-1])['surname'] == expected_response

    def check_request_non_existent_user(self, response, expected_response):
        return json.loads(response[-1]) == expected_response

    def check_status(self, response, expected_status):
        return response[0].split(" ")[1] == expected_status
