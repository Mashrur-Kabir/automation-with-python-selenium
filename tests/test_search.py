import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.search_page import SearchPage
from utils.config import BASE_URL


@pytest.mark.order(4)
def test_search_functionality(driver):
    search = SearchPage(driver)
    search.search_product("winter top")
    search.browse_categories_and_brands()
