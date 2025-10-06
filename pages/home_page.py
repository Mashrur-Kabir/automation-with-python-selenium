from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    SIGNUP_LOGIN_LINK = (By.CSS_SELECTOR, "a[href='/login']")
    SUBSCRIBE_EMAIL_FIELD = (By.ID, "susbscribe_email")

    def go_to_signup_login(self):
        self.click(self.SIGNUP_LOGIN_LINK, pause=2)
        
    
    def subscribe(self, email):
        self.type_text(self.SUBSCRIBE_EMAIL_FIELD, email, pause=1)
