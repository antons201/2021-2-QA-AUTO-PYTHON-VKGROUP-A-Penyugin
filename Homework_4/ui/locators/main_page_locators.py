from ui.locators.base_page_locators import BasePageLocators
from appium.webdriver.common.mobileby import MobileBy


class MainPageLocators(BasePageLocators):
    AGREE_FOREGROUND_LOCATOR = (MobileBy.ID, "com.android.permissioncontroller:id"
                                             "/permission_allow_foreground_only_button")
    AGREE_LOCATOR = (MobileBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
    KEYBOARD_LOCATOR = (MobileBy.ID, "ru.mail.search.electroscope:id/keyboard")
    SEARCH_INPUT_LOCATOR = (MobileBy.ID, "ru.mail.search.electroscope:id/input_text")
    SEARCH_BUTTON_LOCATOR = (MobileBy.ID, "ru.mail.search.electroscope:id/text_input_action")
    CARD_TITLE_LOCATOR = (MobileBy.ID, "ru.mail.search.electroscope:id/item_dialog_fact_card_title")
    CARD_DESCRIPTION_LOCATOR = (MobileBy.ID, "ru.mail.search.electroscope:id/item_dialog_fact_card_content_text")
    SUGGEST_LIST_LOCATOR = (MobileBy.ID, "ru.mail.search.electroscope:id/suggests_list")
    SUGGEST_LOCATOR = "//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView[" \
                      "contains(@text, '{}')] "
    SUGGEST_TITLE_LOCATOR = "//android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[" \
                            "contains(@text, '{}')] "
    RESPONSE_LOCATOR = "//androidx.recyclerview.widget.RecyclerView/android.widget.TextView[contains(@text, '{}')]"
    MENU_LOCATOR = (MobileBy.ID, "ru.mail.search.electroscope:id/assistant_menu_bottom")
