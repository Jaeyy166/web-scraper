from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen('https://books.toscrape.com/catalogue/category/books/classics_6/index.html')
soup = BeautifulSoup(html.read(), 'html.parser')

body = soup.find('body')
h3 = body.find_all('h3')
price = body.find_all('p',{'class':'price_color'})

products = []  # list of names and prices

for title in h3:
    name = title.get_text()
    products.append(name)
for prices in price:
    product_price = prices.get_text()
    products.append(product_price)


print(products)
