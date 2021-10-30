import allure
import pytest

from base import BaseCase
from ui.locators import login_page_locators, invalid_login_locators, dashboard_page_locators, segments_page_locators
from selenium.common.exceptions import TimeoutException
from utils import user_data


class TestTarget(BaseCase):

    @allure.feature('UI tests')
    @allure.description("Checking an attempt to log in with an invalid email and password. "
                        "The login attempt must have failed")
    @pytest.mark.UI
    def test_invalid_login(self):
        self.login_page.attempt_to_login(user_data.nonExistentEmail, user_data.nonExistentPassword)
        self.invalid_login_page.invalid_login_check(invalid_login_locators.InvalidLoginLocators.INVALID_LOGIN_LOCATOR)

    @allure.feature('UI tests')
    @allure.description("Checking an attempt to log in with an incorrect email and password. "
                        "The login attempt must have failed")
    @pytest.mark.UI
    def test_incorrect_login(self):
        self.login_page.attempt_to_login(user_data.invalidEmail, user_data.nonExistentPassword)
        self.login_page.incorrect_login_check(login_page_locators.LoginPageLocators.INCORRECT_EMAIL_LOCATOR)

    @allure.feature('UI tests')
    @allure.description("Checking the creation of a company with valid data")
    @pytest.mark.UI
    @pytest.mark.usefixtures('login')
    @pytest.mark.usefixtures('file_path')
    def test_create_company(self, auth_page, file_path):
        dashboard_page = auth_page.go_to_dashboard()

        dashboard_page.create_company(file_path)

    @allure.feature('UI tests')
    @allure.description("Checking the creation of a segment with valid data")
    @pytest.mark.UI
    @pytest.mark.usefixtures('login')
    def test_create_segment(self, auth_page):
        segments_page = auth_page.go_to_segments()

        segments_page.create_segment()

    @allure.feature('UI tests')
    @allure.description("Checking the deletion of a newly created segment")
    @pytest.mark.UI
    @pytest.mark.usefixtures('login')
    def test_delete_segment(self, auth_page):
        segments_page = auth_page.go_to_segments()

        segments_page.delete_segment(segments_page.create_segment())
