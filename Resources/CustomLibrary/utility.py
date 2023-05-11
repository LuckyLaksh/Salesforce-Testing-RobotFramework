from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class utility:
    def get_driver_path_with_browser(self,browser_name):
        if browser_name.lower() == 'chrome':
            driver_path = ChromeDriverManager().install()
        elif browser_name.lower() == 'firefox':
            driver_path = GeckoDriverManager().install()
        return driver_path