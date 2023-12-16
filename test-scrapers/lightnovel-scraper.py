# Book Walker Shoujo Manga web scraping practice
# with tags: Slice of life, Romance and Shoujo
from bs4 import BeautifulSoup
import requests

source = requests.get(
        "https://global.bookwalker.jp/categories/2/?qtag=6%2C1056%2C1066"
    )
try:
    soup = BeautifulSoup(source.text, "html.parser")

    mangas = soup.find_all('li', class_="o-tile")

    for manga in mangas:
        title = manga.find("h2", class_="a-tile-ttl")
        price = manga.find("div", class_="a-tile-price")

        cleanData = title.get_text() + price.get_text()
        print(cleanData)    
        # AINT NO FUCKING WAY THIS WORKED 

except Exception as e:
    print(e)
