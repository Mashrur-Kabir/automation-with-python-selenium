# pages/register_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegisterPage(BasePage):
    # Locators
    NAME_INPUT = (By.XPATH, "//input[@data-qa='signup-name']")
    EMAIL_INPUT = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP_BUTTON = (By.XPATH, "//button[@data-qa='signup-button']")

    MR_RADIO = (By.ID, "id_gender1")
    PASSWORD_INPUT = (By.ID, "password")
    DAYS_SELECT = (By.ID, "days")
    MONTHS_SELECT = (By.ID, "months")
    YEARS_SELECT = (By.ID, "years")

    FIRSTNAME_INPUT = (By.ID, "first_name")
    LASTNAME_INPUT = (By.ID, "last_name")
    ADDRESS_INPUT = (By.ID, "address1")
    COUNTRY_SELECT = (By.ID, "country")
    STATE_INPUT = (By.ID, "state")
    CITY_INPUT = (By.ID, "city")
    ZIPCODE_INPUT = (By.ID, "zipcode")
    MOBILE_INPUT = (By.ID, "mobile_number")

    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[@data-qa='create-account']")
    CONTINUE_BUTTON = (By.XPATH, "//a[@data-qa='continue-button']")
    LOGOUT_BUTTON = (By.XPATH, "//a[@href='/logout']")

    # Actions
    def signup(self, name, email):
        self.type_text(self.NAME_INPUT, name, pause=1)
        self.type_text(self.EMAIL_INPUT, email, pause=1)
        self.click(self.SIGNUP_BUTTON, pause=2)

    def fill_account_info(
        self, password, day, month, year, firstname, lastname,
        address, country, state, city, zipcode, mobile
    ):
        self.click(self.MR_RADIO, pause=1)
        self.type_text(self.PASSWORD_INPUT, password, pause=1)
        self.select_dropdown(self.DAYS_SELECT, day, pause=1)
        self.select_dropdown(self.MONTHS_SELECT, month, pause=1)
        self.select_dropdown(self.YEARS_SELECT, year, pause=1)
        self.type_text(self.FIRSTNAME_INPUT, firstname, pause=1)
        self.type_text(self.LASTNAME_INPUT, lastname, pause=1)
        self.type_text(self.ADDRESS_INPUT, address, pause=1)
        self.select_dropdown(self.COUNTRY_SELECT, country, pause=1)
        self.type_text(self.STATE_INPUT, state, pause=1)
        self.type_text(self.CITY_INPUT, city, pause=1)
        self.type_text(self.ZIPCODE_INPUT, zipcode, pause=1)
        self.type_text(self.MOBILE_INPUT, mobile, pause=1)

    def create_account(self):
        self.click(self.CREATE_ACCOUNT_BUTTON, pause=2)
        self.click(self.CONTINUE_BUTTON, pause=2)

    def logout(self):
        self.click(self.LOGOUT_BUTTON, pause=2)
