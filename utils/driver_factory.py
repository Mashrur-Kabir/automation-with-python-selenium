'''
CENTRALIZING BROWSER DRIVER SETUP (FOR FUTURE REFERENCE):

#What is driver_factory.py + conftest.py integration?:---

Right now, THE tests create the Chrome driver directly like this:

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

That means testers are stuck with Chrome
If tomorrow they want to test on Firefox, they’ll have to change every file.

#What driver_factory.py does:---

It’s a helper that creates a driver based on input — Chrome, Firefox, or Edge.

For example:

    # utils/driver_factory.py
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium.webdriver.firefox.service import Service as FirefoxService
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.firefox import GeckoDriverManager

    def create_driver(browser_name="chrome"):
        if browser_name == "chrome":
            return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif browser_name == "firefox":
            return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

#Then, in conftest.py:---

    import pytest
    from utils.driver_factory import create_driver

    @pytest.fixture
    def driver():
        # Choose your browser here
        driver = create_driver("chrome")
        driver.maximize_window()
        yield driver
        driver.quit()


**Now all the tests use this single fixture:

    def test_example(driver):
        driver.get("https://automationexercise.com")


#Benefits:---

-Centralized driver setup
-Easy switch: just change "chrome" → "firefox"
-Cleaner test files

#Will it affect the current code?:---

No negative effect, only positive:
-You won’t have to define Chrome setup inside each test file
-You just reuse the fixture driver (which you already do)
-Everything else stays exactly the same

#EXAMPLE FOR MORE CLARITY:---

current test_subscription.py:

    import pytest
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager
    from pages.home_page import HomePage
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

    @pytest.mark.order(3)
    def test_subscription(driver):
        home = HomePage(driver)
        home.subscribe("kabirr44@gmail.com")

Goal:

Instead of repeating the driver setup in every test file (like test_subscription.py, test_login.py, etc.),
you can move it to one place → driver_factory.py + conftest.py.
This makes your tests cleaner, reusable, and easy to switch browsers.

----Step 1: utils/driver_factory.py:

Create a function that builds a driver based on the browser you want.

    # utils/driver_factory.py
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium.webdriver.firefox.service import Service as FirefoxService
    from selenium.webdriver.chrome.options import Options as ChromeOptions
    from selenium.webdriver.firefox.options import Options as FirefoxOptions
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.firefox import GeckoDriverManager

    def get_driver(browser="chrome"):
        """Factory method to create a WebDriver instance."""
        if browser.lower() == "chrome":
            options = ChromeOptions()
            options.add_argument("--start-maximized")
            service = ChromeService(ChromeDriverManager().install())
            return webdriver.Chrome(service=service, options=options)

        elif browser.lower() == "firefox":
            options = FirefoxOptions()
            options.add_argument("--width=1920")
            options.add_argument("--height=1080")
            service = FirefoxService(GeckoDriverManager().install())
            return webdriver.Firefox(service=service, options=options)

        else:
            raise ValueError(f"❌ Unsupported browser: {browser}")

----Step 2: conftest.py:

Define the driver fixture that every test can use.

    # conftest.py
    import pytest
    from utils.driver_factory import get_driver
    from utils.config import BASE_URL

    @pytest.fixture
    def driver():
        # You can later change this to "firefox" or parametrize it
        driver = get_driver("chrome")
        driver.get(BASE_URL)
        yield driver
        driver.quit()


✅ This fixture will now automatically run before each test that uses driver.

----Step 3: Simplify your test files:

You no longer need to write WebDriver setup everywhere.

🟩 Old test_subscription.py:

    from selenium import webdriver
    ...
    driver = webdriver.Chrome()
    ...

🟦 New (clean) version:

    # tests/test_subscription.py
    import pytest
    from pages.home_page import HomePage

    @pytest.mark.order(3)
    def test_subscription(driver):
        home = HomePage(driver)
        home.subscribe("kabirr44@gmail.com")

✨ That’s it!
No setup, no teardown, no imports for Chrome — everything handled by conftest.py.

'''