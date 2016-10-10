from .base_page import BasePage
from selenium.webdriver.common.by import By
from .mortgage_page import MortgagePage


class StartPage(BasePage):
    LANG_MENU_ITEM = (By.ID, "topLangMenuItem")
    LOANS_BUTTON = (By.CSS_SELECTOR, "a[data-utag-name='loans']")
    MORTGAGE_BUTTON = (By.CSS_SELECTOR, "a[data-utag-name='mortgage_loan']")

    def _get_lang_menu_item(self):
        return self.wait_for_visibility_of_element(locator=self.LANG_MENU_ITEM)

    def _get_loans_button(self):
        return self.wait_for_visibility_of_element(locator=self.LOANS_BUTTON)

    def _get_mortgage_button(self):
        return self.wait_for_visibility_of_element(locator=self.MORTGAGE_BUTTON)

    def set_language(self, language):
        current_displayed_language_icon = self._get_lang_menu_item().text
        if current_displayed_language_icon == language:
            self._get_lang_menu_item().click()
        else:
            pass

    def click_loans_button(self):
        self._get_loans_button().click()

    def click_mortgage_button(self):
        self._get_mortgage_button().click()
        return MortgagePage (driver = self.driver)
