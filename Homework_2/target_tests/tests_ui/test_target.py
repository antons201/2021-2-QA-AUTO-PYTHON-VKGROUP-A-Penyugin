import allure
import pytest

from base import BaseCase
from ui.locators import login_page_locators, invalid_login_locators, dashboard_page_locators, segments_page_locators
from selenium.common.exceptions import TimeoutException
from utils import user_data


class TestTarget(BaseCase):

    @allure.feature('UI tests')
    @allure.description("Checking an attempt to log in with an invalid email and password. "
                        "The login attempt must have failed")
    @pytest.mark.UI
    def test_invalid_login(self):
        self.login_page.wait_locator(login_page_locators.LoginPageLocators.SPINNER_LOCATOR)
        self.logger.info(f"Authorization attempt with login:{user_data.nonExistentEmail} and password:"
                         f"{user_data.nonExistentPassword}")
        self.login_page.attempt_to_login(user_data.nonExistentEmail, user_data.nonExistentPassword)
        with allure.step("Checking the appearance of a message about an invalid login"):
            self.invalid_login_page.find(
                invalid_login_locators.InvalidLoginLocators.INVALID_LOGIN_LOCATOR).is_displayed()
        self.logger.info(
            f"Login attempt failed. Found: {invalid_login_locators.InvalidLoginLocators.INVALID_LOGIN_LOCATOR}")

    @allure.feature('UI tests')
    @allure.description("Checking an attempt to log in with an incorrect email and password. "
                        "The login attempt must have failed")
    @pytest.mark.UI
    def test_incorrect_login(self):
        self.login_page.wait_locator(login_page_locators.LoginPageLocators.SPINNER_LOCATOR)
        self.logger.info(f"Authorization attempt with login:{user_data.invalidEmail} and password:"
                         f"{user_data.nonExistentPassword}")
        self.login_page.attempt_to_login(user_data.invalidEmail, user_data.nonExistentPassword)
        with allure.step("Checking the appearance of a message about an incorrect login"):
            self.login_page.find(login_page_locators.LoginPageLocators.INCORRECT_EMAIL_LOCATOR).is_displayed()
        self.logger.info(
            f"Login attempt failed. Found: {login_page_locators.LoginPageLocators.INCORRECT_EMAIL_LOCATOR}")

    @allure.feature('UI tests')
    @allure.description("Checking the creation of a company with valid data")
    @pytest.mark.UI
    @pytest.mark.usefixtures('login')
    @pytest.mark.usefixtures('file_path')
    def test_create_company(self, auth_page, file_path):
        dashboard_page = auth_page.go_to_dashboard()
        dashboard_page.wait_locator(dashboard_page_locators.DashboardPageLocators.SPINNER_LOCATOR)

        company_name = dashboard_page.create_company(file_path)

        with allure.step("Checking that the company has been created"):
            dashboard_page.find((dashboard_page_locators.DashboardPageLocators.COMPANY_LOCATOR[0],
                                 dashboard_page_locators.DashboardPageLocators.COMPANY_LOCATOR[1].format(company_name)))

        self.logger.info(f"A company with the name {company_name} has been created")

    @allure.feature('UI tests')
    @allure.description("Checking the creation of a segment with valid data")
    @pytest.mark.UI
    @pytest.mark.usefixtures('login')
    def test_create_segment(self, auth_page):
        segments_page = auth_page.go_to_segments()
        segments_page.wait_locator(segments_page_locators.SegmentsPageLocators.SPINNER_LOCATOR)

        segment_name = segments_page.create_segment()

        with allure.step("Checking that the segment has been created"):
            segments_page.find((segments_page_locators.SegmentsPageLocators.SEGMENT_NAME_LOCATOR[0],
                                segments_page_locators.SegmentsPageLocators.SEGMENT_NAME_LOCATOR[1].format(
                                    segment_name)))

        self.logger.info(f"A segment with the name {segment_name} has been created")

    @allure.feature('UI tests')
    @allure.description("Checking the deletion of a newly created segment")
    @pytest.mark.UI
    @pytest.mark.usefixtures('login')
    def test_delete_segment(self, auth_page):
        segments_page = auth_page.go_to_segments()
        segments_page.wait_locator(segments_page_locators.SegmentsPageLocators.SPINNER_LOCATOR)

        segment_name = segments_page.create_segment()

        with allure.step("Checking that the segment has been created"):
            segments_page.find((segments_page_locators.SegmentsPageLocators.SEGMENT_NAME_LOCATOR[0],
                                segments_page_locators.SegmentsPageLocators.SEGMENT_NAME_LOCATOR[1].format(
                                    segment_name)))

        self.logger.info(f"A segment with the name {segment_name} has been created")

        segments_page.delete_segment(segment_name)

        with allure.step("Checking that the segment has been deleted"):
            try:
                segments_page.find((segments_page_locators.SegmentsPageLocators.SEGMENT_NAME_LOCATOR[0],
                                    segments_page_locators.SegmentsPageLocators.SEGMENT_NAME_LOCATOR[1].format(
                                        segment_name)), 3)
                self.logger.info(f"A segment with the name {segment_name} has not been deleted")
                pytest.fail('DELETE EXCEPTION')
            except TimeoutException:
                self.logger.info(f"A segment with the name {segment_name} has been deleted")
                pass
