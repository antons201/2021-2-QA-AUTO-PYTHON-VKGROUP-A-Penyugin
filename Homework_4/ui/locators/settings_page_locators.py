from ui.locators.base_page_locators import BasePageLocators
from appium.webdriver.common.mobileby import MobileBy


class SettingsPageLocators(BasePageLocators):
    NEWS_SOURCE_LOCATOR = (MobileBy.ID, "ru.mail.search.electroscope:id/user_settings_field_news_sources")
    ACCOUNTS_LOCATOR = (MobileBy.ID, "ru.mail.search.electroscope:id/user_settings_accessible_accounts_vk_connect")
    CLOSE_BUTTON_LOCATOR = (MobileBy.XPATH, "//android.widget.LinearLayout/android.widget.ImageButton")
    ABOUT_LOCATOR = (MobileBy.ID, "ru.mail.search.electroscope:id/user_settings_about")
