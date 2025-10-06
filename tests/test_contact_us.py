import pytest
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.contact_us_page import ContactUsPage
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

@pytest.mark.order(7)
def test_contact_us(driver):
    contact_us = ContactUsPage(driver)
    contact_us.go_to_contact_us_page()

    contact_us.fill_contact_form(
        name="John Doe",
        email="john@example.com",
        subject="Testing Contact Us",
        message="This is a sample message for testing.",
    )

    # 🧠 Dynamically get absolute path
    file_path = os.path.abspath("sample-for-contact-test/shirt-coral.jpg")
    print("Uploading file:", file_path)  # just to verify
    contact_us.upload_file(file_path)

    contact_us.submit_form()
    
    contact_us.go_back_home()
