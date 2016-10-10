from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select


class PaymentCalculator(BasePage):

    PURCHASE_PRICE_SLIDER = (By.CSS_SELECTOR,
                             "div.row.fond-formulaire.bleu-pale + div.row div.slider-track div.slider-handle.min-slider-handle.custom")
    PURCHASE_CLIDER_LOCATION_BEFORE_MOVING = None
    PURCHASE_CLIDER_LOCATION_AFTER_MOVING = None

    PURCHASE_PRICE_PLUS_BUTTON = (By.CSS_SELECTOR, "button#PrixProprietePlus")
    PURCHASE_PRICE_INPUT_FIELD = (By.CSS_SELECTOR, "div.inputSlide-ia.clearfix input#PrixPropriete")

    DOWN_PAYMENTS_INPUT = (By.CSS_SELECTOR, "input#MiseDeFond")
    DOWN_PAYMENTS_PLUS_BUTTON = (By.ID, "MiseDeFondPlus")

    AMORTIZATION = (By.ID, "Amortissement")

    TAX_INTEREST_INPUT = (By.ID, "TauxInteret")
    FREQUENCY_PAYMENT = (By.ID, "FrequenceVersement")
    CALCULATE_BUTTON = (By.ID, "btn_calculer")

    ERROR = (By.CLASS_NAME, 'icone-validation-erreur')

    CALCULATION_RESULT = (By.CSS_SELECTOR, "span#paiement-resultats")

    def _get_purchase_slider(self):
        return self.wait_for_visibility_of_element(self.PURCHASE_PRICE_SLIDER)

    def _get_purchase_price_input(self):
        return self.wait_for_visibility_of_element(self.PURCHASE_PRICE_INPUT_FIELD)

    def _get_purchase_plus_btn(self):
        return self.wait_for_visibility_of_element(self.PURCHASE_PRICE_PLUS_BUTTON)

    def _get_down_payments_input(self):
        return self.wait_for_visibility_of_element(self.DOWN_PAYMENTS_INPUT)

    def _get_down_payments_plus_button(self):
        return self.wait_for_visibility_of_element(locator = self.DOWN_PAYMENTS_PLUS_BUTTON)

    def _get_amortization_dropdown(self):
        return self.wait_for_visibility_of_element(self.AMORTIZATION)

    def _get_tax_interest_input(self):
        return self.wait_for_visibility_of_element(self.TAX_INTEREST_INPUT)

    def _get_frequency_dropdown(self):
        return self.wait_for_visibility_of_element(self.FREQUENCY_PAYMENT)

    def _get_calculate_button(self):
        return self.wait_for_element_to_be_clickable(self.CALCULATE_BUTTON)

    def _get_calculate_result(self):
        return self.wait_for_visibility_of_element(self.CALCULATION_RESULT)

    def scroll_payment_page(self):
        self.driver.execute_script('window.scrollTo(0, 600)')

    def move_slider(self):
        self.PURCHASE_CLIDER_LOCATION_BEFORE_MOVING = self._get_purchase_slider().location
        actionChains = ActionChains(self.driver)
        actionChains.drag_and_drop_by_offset(self._get_purchase_slider(), 50, 0)
        actionChains.perform()
        self.PURCHASE_CLIDER_LOCATION_AFTER_MOVING = self._get_purchase_slider().location

    # def prints(self):
    #     print self.PURCHASE_CLIDER_LOCATION_BEFORE_MOVING, self.PURCHASE_CLIDER_LOCATION_AFTER_MOVING

    def set_purchase_price(self, purchase_price):
         self._get_purchase_price_input().clear()
         slider_values = ('250000', '500000', '750000', '1000000')
         if (float(purchase_price) < 0 or float(purchase_price) > 1000000.00):
             print "Out of boundaries. Please enter values from 0 to 1 000 000"
         else:
             if purchase_price in slider_values:
                 while self._get_purchase_price_input().get_attribute('value') != purchase_price:
                      self._get_purchase_plus_btn().click()
             else:
                 self._get_purchase_price_input().send_keys(purchase_price)

    def set_down_payments(self, down_payments):
        self._get_down_payments_input().clear()
        slider_values = ('50000', '100000', '150000', '200000')
        if (float(down_payments) < 0 or float(down_payments) > 200000.00):
            print "Out of boundaries. Please enter values from 0 to 200 000"
        else:
            if down_payments in slider_values:
                 while self._get_down_payments_input().get_attribute('value') != down_payments:
                      self._get_down_payments_plus_button().click()
            else:
                self._get_down_payments_input().send_keys(down_payments)


    def set_amortization(self, amortization):
        element = self._get_amortization_dropdown()
        select = Select(element)
        select.select_by_value(amortization)

    def set_tax_interest(self, tax_input):
        self._get_tax_interest_input().clear()
        self._get_tax_interest_input().send_keys(tax_input)

    def set_payment_frequent(self, frequence):

        value_frequence_dict = {'12': ('Monthly', 'Mensuel'), '26': ('Biweekly', 'A la quinzine'),
                                '24': ('Biweekly +', 'A la quinzine +'), '52': ('weekly', 'Hebdomadaire'),
                                '48': ('weekly +', 'Hebdomadaire +')}

        for k, v in value_frequence_dict.iteritems():
            if frequence in v:
                element = self._get_frequency_dropdown()
                select = Select(element)
                select.select_by_value(k)

    def click_calculate_button(self):
        self.scroll_payment_page()
        self._get_calculate_button().click()

    def get_calculation_result(self):
        result = self._get_calculate_result().text
        onlyFigures = result.replace('$', ("")).strip()
        return onlyFigures








