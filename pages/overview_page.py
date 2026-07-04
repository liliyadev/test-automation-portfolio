from selenium.webdriver.common.by import By


class OverviewPage:
    FINISH_BUTTON = (By.ID, "finish")

    def __init__(self, driver):
        self.driver = driver

    def click_finish(self):
        self.driver.find_element(*self.FINISH_BUTTON).click()