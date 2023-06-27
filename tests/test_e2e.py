import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.HomePage import HomePage
from utilities.BaseFile import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.logger()
        expected_list = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
        actual_list = []
        home_page = HomePage(self.driver)
        home_page.search_bar_option().send_keys('ber')
        time.sleep(2)
        items = home_page.select_items()
        assert len(items) > 0

        for item in items:
            actual_list.append(item.find_element(By.XPATH, 'h4').text)
            item.find_element(By.XPATH, 'div/button').click()
            time.sleep(1)
        assert expected_list == actual_list
        home_page.cart_item().click()
        checkout_page = home_page.proceed_item()
        checkout_page.promo_code_item().send_keys('rahulshettyacademy')
        checkout_page.promo_button_item().click()
        self.explicit_wait((By.CSS_SELECTOR, '.promoInfo'))
        log.info(checkout_page.promo_info_item().text)
        prices = checkout_page.item_price()
        sum = 0
        for price in prices:
            sum = sum + int(price.text)

        total_price = checkout_page.total_amount_item().text
        log.info('validation on progress')
        assert sum == int(total_price)



class TestThree(BaseClass):

    def test_e2e_3(self):
        home_page = HomePage(self.driver)
        home_page.search_bar_option().send_keys('carrot')
        home_page.select_item().click()
        home_page.cart_item().click()
        checkout_page = home_page.proceed_item()
        checkout_page.promo_code_item().send_keys('rahulshettyacademy')
        checkout_page.promo_button_item().click()
        self.explicit_wait((By.CSS_SELECTOR, '.promoInfo'))
        print(checkout_page.promo_info_item().text)
        prices = checkout_page.item_price()
        sum = 0
        for price in prices:
            sum = sum + int(price.text)

        total_price = checkout_page.total_amount_item().text

        assert sum == int(total_price)