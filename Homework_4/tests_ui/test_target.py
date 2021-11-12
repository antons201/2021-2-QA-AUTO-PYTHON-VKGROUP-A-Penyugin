import pytest
from appium.webdriver.common.mobileby import MobileBy

from base import BaseCase
from utils import strings


class TestMarussia(BaseCase):

    @pytest.mark.Android
    def test_start_page(self, main_page):
        main_page.enter_text(strings.RUSSIA_REQUEST)
        main_page.check_card(strings.RUSSIA_REQUEST, strings.RUSSIA_TITLE, strings.RUSSIA_DESCRIPTION_START)
        main_page.click_suggest()

    @pytest.mark.Android
    def test_calculator(self, main_page):
        main_page.enter_text(strings.EXAMPLE)
        main_page.find((MobileBy.XPATH, main_page.locators.RESPONSE_LOCATOR.format(strings.SUM)))

    @pytest.mark.Android
    def test_news_change_radio(self, main_page, settings_page, news_sources_page):
        main_page.click(main_page.locators.MENU_LOCATOR)
        settings_page.swipe_settings()
        settings_page.click(settings_page.locators.NEWS_SOURCE_LOCATOR)
        news_sources_page.select_news_source(strings.NEWS_SOURCE)
        settings_page.click(settings_page.locators.CLOSE_BUTTON_LOCATOR)
        main_page.check_source_news(strings.NEWS_SOURCE)

    @pytest.mark.Android
    def test_check_about(self, main_page, settings_page, about_page, file_path):
        main_page.click(main_page.locators.MENU_LOCATOR)
        settings_page.swipe_settings()
        settings_page.click(settings_page.locators.ABOUT_LOCATOR)
        version = about_page.find(about_page.locators.VERSION_LOCATOR).text
        file_version = about_page.get_version_from_file(file_path)
        assert version == strings.VERSION.format(file_version)
        copyright_text = about_page.find(about_page.locators.COPYRIGHT_LOCATOR).text
        assert copyright_text == strings.COPYRIGHT
