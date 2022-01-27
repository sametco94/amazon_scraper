import time
from src.Pages.HomePage import HomePage
from src.Pages.SearchResultsPage import SearchResults
from selenium.webdriver.common.by import By
from selenium import webdriver
from threading import Thread


class Scraper:

    def startdriver(self):
        self.driver = webdriver.Chrome("C:/Users/esame/Downloads/chromedriver.exe")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

    def do_searches(self):
        driver = self.driver
        driver.get("https://www.amazon.com.tr")
        driver.find_element(By.ID, "sp-cc-accept").click()
        time.sleep(1)

        homepage = HomePage(driver)
        searches = SearchResults(driver)

        homepage.find_searchbox()
        time.sleep(2)
        search_item = input("Please enter the detailed item name: ")
        homepage.use_searchbox(search_item)
        time.sleep(1)
        searches.amazon_products_links()
        searches.amazon_products_prices()
        searches.amazon_products_images()
        searches.create_excel()
        searches.download_images()

    def closedriver(self):
        self.driver.close()
        self.driver.quit()

    def runall(self):
        if __name__ == '__main__':
            Thread(target=self.startdriver()).start()
            Thread(target=self.do_searches()).start()
            Thread(target=self.closedriver()).start()


run = Scraper()
run.runall()
