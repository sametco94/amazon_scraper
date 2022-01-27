import urllib.request

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xlsxwriter
import time


class SearchResults:
    def __init__(self, driver):
        self.driver = driver

    # PRODUCTS' URLs
    def amazon_products_links(self):
        wait = WebDriverWait(self.driver, 20)
        results = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@class, 'a-link-normal s-no-outline')]")))
        self.links = []
        for link in results:
            self.links.append(link.get_attribute("href"))

    # PRODUCTS' PRICES
    def amazon_products_prices(self):
        wait = WebDriverWait(self.driver, 20)
        results = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@class, 'a-price-whole')]")))
        self.prices = []
        for price in results:
            self.prices.append(price.text)

    # IMAGE LINKS
    def amazon_products_images(self):
        wait = WebDriverWait(self.driver, 20)
        results = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "s-image")))
        self.images = []
        for image in results:
            self.images.append(image.get_attribute("src"))

    def create_excel(self):
        print(self.links)
        print(self.prices)
        print(self.images)
        table_titles = [['Links'], ['Prices'], ['Images']]
        new_list = [self.links, self.prices, self.images]
        filename = time.strftime("%Y%m%d-%H%M%S")
        sheetname = "SHEET-1"
        with xlsxwriter.Workbook("C:/Users/esame/PycharmProjects/e-commerce_scraper/excelfiles/"+filename+".xlsx") as workbook:
            worksheet = workbook.add_worksheet(sheetname)
            for row_num, data in enumerate(table_titles):
                worksheet.write_row(row_num, 0, data)
            for row_num, data in enumerate(new_list):
                worksheet.write_row(row_num, 1, data)

    def download_images(self):
        urls = self.images
        for img in urls:
            image_name = img.split("/")[-1]
            urllib.request.urlretrieve(url=img, filename="C:/Users/esame/PycharmProjects/e-commerce_scraper/images/"+image_name)

