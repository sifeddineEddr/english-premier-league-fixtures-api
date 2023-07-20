import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.premierleague.com/news/3537201")

soup = BeautifulSoup(response.text, 'html.parser')

print(soup)
