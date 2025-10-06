from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    VIEW_DETAILS_PRODUCT1 = (By.CSS_SELECTOR, "a[href='/product_details/4']")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-default.cart")
    CONTINUE_SHOPPING_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-success.close-modal.btn-block")
    POLO_BRAND = (By.CSS_SELECTOR, "a[href='/brand_products/Polo']")
    VIEW_DETAILS_PRODUCT2 = (By.CSS_SELECTOR, "a[href='/product_details/8']")
    CART_TAB = (By.CSS_SELECTOR, "a[href='/view_cart']")
    REMOVE_PRODUCT = (By.CSS_SELECTOR, "a.cart_quantity_delete[data-product-id='8']")

    def add_items_to_cart(self):
        self.click(self.VIEW_DETAILS_PRODUCT1, pause=2)
        self.click(self.ADD_TO_CART_BUTTON, pause=1)
        self.click(self.CONTINUE_SHOPPING_BUTTON, pause=2)
        self.click(self.POLO_BRAND, pause=2)
        self.click(self.VIEW_DETAILS_PRODUCT2, pause=2)
        self.click(self.ADD_TO_CART_BUTTON, pause=1)
        self.click(self.CONTINUE_SHOPPING_BUTTON, pause=2)

    def remove_item_from_cart(self):
        self.click(self.CART_TAB, pause=2)
        self.click(self.REMOVE_PRODUCT, pause=2)
