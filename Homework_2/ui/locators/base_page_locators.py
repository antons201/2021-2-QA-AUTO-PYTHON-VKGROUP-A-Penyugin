from selenium.webdriver.common.by import By


class BasePageLocators:
    SPINNER_LOCATOR = (By.CSS_SELECTOR, "div[class^='spinner']")