from ui.locators.base_page_locators import BasePageLocators
from appium.webdriver.common.mobileby import MobileBy


class NewsSourcesPageLocators(BasePageLocators):
    NEWS_TYPE_LOCATOR = "//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout['{" \
                        "}']/android.widget.TextView[contains(@text, '{}')] "
    BACK_BUTTON_LOCATOR = (MobileBy.XPATH, "//android.widget.LinearLayout/android.widget.ImageButton")
    NEWS_SELECTED_LOCATOR = "//android.widget.FrameLayout['{}']/android.widget.ImageView"
