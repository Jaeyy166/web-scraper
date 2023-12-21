from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

html = urlopen("https://books.toscrape.com/catalogue/category/books/classics_6/index.html")
soup = BeautifulSoup(html.read(), "html.parser")
article = soup.find_all('li', {'class':"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
    
books_list = []

for items in article:
    img = items.find('img')
    title = img.attrs['alt']
    price = items.find('p', {'class':'price_color'}).text
    book = title , price
    books_list.append(book)

print(books_list)

# this is fine for now, im going to attempt exporting successfully the data to csv next time
