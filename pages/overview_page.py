from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import get_logger


class OverviewPage(BasePage):
    FINISH_BUTTON = (By.ID, "finish")

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger(__name__)

    def click_finish(self):
        self.click(self.FINISH_BUTTON)