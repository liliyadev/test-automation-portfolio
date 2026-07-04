from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.settings import STANDARD_USERNAME, PASSWORD, INVALID_PASSWORD

def test_valid_login(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login(STANDARD_USERNAME, PASSWORD)

    assert inventory_page.is_loaded()


def test_invalid_login(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login(STANDARD_USERNAME, INVALID_PASSWORD)

    error_message = login_page.get_error_message()

    assert "Username and password do not match" in error_message