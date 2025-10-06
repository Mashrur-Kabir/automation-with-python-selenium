from selenium.webdriver.common.by import By
from .base_page import BasePage

class SearchPage(BasePage):
    PRODUCTS_TAB = (By.CSS_SELECTOR, "a[href='/products']")
    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    WOMEN_CATEGORY = (By.XPATH, "//a[@href='#Women']")
    DRESS_SUBCATEGORY = (By.CSS_SELECTOR, "a[href='/category_products/1']")
    PRODUCTS_LINK = (By.CSS_SELECTOR, "a[href='/products']")
    BABYHUG_BRAND = (By.CSS_SELECTOR, "a[href='/brand_products/Babyhug']")

    def search_product(self, term):
        self.click(self.PRODUCTS_TAB)
        self.type_text(self.SEARCH_INPUT, term)
        self.click(self.SEARCH_BUTTON, pause=2)

    def browse_categories_and_brands(self):
        self.click(self.WOMEN_CATEGORY, pause=1)
        self.click(self.DRESS_SUBCATEGORY, pause=2)
        self.driver.execute_script("window.scrollBy(0, 400);")
        self.click(self.PRODUCTS_LINK, pause=2)
        self.click(self.BABYHUG_BRAND, pause=2)
        self.driver.execute_script("window.scrollBy(0, 400);")
        

