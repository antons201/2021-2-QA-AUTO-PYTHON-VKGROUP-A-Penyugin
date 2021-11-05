import allure

from ui.pages.base_page import BasePage
from ui.pages.segments_page import SegmentsPage
from ui.pages.dashboard_page import DashboardPage
from ui.locators.auth_page_locators import AuthPageLocators


class AuthPage(BasePage):
    locators = AuthPageLocators()

    @allure.step("Go to the Dashboard page")
    def go_to_dashboard(self):
        self.click(AuthPageLocators.DASHBOARD_LOCATOR)
        return DashboardPage(self.driver)

    @allure.step("Go to the Segments page")
    def go_to_segments(self):
        self.click(AuthPageLocators.SEGMENTS_LOCATOR)
        return SegmentsPage(self.driver)