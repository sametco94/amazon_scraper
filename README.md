"scraper.py" opens "amazon.com.tr" via 'chromedriver' and searches for the product, which is written/input by the user on the console, here. After the search is completed; only for the first result page: 

It gathers all the links(URLs) for the products' pages, the products' prices, and the links for the products' first displayed images in an excel file named with the current date and time, which is inside the file named 'excelfiles'.
Then lastly, downloads/saves all the first displayed images into the file named 'images'. 

The first example has been run and all the scraped data can be found here.


packs: 
  selenium
  urllib
  xlsxwriter
