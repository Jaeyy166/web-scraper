# scraping my github repos
# im going to try if i can get both name of repo and links
from bs4 import BeautifulSoup
import requests

source = requests.get('https://github.com/Jaeyy166?tab=repositories')

try:
    soup = BeautifulSoup(source.text, 'html.parser')
    link = soup.find_all('h3', 'a')
    



except Exception as e:
    print(e)
