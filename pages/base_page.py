# pages/base_page.py
import time
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    TimeoutException,
    NoSuchElementException,
)

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def find_element(self, locator):
        """Finds a single element with an explicit wait."""
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except (TimeoutException, NoSuchElementException):
            self.driver.save_screenshot("find_element_error.png")
            raise Exception(f"Element with locator {locator} not found.")

    def click(self, locator, pause=0):
        """Clicks an element safely, waiting until clickable and handling overlays."""
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            time.sleep(0.5)

            try:
                element.click()
            except ElementClickInterceptedException:
                self.driver.execute_script("arguments[0].click();", element)
            except Exception:
                self.driver.execute_script("arguments[0].click();", element)

            if pause > 0:
                time.sleep(pause)

        except TimeoutException:
            self.driver.save_screenshot("click_timeout_error.png")
            raise Exception(f"Timeout: Element {locator} not clickable within wait time.")
        except Exception as e:
            self.driver.save_screenshot("click_unexpected_error.png")
            raise Exception(f"Failed to click element {locator}. Error: {str(e)}")

    def type_text(self, locator, text, pause=0):
        """Types text into an input field."""
        try:
            element = self.find_element(locator)
            element.clear()
            element.send_keys(text)
            if pause > 0:
                time.sleep(pause)
        except Exception as e:
            self.driver.save_screenshot("type_text_error.png")
            raise Exception(f"Failed to type text into element {locator}. Error: {str(e)}")

    def select_dropdown(self, locator, value, pause=0):
        """Selects an option from a dropdown by visible text."""
        try:
            element = self.find_element(locator)
            select = Select(element)
            select.select_by_visible_text(str(value))
            if pause > 0:
                time.sleep(pause)
        except Exception as e:
            self.driver.save_screenshot("select_dropdown_error.png")
            raise Exception(f"Failed to select '{value}' in dropdown {locator}. Error: {str(e)}")
