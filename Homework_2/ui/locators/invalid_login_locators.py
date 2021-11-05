from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class InvalidLoginLocators(BasePageLocators):
    INVALID_LOGIN_LOCATOR = (By.XPATH, "//div[contains(@class, 'formMsg_text')]")