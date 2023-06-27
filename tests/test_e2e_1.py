import pytest
from selenium.webdriver.common.by import By

from PageObjects.HomePage import HomePage
from TestData.HomePageData import HomePageData
from utilities.BaseFile import BaseClass


class TestTwo(BaseClass):

    def test_e2e_1(self,get_data):
        home_page = HomePage(self.driver)
        home_page.search_bar_option().send_keys(get_data['veg'])
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

    @pytest.fixture(params= HomePageData.test_homepage_data)
    def get_data(self,request):
        return request.param