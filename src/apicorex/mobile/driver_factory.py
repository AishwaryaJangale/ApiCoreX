from appium import webdriver
from appium.options.common import AppiumOptions

class MobileDriverFactory:
    """Factory builder for generating Appium Mobile Drivers."""
    
    @staticmethod
    def get_driver(appium_server_url, cap_dict):
        options = AppiumOptions()
        options.load_capabilities(cap_dict)
        return webdriver.Remote(command_executor=appium_server_url, options=options)
