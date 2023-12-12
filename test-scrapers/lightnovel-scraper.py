# Book Walker Shoujo Light Novels web scraping practice
# with tags: Slice of life, Romance and Shoujo
from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("https://global.bookwalker.jp/categories/2/?qtag=6%2C1056%2C1066")
soup = BeautifulSoup(html.read(), 'html.parser')

h2 = soup.find_all('h2', {'class':'a-tile-ttl'})
price = soup.find_all('div',{'class':'a-tile-price'})

product_list = []

for title in h2:
    name = title.get_text().strip().replace('\n', '')
    product_list.append(name)

print(product_list)
