from ui.locators import base_page_locators
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

CLICK_RETRY = 5


class BasePage(object):

    locators = base_page_locators.BasePageLocators

    def __init__(self, driver):
        self.driver = driver

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 10
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator, timeout=None):
        for i in range(CLICK_RETRY):
            try:
                self.find(locator, timeout=timeout)
                self.wait(timeout).until(EC.element_to_be_clickable(locator)).click()
                return
            except (StaleElementReferenceException, TimeoutException):
                if i == CLICK_RETRY-1:
                    raise

    def send_data(self, locator, data, clear = True):
            elem = self.find(locator)
            if clear:
                elem.clear()
            elem.send_keys(data)

    def swipe_element_to_left(self, locator, swipetime=2000):
        web_element = self.find(locator)
        left_x = web_element.location['x']
        right_x = left_x + web_element.rect['width']-1
        upper_y = web_element.location['y']
        lower_y = upper_y + web_element.rect['height']-1
        middle_y = (upper_y + lower_y) / 2
        action = TouchAction(self.driver)
        action. \
            press(x=2*right_x/3, y=middle_y). \
            wait(ms=swipetime). \
            move_to(x=left_x, y=middle_y). \
            release(). \
            perform()

    def swipe_up(self, swipetime=200):
        action = TouchAction(self.driver)
        dimension = self.driver.get_window_size()
        x = int(dimension['width'] / 2)
        start_y = int(dimension['height'] * 0.99)
        end_y = int(dimension['height'] * 0.01)
        action. \
            press(x=x, y=start_y). \
            wait(ms=swipetime). \
            move_to(x=x, y=end_y). \
            release(). \
            perform()
