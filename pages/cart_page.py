from selenium.webdriver.common.by import By
from utils.logger import get_logger

class CartPage:
    CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")

    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger(__name__)

    def get_item_name(self):
        self.logger.info("Getting item name from cart")
        return self.driver.find_element(*self.CART_ITEM_NAME).text

    def is_backpack_in_cart(self):
        return self.get_item_name() == "Sauce Labs Backpack"

    def click_checkout(self):
        self.logger.info("Clicking checkout")
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()

    def continue_shopping(self):
        self.driver.find_element(*self.CONTINUE_SHOPPING_BUTTON).click()