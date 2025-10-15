import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.cart_page import CartPage
from utils.config import BASE_URL

@pytest.mark.order(5)
def test_cart_functionality(driver):
    cart = CartPage(driver)
    cart.add_items_to_cart()
    cart.remove_item_from_cart()
