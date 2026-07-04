from selenium.webdriver.common.by import By
from utils.logger import get_logger

class InventoryPage:

    TITLE = (By.CLASS_NAME, "title")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    BACKPACK_ADD_BUTTON = (
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    )

    BACKPACK_REMOVE_BUTTON = (
          By.ID,
          "remove-sauce-labs-backpack"
      )

    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger(__name__)

    def is_loaded(self):
        return (
            self.driver.find_element(*self.TITLE).text
            == "Products"
        )

    def add_backpack_to_cart(self):
        self.logger.info("Adding Backpack to cart")
        self.driver.find_element(*self.BACKPACK_ADD_BUTTON).click()
    
    def get_cart_count(self):
        return self.driver.find_element(
            *self.SHOPPING_CART_BADGE
        ).text
    
    def remove_backpack_from_cart(self):
      self.logger.info("Removing Backpack from cart")
      self.driver.find_element(*self.BACKPACK_REMOVE_BUTTON).click()
    
    def is_cart_empty(self):
      self.logger.info("Checking if cart is empty")
      badges = self.driver.find_elements(*self.SHOPPING_CART_BADGE)
      return len(badges) == 0
    
    def open_cart(self):
      self.logger.info("Opening cart")
      self.driver.find_element(*self.SHOPPING_CART_LINK).click()