from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://jaeyy166.github.io/odin-recipes/')
bs = BeautifulSoup(html.read(), 'html.parser')

recipeTitle = bs.find_all('ul')
for title in recipeTitle:
    print(title.get_text())
