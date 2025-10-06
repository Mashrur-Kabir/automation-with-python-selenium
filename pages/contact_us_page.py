from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ContactUsPage(BasePage):
    # Locators
    CONTACT_US_LINK = (By.LINK_TEXT, "Contact us")
    NAME_INPUT = (By.NAME, "name")
    EMAIL_INPUT = (By.NAME, "email")
    SUBJECT_INPUT = (By.NAME, "subject")
    MESSAGE_TEXTAREA = (By.ID, "message")
    UPLOAD_INPUT = (By.NAME, "upload_file")
    SUBMIT_BUTTON = (By.NAME, "submit")
    HOME_BUTTON = (By.CSS_SELECTOR, "a.btn.btn-success")  # or a more specific selector if needed

    # Actions
    def go_to_contact_us_page(self):
        self.click(self.CONTACT_US_LINK, pause=1)

    def fill_contact_form(self, name, email, subject, message):
        self.type_text(self.NAME_INPUT, name, pause=1)
        self.type_text(self.EMAIL_INPUT, email, pause=1)
        self.type_text(self.SUBJECT_INPUT, subject, pause=1)
        self.type_text(self.MESSAGE_TEXTAREA, message, pause=1)

    def upload_file(self, file_path):
        self.type_text(self.UPLOAD_INPUT, file_path, pause=1)

    def submit_form(self):
        self.click(self.SUBMIT_BUTTON, pause=2)
        alert = self.driver.switch_to.alert
        alert.accept()  # ✅ clicks "OK"
        
    def go_back_home(self):
        self.click(self.HOME_BUTTON, pause=2)

