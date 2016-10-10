from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement


class PaymentCalculator(BasePage):

    PURCHASE_PRICE_SLIDER = (By.CSS_SELECTOR,
                             "div.row.fond-formulaire.bleu-pale + div.row div.slider-track div.slider-handle.min-slider-handle.custom")
    PURCHASE_CLIDER_LOCATION_BEFORE_MOVING = None
    PURCHASE_CLIDER_LOCATION_AFTER_MOVING = None

    PURCHASE_PRICE_PLUS_BUTTON = (By.CSS_SELECTOR, "button#PrixProprietePlus")
    PURCHASE_PRICE_INPUT_FIELD = (By.CSS_SELECTOR, "input#PrixPropriete")


    def _get_purchase_slider(self):
        return self.wait_for_visibility_of_element(self.PURCHASE_PRICE_SLIDER)

    def _get_purchase_price_input(self):
        return self.wait_for_visibility_of_element(self.PURCHASE_PRICE_INPUT_FIELD)

    def _get_purchase_plus_btn(self):
        return self.wait_for_visibility_of_element(self.PURCHASE_PRICE_PLUS_BUTTON)

    def scroll_payment_page(self):
        self.driver.execute_script('window.scrollTo(0, 600)')

    def move_slider(self):
        self.PURCHASE_CLIDER_LOCATION_BEFORE_MOVING = self._get_purchase_slider().location
        actionChains = ActionChains(self.driver)
        actionChains.drag_and_drop_by_offset(self._get_purchase_slider(), 50, 0)
        actionChains.perform()
        self.PURCHASE_CLIDER_LOCATION_AFTER_MOVING = self._get_purchase_slider().location
        self._get_purchase_plus_btn().click()
        print self._get_purchase_price_input().text
    #     self.prints()
    #
    # def prints(self):
    #     print self.PURCHASE_CLIDER_LOCATION_BEFORE_MOVING, self.PURCHASE_CLIDER_LOCATION_AFTER_MOVING

    def set_purchase_price(self, purchase_price):
         self._get_purchase_price_input().clear()
        # while self._get_purchase_price_input().text != purchase_price:
        #     print self._get_purchase_price_input().text
         if self._get_purchase_price_input().text != purchase_price:
             print self._get_purchase_price_input().text
             self._get_purchase_plus_btn().click()
             print self._get_purchase_price_input().text

