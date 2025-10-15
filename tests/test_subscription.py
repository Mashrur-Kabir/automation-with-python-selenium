import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage
from utils.config import BASE_URL


@pytest.mark.order(3)
def test_subscription(driver):
    home = HomePage(driver)
    home.subscribe("kabirr44@gmail.com")
