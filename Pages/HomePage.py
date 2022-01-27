import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.amazon_searchbox_ID = "twotabsearchtextbox"
        self.searchbox = "empty"

    def find_searchbox(self):
        try:
            self.driver.find_element(By.ID, self.amazon_searchbox_ID)
            self.searchbox = self.driver.find_element(By.ID, "twotabsearchtextbox")
            print("Search will perform on Amazon")
        except NoSuchElementException:
            print("Searchbox not found!")

    def use_searchbox(self, itemname):
        time.sleep(1)
        self.searchbox.send_keys(itemname)
        time.sleep(2)
        self.searchbox.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)
