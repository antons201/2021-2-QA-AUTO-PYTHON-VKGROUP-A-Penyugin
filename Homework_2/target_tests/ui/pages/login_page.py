import allure
import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.base_page import BasePage
from ui.locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    locators = LoginPageLocators()

    @allure.step("Authorization attempt")
    def attempt_to_login(self, email, password):
        self.click(LoginPageLocators.LOGIN_LOCATOR)
        self.send_data(LoginPageLocators.EMAIL_LOCATOR, email)
        self.send_data(LoginPageLocators.PASSWORD_LOCATOR, password)
        self.click(LoginPageLocators.AUTH_LOCATOR)