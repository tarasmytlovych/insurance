from selenium import webdriver
from unittest import TestCase
from source_code.start_page import StartPage
from source_code.mortgage_page import MortgagePage
from source_code.payment_calculator import PaymentCalculator


class Tests(TestCase):


    def test_a_slider_moing(self):
        start_page = StartPage()
        start_page.set_language("EN")
        start_page.click_loans_button()
        mortgage_page = start_page.click_mortgage_button()
        mortgage_page.scroll_mortgage_page()
        payment_calculator = mortgage_page.click_calculate_your_payments()
        payment_calculator.scroll_payment_page()
        payment_calculator.move_slider()

        self.assertNotEqual(payment_calculator.PURCHASE_CLIDER_LOCATION_BEFORE_MOVING,
                         payment_calculator.PURCHASE_CLIDER_LOCATION_AFTER_MOVING,
                         "Slider is not mooved")

    def test_b_calculation(self):
        payment_calculator = PaymentCalculator()
        payment_calculator.set_purchase_price("500000")



