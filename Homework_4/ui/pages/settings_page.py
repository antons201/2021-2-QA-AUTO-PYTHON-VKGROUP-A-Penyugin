from ui.pages.base_page import BasePage
from ui.locators.settings_page_locators import SettingsPageLocators
from appium.webdriver.common.mobileby import MobileBy


class SettingsPage(BasePage):
    locators = SettingsPageLocators()

    def swipe_settings(self):
        self.find(SettingsPageLocators.ACCOUNTS_LOCATOR)
        self.swipe_up()