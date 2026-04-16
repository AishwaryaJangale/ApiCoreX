from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

class WebDriverFactory:
    """Factory builder for generating Selenium WebDrivers."""
    
    @staticmethod
    def get_driver(browser_name="chrome"):
        browser_name = browser_name.lower()
        if browser_name == "chrome":
            options = ChromeOptions()
            options.add_argument("--window-size=1920,1080")
            return webdriver.Chrome(options=options)
        elif browser_name == "firefox":
            options = FirefoxOptions()
            return webdriver.Firefox(options=options)
        else:
            raise ValueError(f"Browser '{browser_name}' is not supported.")
