from selenium.webdriver.common.by import By
from utils.logger import get_logger
from config.settings import BASE_URL

class LoginPage:
    URL = BASE_URL

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger(__name__)

    def open(self):
        self.logger.info("Opening Login Page")
        self.driver.get(self.URL)

    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def login(self, username, password):
        self.logger.info(f"Logging in as {username}")

        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text