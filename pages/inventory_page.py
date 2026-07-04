from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import get_logger

class InventoryPage(BasePage):

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
        super().__init__(driver)
        self.logger = get_logger(__name__)

    def is_loaded(self):
        return self.get_text(self.TITLE) == "Products"

    def add_backpack_to_cart(self):
        self.click(self.BACKPACK_ADD_BUTTON)

    def remove_backpack_from_cart(self):
        self.click(self.BACKPACK_REMOVE_BUTTON)

    def open_cart(self):
        self.click(self.SHOPPING_CART_LINK)
    
    def get_cart_count(self):
        return self.get_text(self.SHOPPING_CART_BADGE)
    
    def is_cart_empty(self):
      self.logger.info("Checking if cart is empty")
      badges = self.driver.find_elements(*self.SHOPPING_CART_BADGE)
      return len(badges) == 0