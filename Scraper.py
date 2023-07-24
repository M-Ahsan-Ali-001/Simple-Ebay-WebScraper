from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
from chromedriver_py import binary_path

service_object = Service(binary_path)

products = []  # List to store name of the product
prices = []  # List to store price of the product
ratings = []  # List to store rating of the product

driver = webdriver.Chrome(service=service_object)
driver.get("https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=iphone+4&_sacat=0")

# Wait for the content to load if necessary
# Add necessary wait here

content = driver.page_source
#print(content)
soup = BeautifulSoup(content, 'html.parser')
print(soup.findAll('li', {'class': 's-item s-item__pl-on-bottom'}))
for a in soup.findAll('li', {'class': 's-item s-item__pl-on-bottom'}):
    name = a.find('span', {'role': 'heading'})
    price = a.find('span', {'class': 's-item__price'})
    rating = a.find('span', {'class': 's-item__seller-info'})

    if name and price and rating:  # Check if all elements are found before appending
        print("name:",name.text.strip())
        print("price:",price.text.strip())
        print("rating:",rating.text.strip())


        products.append(name.text.strip())

        prices.append(price.text.strip())
        ratings.append(rating.text.strip())
    else:
      print("foul")

df = pd.DataFrame({'Product Name': products, "price":prices,"rate":ratings})
df.to_csv('products.csv', index=False, encoding='utf-8')
