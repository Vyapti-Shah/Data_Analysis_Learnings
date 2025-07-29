#BeautifulSoup and Requests 
from bs4 import BeautifulSoup
import requests

url = 'https://www.scrapethissite.com/pages/forms/'
print(requests.get(url))

page = requests.get(url)

soup = BeautifulSoup(page.text,'html')

print(soup)

print()

print(soup.prettify())