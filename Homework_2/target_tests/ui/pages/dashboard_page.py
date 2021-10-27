import allure

from ui.pages.base_page import BasePage
from ui.locators.dashboard_page_locators import DashboardPageLocators
from utils import company_data, constants
from random import randint


class DashboardPage(BasePage):
    locators = DashboardPageLocators()

    @allure.step("Attempt to create a company")
    def create_company(self, file_path):
        unic_value = randint(constants.MIN_RANDOM, constants.MAX_RANDOM) * randint(constants.MIN_RANDOM,constants.MAX_RANDOM)

        try:
            self.click(DashboardPageLocators.CREATE_COMPANY_LOCATOR)
        except:
            self.click(DashboardPageLocators.NEW_COMPANY_LOCATOR)
        self.wait_locator(DashboardPageLocators.SPINNER_LOCATOR)
        self.click(DashboardPageLocators.TRAFFIC_LOCATOR)
        self.send_data(DashboardPageLocators.LINK_LOCATOR, company_data.link)
        self.send_data(DashboardPageLocators.COMPANY_NAME_LOCATOR, unic_value, False)
        company_name = self.find(DashboardPageLocators.COMPANY_NAME_LOCATOR).get_attribute("value")
        self.click(DashboardPageLocators.FORMAT_LOCATOR)
        input_field = self.find(DashboardPageLocators.UPLOAD_LOCATOR)
        input_field.send_keys(file_path)
        self.wait_locator(DashboardPageLocators.UPLOAD_PROCESS_LOCATOR)
        self.click(DashboardPageLocators.SUBMIT_CREATE_LOCATOR)

        return company_name
