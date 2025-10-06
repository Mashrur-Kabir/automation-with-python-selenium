import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.config import BASE_URL

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.mark.order(2)
def test_login_and_delete_account(driver):
    home = HomePage(driver)
    login = LoginPage(driver)

    # Step 1: Go to login page
    home.go_to_signup_login()

    # Step 2: Perform login
    login.login("kabir951@gmail.com", "123ert")

    # Step 3: Delete account
    login.delete_account()
