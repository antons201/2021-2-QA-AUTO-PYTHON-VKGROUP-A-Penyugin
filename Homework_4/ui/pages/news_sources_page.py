from ui.pages.base_page import BasePage
from ui.locators.news_sources_page_locators import NewsSourcesPageLocators
from appium.webdriver.common.mobileby import MobileBy


class NewsSourcesPage(BasePage):
    locators = NewsSourcesPageLocators()

    def select_news_source(self, news_source):
        self.click((MobileBy.XPATH, NewsSourcesPageLocators.NEWS_TYPE_LOCATOR.format(2, news_source)))
        self.find((MobileBy.XPATH, NewsSourcesPageLocators.NEWS_SELECTED_LOCATOR.format(2)))
        self.click(NewsSourcesPageLocators.BACK_BUTTON_LOCATOR)