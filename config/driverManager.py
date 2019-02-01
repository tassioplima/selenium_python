from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

url = "www.google.com.br"
driver = webdriver.Chrome("./env/chromedriver")
class DriverManager:
    def driver(self):
        driver.maximize_window()
        return driver

    def tearDown(self):
        driver.close

    def open (self):
        pass