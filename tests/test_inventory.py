from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_add_backpack_to_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_backpack_to_cart()

    assert inventory_page.get_cart_count() == "1"

def test_remove_backpack_from_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_backpack_to_cart()
    inventory_page.remove_backpack_from_cart()

    assert inventory_page.is_cart_empty()