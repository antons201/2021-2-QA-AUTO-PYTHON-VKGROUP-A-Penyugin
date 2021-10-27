import os
import allure
import pytest

from _pytest.fixtures import FixtureRequest
from selenium.webdriver.remote.webdriver import WebDriver

from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
from ui.pages.invalid_login_page import InvalidLoginPage
from ui.pages.auth_page import AuthPage
from ui.pages.dashboard_page import DashboardPage
from ui.pages.segments_page import SegmentsPage


class BaseCase:

    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def ui_report(self, driver, request, temp_dir):
        failed_tests_count = request.session.testsfailed
        yield
        if request.session.testsfailed > failed_tests_count:
            screenshot = os.path.join(temp_dir, 'failure.png')
            driver.get_screenshot_as_file(screenshot)
            allure.attach.file(screenshot, 'failure.png', attachment_type=allure.attachment_type.PNG)

            browser_log = os.path.join(temp_dir, 'browser.log')
            with open(browser_log, 'w') as f:
                for i in driver.get_log('browser'):
                    f.write(f"{i['level']} - {i['source']}\n{i['message']}\n")

            with open(browser_log, 'r') as f:
                allure.attach(f.read(), 'browser.log', attachment_type=allure.attachment_type.TEXT)

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, logger, request: FixtureRequest):
        self.driver: WebDriver = driver
        self.config = config
        self.logger = logger

        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.login_page: LoginPage = request.getfixturevalue('login_page')
        self.invalid_login_page: InvalidLoginPage = request.getfixturevalue('invalid_login_page')
        self.auth_page: AuthPage = request.getfixturevalue("auth_page")
        self.dashboard_page: DashboardPage = request.getfixturevalue("dashboard_page")
        self.segments_page: SegmentsPage = request.getfixturevalue("segments_page")

    @pytest.fixture(scope='function')
    def login(self, request: FixtureRequest):
        with allure.step("Get cookies"):
            cookies = request.getfixturevalue('cookies')
        with allure.step("Add cookies"):
            for cookie in cookies:
                self.driver.add_cookie(cookie)

        with allure.step("Refresh page"):
            self.driver.refresh()
        with allure.step("Get Auth page"):
            self.auth_page = AuthPage(self.driver)

        return self.auth_page