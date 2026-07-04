from selenium.webdriver.common.by import By


class CompletePage:
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver

    def is_order_complete(self):
        return self.driver.find_element(*self.COMPLETE_HEADER).text == "Thank you for your order!"