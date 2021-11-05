import allure
import pytest

from base import BaseCase
from utils import user_data
from selenium.common.exceptions import TimeoutException


class TestTarget(BaseCase):

    @allure.feature('UI tests')
    @allure.description("Checking an attempt to log in with an invalid email and password. "
                        "The login attempt must have failed")
    @pytest.mark.UI
    def test_invalid_login(self, login_page, invalid_login_page):
        login_page.attempt_to_login(user_data.nonExistentEmail, user_data.nonExistentPassword)

        with allure.step("Checking the appearance of a message about an incorrect login"):
            assert invalid_login_page.find(invalid_login_page.locators.INVALID_LOGIN_LOCATOR).is_displayed()
            self.logger.info(f"Login attempt failed. Found: {invalid_login_page.locators.INVALID_LOGIN_LOCATOR}")


    @allure.feature('UI tests')
    @allure.description("Checking an attempt to log in with an incorrect email and password. "
                        "The login attempt must have failed")
    @pytest.mark.UI
    def test_incorrect_login(self, login_page):
        login_page.attempt_to_login(user_data.invalidEmail, user_data.nonExistentPassword)

        with allure.step("Checking the appearance of a message about an incorrect login"):
            try:
                login_page.find(login_page.locators.INCORRECT_EMAIL_LOCATOR)
                self.logger.info(f"Login attempt failed. Found: {login_page.locators.INCORRECT_EMAIL_LOCATOR}")
            except TimeoutException:
                self.logger.info(f"Not found: {login_page.locators.INCORRECT_EMAIL_LOCATOR}")
                pytest.fail('INCORRECT LOGIN EXCEPTION')

    @allure.feature('UI tests')
    @allure.description("Checking the creation of a company with valid data")
    @pytest.mark.UI
    def test_create_company(self, file_path, dashboard_page):
        company_name = dashboard_page.create_company(file_path)

        with allure.step("Checking that the company has been created"):
            try:
                dashboard_page.find((dashboard_page.locators.COMPANY_LOCATOR[0],
                                     dashboard_page.locators.COMPANY_LOCATOR[1].format(company_name)))

                self.logger.info(f"A company with the name {company_name} has been created")
            except TimeoutException:
                self.logger.info(f"A company with the name {company_name} has not been created")
                pytest.fail('CREATE COMPANY EXCEPTION')

    @allure.feature('UI tests')
    @allure.description("Checking the creation of a segment with valid data")
    @pytest.mark.UI
    def test_create_segment(self, segments_page):
        segment_name = segments_page.create_segment()

        with allure.step("Checking that the segment has been created"):
            try:
                segments_page.find((segments_page.locators.SEGMENT_NAME_LOCATOR[0],
                                    segments_page.locators.SEGMENT_NAME_LOCATOR[1].format(segment_name)))

                self.logger.info(f"A segment with the name {segment_name} has been created")
            except TimeoutException:
                self.logger.info(f"A segment with the name {segment_name} has not been created")
                pytest.fail('CREATE SEGMENT EXCEPTION')

    @allure.feature('UI tests')
    @allure.description("Checking the deletion of a newly created segment")
    @pytest.mark.UI
    def test_delete_segment(self, segments_page):
        segment_name = segments_page.create_segment()
        segments_page.delete_segment(segment_name)

        with allure.step("Checking that the segment has been deleted"):
            try:
                segments_page.find((segments_page.locators.SEGMENT_NAME_LOCATOR[0],
                                    segments_page.locators.SEGMENT_NAME_LOCATOR[1].format(segment_name)), 3)
                self.logger.info(f"A segment with the name {segment_name} has not been deleted")
                pytest.fail('DELETE SEGMENT EXCEPTION')

            except TimeoutException:
                self.logger.info(f"A segment with the name {segment_name} has been deleted")
