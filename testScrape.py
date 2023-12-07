from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://jaeyy166.github.io/blogsite-jaey/')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.h1)
