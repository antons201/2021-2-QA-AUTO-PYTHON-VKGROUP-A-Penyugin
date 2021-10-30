import allure
import pytest

from ui.pages.base_page import BasePage
from ui.locators.segments_page_locators import SegmentsPageLocators
from selenium.common.exceptions import TimeoutException
from utils import constants
from random import randint


class SegmentsPage(BasePage):
    locators = SegmentsPageLocators()

    @allure.step("Attempt to create a segment")
    def create_segment(self):
        unic_value = randint(constants.MIN_RANDOM, constants.MAX_RANDOM) * randint(constants.MIN_RANDOM,
                                                                                   constants.MAX_RANDOM)

        self.wait_locator(SegmentsPageLocators.SPINNER_LOCATOR)
        try:
            self.click(SegmentsPageLocators.CREATE_SEGMENT_LOCATOR, 5)
        except:
            self.click(SegmentsPageLocators.NEW_SEGMENT_LOCATOR, 5)

        self.click(SegmentsPageLocators.SELECT_SEGMENT_LOCATOR)
        self.click(SegmentsPageLocators.SEGMENT_SOURCE_CHECKBOX_LOCATOR)
        self.click(SegmentsPageLocators.SUBMIT_ADD_LOCATOR)
        self.send_data(SegmentsPageLocators.SEGMENT_NAME_LOCATOR, unic_value, False)
        segment_name = self.find(
            SegmentsPageLocators.SEGMENT_NAME_LOCATOR).get_attribute("value")

        self.click(SegmentsPageLocators.CREATE_SEGMENT_LOCATOR)

        with allure.step("Checking that the segment has been created"):
            self.find((SegmentsPageLocators.SEGMENT_NAME_LOCATOR[0],
                       SegmentsPageLocators.SEGMENT_NAME_LOCATOR[1].format(segment_name)))

        self.logger.info(f"A segment with the name {segment_name} has been created")

        return segment_name

    @allure.step("Attempt to delete a segment")
    def delete_segment(self, segment_name):
        self.click((SegmentsPageLocators.DELETE_SEGMENT_LOCATOR[0], SegmentsPageLocators.DELETE_SEGMENT_LOCATOR[1].
                    format(segment_name)))
        self.click(SegmentsPageLocators.SUBMIT_DELETE_LOCATOR)

        with allure.step("Checking that the segment has been deleted"):
            try:
                self.find((SegmentsPageLocators.SEGMENT_NAME_LOCATOR[0],
                           SegmentsPageLocators.SEGMENT_NAME_LOCATOR[1].format(segment_name)), 3)
                self.logger.info(f"A segment with the name {segment_name} has not been deleted")
                pytest.fail('DELETE EXCEPTION')
            except TimeoutException:
                self.logger.info(f"A segment with the name {segment_name} has been deleted")
                pass