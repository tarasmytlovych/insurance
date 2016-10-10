from selenium.webdriver.common.by import By
from .base_page import BasePage
from .payment_calculator import PaymentCalculator

class MortgagePage(BasePage):

    CALCULATE_YOUR_PAYMENTS_BUTTON = (By.CSS_SELECTOR,
                                      "a[data-utag-name='calculate_your_payments'][data-utag-type='button']")

    def _get_calculate_payments_button(self):
        return self.wait_for_visibility_of_element(locator = self.CALCULATE_YOUR_PAYMENTS_BUTTON)


    def scroll_mortgage_page(self):
        self.driver.execute_script('window.scrollTo(0, 600)')




    def click_calculate_your_payments(self):
        self._get_calculate_payments_button().click()
        return PaymentCalculator(driver = self.driver)