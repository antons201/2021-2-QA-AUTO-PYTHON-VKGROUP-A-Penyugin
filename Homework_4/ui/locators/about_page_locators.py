from ui.locators.base_page_locators import BasePageLocators
from appium.webdriver.common.mobileby import MobileBy


class AboutPageLocators(BasePageLocators):
    VERSION_LOCATOR = (MobileBy.ID, "ru.mail.search.electroscope:id/about_version")
    COPYRIGHT_LOCATOR = (MobileBy.ID, "ru.mail.search.electroscope:id/about_copyright")
