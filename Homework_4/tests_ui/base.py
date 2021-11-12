import pytest

from appium.webdriver.webdriver import WebDriver


class BaseCase:

    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, main_page):
        self.driver: WebDriver = driver
        main_page.allow_permissions()
