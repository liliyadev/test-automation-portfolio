from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import get_logger


class CompletePage(BasePage):
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger(__name__)

    def is_order_complete(self):
        return self.get_text(self.COMPLETE_HEADER) == "Thank you for your order!"