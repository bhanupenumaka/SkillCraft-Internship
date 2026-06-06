import requests
from bs4 import BeautifulSoup
import csv

url = 'https://example.com/products' # Ee site nundi data scrap cheyali
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Data ni extract cheyali
products = []
for item in soup.find_all('div', class_='product'):
    name = item.find('h2').text
    price = item.find('span', class_='price').text
    products.append([name, price])

# CSV file lo save cheyali
with open('products.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Price'])
    writer.writerows(products)

print("Data scraped and saved to products.csv")
