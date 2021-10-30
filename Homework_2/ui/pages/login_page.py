import allure

from ui.pages.base_page import BasePage
from ui.locators.login_page_locators import LoginPageLocators
from ui.locators.invalid_login_locators import InvalidLoginLocators


class LoginPage(BasePage):
    locators = LoginPageLocators()

    @allure.step("Authorization attempt")
    def attempt_to_login(self, email, password):
        self.wait_locator(LoginPageLocators.SPINNER_LOCATOR)
        self.logger.info(f"Authorization attempt with login:{email} and password:"
                         f"{password}")
        self.click(LoginPageLocators.LOGIN_LOCATOR)
        self.send_data(LoginPageLocators.EMAIL_LOCATOR, email)
        self.send_data(LoginPageLocators.PASSWORD_LOCATOR, password)
        self.click(LoginPageLocators.AUTH_LOCATOR)

    def incorrect_login_check(self, failed_login_locator):
        with allure.step("Checking the appearance of a message about an incorrect login"):
            self.find(failed_login_locator).is_displayed()
        self.logger.info(
            f"Login attempt failed. Found: {failed_login_locator}")