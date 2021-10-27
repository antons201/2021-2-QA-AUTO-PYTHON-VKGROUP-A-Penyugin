from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class AuthPageLocators(BasePageLocators):
    DASHBOARD_LOCATOR = (By.CSS_SELECTOR, "a[href='/dashboard']")
    SEGMENTS_LOCATOR = (By.CSS_SELECTOR, "a[href='/segments']")