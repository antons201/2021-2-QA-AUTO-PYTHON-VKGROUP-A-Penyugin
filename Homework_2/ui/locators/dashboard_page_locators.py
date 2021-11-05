from selenium.webdriver.common.by import By
from ui.locators.auth_page_locators import AuthPageLocators


class DashboardPageLocators(AuthPageLocators):
    NEW_COMPANY_LOCATOR = (By.CSS_SELECTOR, "a[href='/campaign/new']")
    CREATE_COMPANY_LOCATOR = (By.XPATH, "//div[contains(@class, 'dashboard-module-createButtonWrap')]/div")
    TRAFFIC_LOCATOR = (By.CSS_SELECTOR, "div[class$='traffic']")
    LINK_LOCATOR = (By.CSS_SELECTOR, "input[data-gtm-id='ad_url_text']")
    COMPANY_NAME_LOCATOR = (By.XPATH, "//div[contains(@class, 'input_campaign-name')]/div[@class='input__wrap']/input")
    FORMAT_LOCATOR = (By.CSS_SELECTOR, "div[id^='patterns_banner']")
    UPLOAD_LOCATOR = (By.XPATH, "//div[contains(@class, 'upload-module-wrapper')]/input[contains(@data-test, 'image_240x400')]")
    UPLOAD_PROCESS_LOCATOR = (By.XPATH, "//div[contains(@class, 'roles-module-uploadButton')]")
    SUBMIT_CREATE_LOCATOR = (By.XPATH, "//div[contains(@class, 'js-save-button-wrap')]/button")
    COMPANY_LOCATOR = (By.XPATH, "//a[@title='{}']")
