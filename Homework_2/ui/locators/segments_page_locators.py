from selenium.webdriver.common.by import By
from ui.locators.auth_page_locators import AuthPageLocators


class SegmentsPageLocators(AuthPageLocators):
    NEW_SEGMENT_LOCATOR = (By.CSS_SELECTOR, "a[href='/segments/segments_list/new/']")
    CREATE_SEGMENT_LOCATOR = (By.XPATH, "//div[contains(@class, 'js-create-button-wrap')]/button")
    SUBMIT_ADD_LOCATOR = (By.XPATH, "//div[contains(@class, 'js-add-button')]/button")
    SELECT_SEGMENT_LOCATOR = (By.XPATH, "//div[contains(@class, 'adding-segments-item')][8]")
    SEGMENT_SOURCE_CHECKBOX_LOCATOR = (By.CSS_SELECTOR, "input[class^='adding-segments-source__checkbox']")
    SUBMIT_CREATE_SEGMENT_LOCATOR = (By.XPATH, "//div[contains(@class, 'js-create-segment-button-wrap')]/button")
    SEGMENT_NAME_LOCATOR = (By.XPATH, "//div[contains(@class, 'input_create-segment-form')]/div[@class='input__wrap']/input")
    SEGMENT_LOCATOR = (By.XPATH, "//a[@title='{}']")
    DELETE_SEGMENT_LOCATOR = (By.XPATH, "//a[@title='{}']/ancestor::div/following-sibling::div[4]/span")
    SUBMIT_DELETE_LOCATOR = (By.XPATH, "//button[contains(@class, 'button_confirm-remove')]")