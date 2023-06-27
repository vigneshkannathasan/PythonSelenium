from selenium.webdriver.common.by import By


class CheckoutPage:

    promo_code_property = (By.CSS_SELECTOR, '.promoCode')
    promo_button_property = (By.CSS_SELECTOR, '.promoBtn')
    promo_info_property = (By.CSS_SELECTOR, '.promoInfo')
    item_price_property = (By.CSS_SELECTOR, "tr td:nth-child(5) p")
    total_amount_property = (By.CSS_SELECTOR, ".totAmt")

    def __init__(self,driver):
        self.driver = driver

    def promo_code_item(self):
        return self.driver.find_element(*CheckoutPage.promo_code_property)

    def promo_button_item(self):
        return self.driver.find_element(*CheckoutPage.promo_button_property)

    def promo_info_item(self):
        return self.driver.find_element(*CheckoutPage.promo_info_property)

    def item_price(self):
        return self.driver.find_elements(*CheckoutPage.item_price_property)

    def total_amount_item(self):
        return self.driver.find_element(*CheckoutPage.total_amount_property)


