from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class LoginPageLocators(BasePageLocators):
    LOGIN_LOCATOR = (By.CSS_SELECTOR, "div[class^='responseHead-module-button']")
    EMAIL_LOCATOR = (By.NAME, "email")
    PASSWORD_LOCATOR = (By.NAME, "password")
    AUTH_LOCATOR = (By.CSS_SELECTOR, "div[class^='authForm-module-button']")
    INCORRECT_EMAIL_LOCATOR = (By.XPATH, "//div[contains(@class, 'authForm-module-notify')]/div[contains(@class, 'undefined')]")