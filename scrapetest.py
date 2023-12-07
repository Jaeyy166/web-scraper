from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html,'html.parser')
print(bs.h1)
