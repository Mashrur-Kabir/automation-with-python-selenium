from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutPage(BasePage):
    PROCEED_TO_CHECKOUT = (By.CSS_SELECTOR, "a.btn.btn-default.check_out")
    MESSAGE_TEXTAREA = (By.CSS_SELECTOR, "textarea[name='message']")
    PLACE_ORDER = (By.CSS_SELECTOR, "a[href='/payment'].btn.btn-default.check_out")

    NAME_ON_CARD = (By.CSS_SELECTOR, "input[name='name_on_card']")
    CARD_NUMBER = (By.CSS_SELECTOR, "input[name='card_number']")
    CVC = (By.CSS_SELECTOR, "input[name='cvc']")
    EXPIRY_MONTH = (By.CSS_SELECTOR, "input[name='expiry_month']")
    EXPIRY_YEAR = (By.CSS_SELECTOR, "input[name='expiry_year']")
    PAY_AND_CONFIRM = (By.CSS_SELECTOR, "button[data-qa='pay-button']")
    DOWNLOAD_INVOICE = (By.CSS_SELECTOR, "a[href^='/download_invoice']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "a[data-qa='continue-button']")
    
    #delete to erase the account after ordering
    DELETE_ACCOUNT_LINK = (By.CSS_SELECTOR, "a[href='/delete_account']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "a[data-qa='continue-button']")
    
    def proceed_to_checkout(self):
        self.click(self.PROCEED_TO_CHECKOUT, pause=2)

    def add_message(self, message):
        self.type_text(self.MESSAGE_TEXTAREA, message, pause=1)

    def place_order(self):
        self.click(self.PLACE_ORDER, pause=2)

    def fill_payment_details(self, name, card_number, cvc, month, year):
        self.type_text(self.NAME_ON_CARD, name)
        self.type_text(self.CARD_NUMBER, card_number)
        self.type_text(self.CVC, cvc)
        self.type_text(self.EXPIRY_MONTH, month)
        self.type_text(self.EXPIRY_YEAR, year)
        self.click(self.PAY_AND_CONFIRM, pause=2)

    def finish_order(self):
        self.click(self.DOWNLOAD_INVOICE, pause=2)
        self.click(self.CONTINUE_BUTTON, pause=2)
        
    def delete_account(self):
        self.click(self.DELETE_ACCOUNT_LINK, pause=2)
        self.click(self.CONTINUE_BUTTON, pause=2)
    

