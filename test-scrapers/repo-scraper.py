# scraping my github repos
# im going to try if i can get both name of repo and links
from bs4 import BeautifulSoup
import requests

source = 'http://#'
r = requests.get(source)
soup = BeautifulSoup(r.text, 'html.parser')

def get_links():


def repo_lists():


def main():
