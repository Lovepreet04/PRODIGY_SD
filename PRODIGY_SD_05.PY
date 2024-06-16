import csv
import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/static"
# or use input command for user input
# url = input("ENTER THE URL : ")
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

products = soup.find_all("div", class_="thumbnail")
product_data = []
for product in products:
    name = product.find("a", class_="title").text.strip()
    price = float(product.find("h4", class_="price").text.strip()[1:])
    rating = len(product.find_all("span", class_="glyphicon-star"))
    product_data.append([name, price, rating])

with open("products.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "Price", "Rating"])
    for row in product_data:
        writer.writerow(row)