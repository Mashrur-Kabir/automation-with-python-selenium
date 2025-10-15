import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.home_page import HomePage
from pages.register_page import RegisterPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.config import BASE_URL


@pytest.mark.order(6)
def test_checkout_process(driver):
    home = HomePage(driver)
    register = RegisterPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    # Step 1: Register again since old account was deleted
    home.go_to_signup_login()
    register.signup("Kabirs", "kabir95i@gmail.com")
    register.fill_account_info(
        password="123ert",
        day="15",
        month="February",
        year="2005",
        firstname="Mashrur",
        lastname="Kabir",
        address="3761 St. John Street, Saskatchewan, Weldon",
        country="Canada",
        state="Ontario",
        city="Oakville",
        zipcode="L6J 3X4",
        mobile="905-337-6242"
    )
    register.create_account()

    # Step 2: Add a product and go to cart
    cart.add_items_to_cart()

    # Step 3: Proceed to checkout
    cart.remove_item_from_cart()  # Optional cleanup of one product
    checkout.proceed_to_checkout()

    # Step 4: Write message
    checkout.add_message("Please deliver between 9am-5pm")

    # Step 5: Place order and fill payment
    checkout.place_order()
    checkout.fill_payment_details(
        name="Mashrur Kabir",
        card_number="4242424242424242",
        cvc="311",
        month="03",
        year="2030"
    )

    # Step 6: Download invoice and finish order
    checkout.finish_order()
    
    # Step 7: Delete account after order completion
    checkout.delete_account()
