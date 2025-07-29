#Find and Find All
from bs4 import BeautifulSoup
import requests

url = 'https://www.scrapethissite.com/pages/forms/'
page = requests.get(url)

#soup = BeautifulSoup(page.text,'html') #it show warning
soup = BeautifulSoup(page.text, 'html.parser') #here it states the parser used is html
#A parser is a tool that reads and analyzes HTML or XML documents, breaking them down into a structured format so that BeautifulSoup can extract information from them

#print(soup)
print(soup.find('div')) #finds the first response in the html ie. first div class
print(soup.find_all('div',class_ = 'col-md-12')) #finds all response in the html ie. all div class

print(soup.find_all('p', class_ = 'lead'))
print(soup.find('p',class_='lead').text)
print(soup.find('p',class_='lead').text.strip())

print(soup.find_all('th'))

print(soup.find('th').text)

print(soup.find('th').text.strip())
