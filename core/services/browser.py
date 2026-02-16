from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class BrowserManager:
    def __init__(self, user_data_path, profile_name):
        self.user_data_path = user_data_path
        self.profile_name = profile_name
        self.driver = None

    def start(self):
        options = Options()
        if self.user_data_path:
            options.add_argument(f"--user-data-dir={self.user_data_path}")
        if self.profile_name:
            options.add_argument(f"--profile-directory={self.profile_name}")

        options.add_experimental_option("detach", True)

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        return self.driver

    def open_url(self, url):
        if self.driver:
            self.driver.get(url)

    def quit(self):
        if self.driver:
            self.driver.quit()
