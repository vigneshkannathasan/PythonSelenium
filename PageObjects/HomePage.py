from selenium.webdriver.common.by import By
from PageObjects.CheckoutPage import CheckoutPage


class HomePage:
    search_bar = (By.CSS_SELECTOR, '.search-keyword')
    selected_item = (By.XPATH, "//div[@class='products']/div")
    select_item_property = (By.XPATH, "//div[@class='products']/div/div/button")
    cart_item_property = (By.CSS_SELECTOR, "img[alt='Cart']")
    proceed_to_checkout_property = (By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")

    def __init__(self,driver):
        self.driver = driver

    def search_bar_option(self):
        return self.driver.find_element(*HomePage.search_bar)

    def select_items(self):
        return self.driver.find_elements(*HomePage.selected_item)

    def select_item(self):
        return self.driver.find_element(*HomePage.select_item_property)

    def cart_item(self):
        return self.driver.find_element(*HomePage.cart_item_property)

    def proceed_item(self):
        self.driver.find_element(*HomePage.proceed_to_checkout_property).click()
        checkout_page = CheckoutPage(self.driver)
        return checkout_page


