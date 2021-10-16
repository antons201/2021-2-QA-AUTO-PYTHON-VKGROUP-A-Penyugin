from base import BaseCase
from ui.locators import basic_locators
from selenium.common.exceptions import TimeoutException
from utils import user_data
import pytest


class TestTarget(BaseCase):

    def login(self):
        self.wait_spinner()
        self.click(basic_locators.LOGIN_LOCATOR)
        self.send_data(basic_locators.EMAIL_LOCATOR, user_data.email)
        self.send_data(basic_locators.PASSWORD_LOCATOR, user_data.password)
        self.click(basic_locators.AUTH_LOCATOR)
        self.wait_spinner()
        try:
            self.find(basic_locators.USER_ICON_LOCATOR)
        except TimeoutException:
            assert False

    @pytest.mark.UI
    def test_login(self):
        self.login()

    @pytest.mark.UI
    def test_logout(self):
        self.login()
        self.click(basic_locators.USER_ICON_LOCATOR)
        self.click(basic_locators.LOGOUT_LOCATOR)
        try:
            self.find(basic_locators.LOGIN_LOCATOR)
        except TimeoutException:
            assert False

    def change_info(self, fio, phone):
        self.send_data(basic_locators.FIO_LOCATOR, fio)
        self.send_data(basic_locators.PHONE_LOCATOR, phone)
        self.click(basic_locators.SUBMIT_LOCATOR)

    def check_change_info(self, fio, phone):
        assert "Информация успешно сохранена" in self.driver.page_source
        self.driver.refresh()
        self.wait_spinner()
        assert self.find(basic_locators.FIO_LOCATOR).get_attribute("value") == fio
        assert self.find(basic_locators.PHONE_LOCATOR).get_attribute("value") == phone

    @pytest.mark.UI
    def test_edit_contact_info(self):
        self.login()
        self.click(basic_locators.PROFILE_LOCATOR)
        self.wait_spinner()
        self.change_info(user_data.fio_before, user_data.phone_before)
        self.check_change_info(user_data.fio_before, user_data.phone_before)
        self.change_info(user_data.fio_after, user_data.phone_after)
        self.check_change_info(user_data.fio_after, user_data.phone_after)

    @pytest.mark.UI
    @pytest.mark.parametrize("locator", [basic_locators.SEGMENTS_LOCATOR, basic_locators.BILLING_LOCATOR])
    def test_go_to_page(self, locator):
        self.login()
        self.click(locator)
        self.wait_spinner()
        assert self.find(basic_locators.ACTIVE_LOCATOR).get_attribute("href") == self.find(locator).get_attribute("href")



