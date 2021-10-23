from base import BaseCase
from ui.locators import basic_locators
from selenium.common.exceptions import TimeoutException
from utils import user_data
import pytest


class TestTarget(BaseCase):

    @pytest.mark.UI
    @pytest.mark.usefixtures('login')
    def test_login(self):
        pass

    @pytest.mark.UI
    @pytest.mark.usefixtures('login')
    def test_logout(self):
        self.click(basic_locators.USER_ICON_LOCATOR)
        self.click(basic_locators.LOGOUT_LOCATOR)
        try:
            self.find(basic_locators.LOGIN_LOCATOR)
        except TimeoutException:
            pytest.fail('LOGOUT EXCEPTION')

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
    @pytest.mark.usefixtures('login')
    def test_edit_contact_info(self):
        self.click(basic_locators.PROFILE_LOCATOR)
        self.wait_spinner()
        self.change_info(user_data.fio_before, user_data.phone_before)
        self.check_change_info(user_data.fio_before, user_data.phone_before)
        self.change_info(user_data.fio_after, user_data.phone_after)
        self.check_change_info(user_data.fio_after, user_data.phone_after)

    @pytest.mark.UI
    @pytest.mark.usefixtures('login')
    @pytest.mark.parametrize("locator, title", [(basic_locators.SEGMENTS_LOCATOR, "Список сегментов"),
                                                (basic_locators.BILLING_LOCATOR, "Лицевой счет")])
    def test_go_to_page(self, locator, title):
        self.click(locator)
        self.wait_spinner()
        assert self.driver.title == title
