import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():

    browser = webdriver.Chrome(executable_path='chromedriver.exe')

    browser.maximize_window()
    browser.get("https://target.my.com/")

    yield browser

    browser.close()