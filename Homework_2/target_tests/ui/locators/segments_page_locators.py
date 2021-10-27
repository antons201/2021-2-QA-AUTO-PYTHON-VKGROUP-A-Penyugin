from selenium.webdriver.common.by import By
from ui.locators.auth_page_locators import AuthPageLocators


class SegmentsPageLocators(AuthPageLocators):
    NEW_SEGMENT_LOCATOR = (By.CSS_SELECTOR, "a[href='/segments/segments_list/new/']")
    CREATE_SEGMENT_LOCATOR = (By.XPATH, "//div[contains(@class, 'button__text') and contains(string(), 'Создать сегмент')]")
    SUBMIT_ADD_LOCATOR = (By.XPATH, "//div[contains(@class, 'button__text') and contains(string(), 'Добавить сегмент')]")
    SELECT_SEGMENT_LOCATOR = (By.XPATH, "//div[contains(@class, 'adding-segments-item') and "
                                        "contains(string(), 'Приложения и игры в соцсетях')]")
    SEGMENT_SOURCE_CHECKBOX_LOCATOR = (By.CSS_SELECTOR, "input[class^='adding-segments-source__checkbox']")
    CLOSE_LOCATOR = (By.XPATH, "//div[contains(@class, 'button__text') and contains(string(), 'Закрыть')]")
    SEGMENT_NAME_LOCATOR = (By.XPATH, "//div[contains(@class, 'input_create-segment-form')]/div[@class='input__wrap']/input")
    SEGMENT_LOCATOR = (By.XPATH, "//a[@title='{}']")
    DELETE_SEGMENT_LOCATOR = (By.XPATH, "//a[@title='{}']/../../../div[contains(@data-test, 'remove')]/span")
    SUBMIT_DELETE_LOCATOR = (By.XPATH, "//div[contains(@class, 'button__text') and contains(string(), 'Удалить')]")