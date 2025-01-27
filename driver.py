# driver.py
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class Driver:
    def __init__(self):
        self.driver = None

    def get_driver(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        return self.driver

    def quit(self):
        """Закрывает браузер"""
        if self.driver:
            self.driver.quit()
