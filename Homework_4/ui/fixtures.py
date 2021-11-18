import pytest
import os

from appium import webdriver
from ui.capability import capability_select


from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.settings_page import SettingsPage
from ui.pages.news_sources_page import NewsSourcesPage
from ui.pages.about_page import AboutPage


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)


@pytest.fixture
def settings_page(driver):
    return SettingsPage(driver=driver)


@pytest.fixture
def news_sources_page(driver):
    return NewsSourcesPage(driver=driver)


@pytest.fixture
def about_page(driver):
    return AboutPage(driver=driver)


def get_driver(file_path):
    desired_caps = capability_select(file_path)
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)
    return driver


@pytest.fixture(scope='function')
def driver(file_path):

    browser = get_driver(file_path)

    yield browser

    browser.quit()


@pytest.fixture(scope='function')
def file_path(repo_root):
    yield os.path.join(repo_root, "files", "Marussia_v1.50.2.apk")
