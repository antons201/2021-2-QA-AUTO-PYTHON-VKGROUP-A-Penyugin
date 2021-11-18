import pytest
from appium.webdriver.common.mobileby import MobileBy

from base import BaseCase
from utils import strings


class TestMarussia(BaseCase):

    @pytest.mark.Android
    def test_start_page(self, main_page):
        main_page.send_request_with_card_response(strings.RUSSIA_REQUEST, strings.RUSSIA_TITLE,
                                                  strings.RUSSIA_DESCRIPTION_START)
        main_page.click_suggest(strings.SUGGEST_POPULATION, strings.SUGGEST_POPULATION_SIZE)

    @pytest.mark.Android
    def test_calculator(self, main_page):
        main_page.send_request_with_string_response(strings.EXAMPLE, strings.SUM)

    @pytest.mark.Android
    def test_news_change_radio(self, main_page, settings_page, news_sources_page):
        main_page.go_to_menu()
        settings_page.select_setting(settings_page.locators.NEWS_SOURCE_LOCATOR)
        news_sources_page.select_news_source(strings.NEWS_SOURCE_SETTINGS)
        settings_page.back_to_main_page()
        main_page.check_source_news(strings.NEWS_REQUEST, strings.NEWS_SOURCE_PLAYER)

    @pytest.mark.Android
    def test_check_about(self, main_page, settings_page, about_page, file_path):
        main_page.go_to_menu()
        settings_page.select_setting(settings_page.locators.ABOUT_LOCATOR)
        about_page.check_version(file_path, strings.VERSION)
        about_page.check_copyright(strings.COPYRIGHT)

