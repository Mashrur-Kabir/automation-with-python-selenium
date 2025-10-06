
# Automation Exercise — Selenium + pytest test suite

**Short:** A ready-to-run automated test suite for **https://www.automationexercise.com/** implemented with **Selenium + pytest** using a simple Page Object Model structure.  
This repository contains end-to-end UI tests, a small K6 load test, and supporting utilities.

---

## Goals / Intent of this repo
- Provide automated UI tests that simulate real user flows (register, login, search, cart + checkout, contact-us with file upload, subscription).
- Demonstrate simple Page Object Model (POM) usage to keep selectors/actions centralized in `pages/`.
- Provide a lightweight K6 script for a basic load check of the home page.

---

## Prerequisites
- **Python 3.10+** recommended (code was compiled into `.pyc` for CPython 3.12 in the archive; 3.10+ is a safe target).
- Google Chrome installed locally (tests use Chrome via `webdriver-manager`).
- `k6` (optional) if you want to run the load test (`K6/main/getAPI.js`).
- Git (for GitHub usage)

---

## Recommended virtual environment (venv) setup
**Create a venv** (run from the repo root where `automation-exercise/` lives):

**Unix / macOS**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (PowerShell)**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (CMD)**
```cmd
python -m venv venv
.\venv\Scripts\activate.bat
```

> After activation, your prompt should show `(venv)`.

**Install dependencies**
```bash
pip install --upgrade pip
pip install -r automation-exercise/requirements.txt
```

---

## How tests are executed
The tests use `webdriver-manager` to automatically download a matching `chromedriver` binary, and each test file currently creates its own `driver()` fixture that configures a `webdriver.Chrome` instance and opens `BASE_URL`.

**Run all tests**
```bash
pytest -s -v
```

**Run a single test file**
```bash
pytest tests/test_contact_us.py -v -s
```

**Useful options**
- `-k "expression"` — run tests that match an expression (by name).
- `-m "marker"` — run tests with a pytest marker (note: current tests use `pytest.mark.order`, not a named domain marker like `regression`).

---

## Notes about test design & improvements (recommended)
Centralizing Browser Driver Setup (For Future Reference)

Right now, the tests create the Chrome driver directly like this:
  service = Service(ChromeDriverManager().install())
  driver = webdriver.Chrome(service=service, options=chrome_options)

That means testers are stuck with Chrome.
If tomorrow they want to test on Firefox, they’ll have to modify every test file.

What driver_factory.py should do:

It’s a helper that creates a WebDriver instance based on input — Chrome, Firefox, or Edge.

💡 Benefits:

  -Centralized driver setup
  -Easy browser switch — just change "chrome" → "firefox"
  -Cleaner, shorter test files
  -Reusable across the entire test suite

📘 Example for Clarity
Look at the current test_subscription.py*

✅ Goal

Instead of repeating driver setup in every test file, move it to one place →
driver_factory.py + conftest.py

This makes your tests cleaner, reusable, and easier to maintain.

🧱 Step 1 — utils/driver_factory.py

Create a function that builds a driver for the desired browser.

# utils/driver_factory.py
```python
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
```

🧱 Step 2 — conftest.py

Define the reusable driver fixture for all tests.

# conftest.py
```python
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
```

This fixture will now automatically run before each test that uses driver.

🧱 Step 3 — Simplify your test files

You no longer need to write WebDriver setup everywhere.

🟩 Old test_subscription.py:

```python
  from selenium import webdriver
  ...
  driver = webdriver.Chrome()
  ...
```

🟦 New (clean) version:

```python
  # tests/test_subscription.py
  import pytest
  from pages.home_page import HomePage

  @pytest.mark.order(3)
  def test_subscription(driver):
      home = HomePage(driver)
      home.subscribe("kabirr44@gmail.com")
```

✨ That’s it — no setup, no teardown, no Chrome imports.
Everything is handled automatically by conftest.py.

---

## K6 load test
A small k6 script is at `K6/main/getAPI.js`. Basic usage:

**Local run**
```bash
k6 run K6/main/getAPI.js
```

**Cloud run**
```bash
k6 cloud K6/main/getAPI.js
```

The script currently does `http.get("https://www.automationexercise.com/")` with VUs configured — edit `getAPI.js` to target your environment. `K6/test_results1.pdf` is included as an example report.

## Quick maintenance checklist before publishing to GitHub
- [ ] Add `.gitignore` entries for `venv/`, `*.pyc`, `.pytest_cache/`.
- [ ] Add a proper `conftest.py` (suggested above).
- [ ] Pin `requirements.txt`.
- [ ] Add `.env.example` if environment variables will be used; DO NOT store secrets in repo.
- [ ] Add `pytest.ini` to register markers and configure test ordering/reporting.
- [ ] Add CONTRIBUTING.md and LICENSE as needed.

---

## Troubleshooting tips
- **Chromedriver/version mismatch**: `webdriver-manager` tries to auto-install a driver that fits your Chrome. If errors occur, ensure your local Chrome is up-to-date or force a matching chromedriver version.
- **File upload test failing**: `test_contact_us.py` expects `sample-for-contact-test/shirt-coral.jpg` at repo root — ensure the working directory is the project root when running tests.
- **Headless vs non-headless UI differences**: some elements behave differently in headless mode; test both when debugging.
- **Slow CI**: add `--maxfail=1 -q` in CI to fail fast, and parallelize with `pytest-xdist`.

---

## Final notes from my analysis
- The suite is functional and demonstrates core e2e flows and a basic k6 load test.  
- To make it production-ready for CI: **centralize fixtures**, **pin dependencies**, **add reporting**, and implement the `driver_factory` (or use `conftest.py`) to support multiple browsers and headless runs.

---

