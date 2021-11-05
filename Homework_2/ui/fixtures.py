import allure
import pytest
import os

from _pytest.fixtures import FixtureRequest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from utils import user_data


from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
from ui.pages.invalid_login_page import InvalidLoginPage
from ui.pages.auth_page import AuthPage
from ui.pages.dashboard_page import DashboardPage
from ui.pages.segments_page import SegmentsPage


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver=driver)

@pytest.fixture
def invalid_login_page(driver):
    return InvalidLoginPage(driver=driver)

@pytest.fixture
def auth_page(driver):
    return AuthPage(driver=driver)

@pytest.fixture
def dashboard_page(login):
    return login.go_to_dashboard()

@pytest.fixture
def segments_page(login):
    return login.go_to_segments()

def get_driver():
    manager = ChromeDriverManager(version='latest')
    browser = webdriver.Chrome(executable_path=manager.install())

    browser.maximize_window()
    browser.get("https://target.my.com/")

    return browser

@pytest.fixture(scope='function')
def driver():

    with allure.step("Init driver"):
        browser = get_driver()

    yield browser

    browser.quit()

@pytest.fixture(scope='session')
def cookies():
    driver = get_driver()
    driver.get("https://target.my.com/")
    login_page = LoginPage(driver)
    login_page.attempt_to_login(user_data.email, user_data.password)

    cookies = driver.get_cookies()
    driver.quit()
    return cookies

@pytest.fixture(scope='function')
def file_path(repo_root):
    return os.path.join(repo_root, "files", "test_company_image.jpg")

@pytest.fixture(scope='function')
def login(driver, request: FixtureRequest, auth_page):
    with allure.step("Get cookies"):
        cookies = request.getfixturevalue('cookies')
    with allure.step("Add cookies"):
        for cookie in cookies:
            driver.add_cookie(cookie)

    with allure.step("Refresh page"):
        driver.refresh()

    yield auth_page
