from ui.pages.base_page import BasePage
from ui.locators.main_page_locators import MainPageLocators
from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.mobileby import MobileBy


class MainPage(BasePage):
    locators = MainPageLocators()

    def allow_permissions(self):
        self.click(MainPageLocators.AGREE_FOREGROUND_LOCATOR)
        self.click(MainPageLocators.AGREE_LOCATOR)

    def enter_text(self, text):
        self.click(MainPageLocators.KEYBOARD_LOCATOR)
        self.send_text(text)

    def send_text(self, text):
        self.send_data(MainPageLocators.SEARCH_INPUT_LOCATOR, text)
        self.driver.hide_keyboard()
        self.click(MainPageLocators.SEARCH_BUTTON_LOCATOR)

    def check_card(self, text_request, text_title, text_description):
        try:
            title = self.find(MainPageLocators.CARD_TITLE_LOCATOR, 5)
        except TimeoutException:
            self.send_text(text_request)
            title = self.find(MainPageLocators.CARD_TITLE_LOCATOR)
        assert title.text == text_title
        description = self.find(MainPageLocators.CARD_DESCRIPTION_LOCATOR)
        assert description.text[0:7] == text_description

    def click_suggest(self):
        self.swipe_element_to_left(MainPageLocators.SUGGEST_LIST_LOCATOR)
        self.click((MobileBy.XPATH, MainPageLocators.SUGGEST_LOCATOR.format("население россии")))
        self.find((MobileBy.XPATH, MainPageLocators.SUGGEST_TITLE_LOCATOR.format("146 млн.")))

    def check_source_news(self, news_source):
        self.enter_text("News")
        self.find((MobileBy.XPATH, MainPageLocators.RESPONSE_LOCATOR.format(news_source)))