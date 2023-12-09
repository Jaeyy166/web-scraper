from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv 

html = urlopen('https://shopee.ph/search?category=11044709&keyword=japanese%20light%20novel&subcategory=11046717&thirdCategory=11046757')
soup = BeautifulSoup(html, 'html.parser')

item_wrapper = soup.find_all('div',{'class':'item-card-list'})
item_List = item_wrapper.find_all('')

print(item_title)
