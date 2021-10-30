import allure

from ui.pages.base_page import BasePage
from ui.locators.invalid_login_locators import InvalidLoginLocators


class InvalidLoginPage(BasePage):
    locators = InvalidLoginLocators()

    def invalid_login_check(self, failed_login_locator):
        with allure.step("Checking the appearance of a message about an invalid login"):
            self.find(failed_login_locator).is_displayed()
        self.logger.info(f"Login attempt failed. Found: {failed_login_locator}")

