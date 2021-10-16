import pytest
from ui.locators import basic_locators
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException, \
    TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

CLICK_RETRY = 5


class BaseCase:

    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.driver = driver

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def wait_spinner(self, timeout=None):
        try:
            self.wait(2).until(EC.visibility_of_element_located(basic_locators.SPINNER_LOCATOR))
        except TimeoutException:
            return
        self.wait(10).until(EC.invisibility_of_element_located(basic_locators.SPINNER_LOCATOR))

    def click(self, locator, timeout=None):
        for i in range(CLICK_RETRY):
            try:
                elem = self.find(locator, timeout=timeout)
                elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                elem.click()
                return
            except (StaleElementReferenceException, ElementClickInterceptedException):
                if i == CLICK_RETRY-1:
                    raise

    def send_data(self, locator, data):
        elem = self.find(locator)
        elem.clear()
        elem.send_keys(data)