from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen('https://shopee.ph/search?category=11044709&keyword=japanese%20light%20novel&subcategory=11046717&thirdCategory=11046757')
soup = BeautifulSoup(html.read(), 'html.parser')

item_name = soup.body.find_all('div', {'class':'GDO2sl_6Q4fcE fJEFbf'})
for items in item_name:
    print(items.get_text())
