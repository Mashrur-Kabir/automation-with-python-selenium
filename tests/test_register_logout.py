import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from utils.config import BASE_URL

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")   # optional
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    # 👇 Go to the target website before tests start
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.mark.order(1) #for testing order of components/features
def test_register_and_logout(driver):
    home = HomePage(driver)
    register = RegisterPage(driver)

    # Step 1: Go to signup
    home.go_to_signup_login()

    # Step 2: Signup with name/email
    register.signup("Kabirr", "kabir951@gmail.com")

    # Step 3: Fill details
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

    # Step 4: Create account + Continue
    register.create_account()

    # Step 5: Logout
    register.logout()
