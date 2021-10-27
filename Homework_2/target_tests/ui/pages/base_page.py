import allure
from ui.locators import base_page_locators
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException, \
    TimeoutException, ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

CLICK_RETRY = 5


class BasePage(object):

    locators = base_page_locators.BasePageLocators

    def __init__(self, driver):
        self.driver = driver

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 10
        return WebDriverWait(self.driver, timeout=timeout)

    @allure.step("Find {locator}")
    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    @allure.step("Waiting for the load")
    def wait_locator(self, locator):
        try:
            self.wait(3).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return
        self.wait(10).until(EC.invisibility_of_element_located(locator))

    @allure.step("Click to {locator}")
    def click(self, locator, timeout=None):
        for i in range(CLICK_RETRY):
            try:
                self.find(locator, timeout=timeout)
                self.wait(timeout).until(EC.element_to_be_clickable(locator)).click()
                return
            except (StaleElementReferenceException, ElementClickInterceptedException):
                if i == CLICK_RETRY-1:
                    raise

    @allure.step("Send data to {locator}")
    def send_data(self, locator, data, clear = True):
        for i in range(CLICK_RETRY):
            try:
                elem = self.find(locator)
                if clear:
                    elem.clear()
                elem.send_keys(data)
                return
            except ElementNotInteractableException:
                if i == CLICK_RETRY-1:
                    raise
            time.sleep(0.5)


