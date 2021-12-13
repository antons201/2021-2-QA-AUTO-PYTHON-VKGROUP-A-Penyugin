from base import Base
from utils import responses, locations
import pytest


class TestMock(Base):

    def test_get_surname(self, user):
        self.create_user(user)

        resp = self.request("GET", locations.GET_SURNAME.format(user.name))

        assert self.check_request_existent_user(resp, user.surname)
        assert self.check_status(resp, "200")

    def test_get_non_existent_surname(self, user):
        resp = self.request("GET", locations.GET_SURNAME.format(user.name))

        assert self.check_request_non_existent_user(resp, responses.USER_NOT_FOUND.format(user.name))
        assert self.check_status(resp, "404")

    def test_update_surname(self, user):
        self.create_user(user)

        resp = self.request("PUT", locations.UPDATE_SURNAME.format(user.name, user.surname+'Upd'))

        assert self.check_request_existent_user(resp, user.surname + 'Upd')
        assert self.check_status(resp, "200")

    def test_update_non_existent_surname(self, user):
        resp = self.request("PUT", locations.UPDATE_SURNAME.format(user.name, user.surname+'Upd'))

        assert self.check_request_non_existent_user(resp, responses.USER_NOT_FOUND.format(user.name))
        assert self.check_status(resp, "404")

    def test_delete_user(self, user):
        self.create_user(user)

        resp = self.request("DELETE", locations.DELETE_NAME.format(user.name))

        assert self.check_request_non_existent_user(resp, responses.USER_DELETED.format(user.name, user.surname))
        assert self.check_status(resp, "200")

    def test_delete_non_existent_user(self, user):
        resp = self.request("DELETE", locations.DELETE_NAME.format(user.name))

        assert self.check_request_non_existent_user(resp, responses.USER_NOT_FOUND.format(user.name))
        assert self.check_status(resp, "404")




