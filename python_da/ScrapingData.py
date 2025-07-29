#Scraping Data from a Real Website 
from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)
soup = BeautifulSoup(page.text,'html.parser')
print(soup)
print(soup.find_all('table'))
print(soup.find_all('table')[1]) #accesses the item at 1st index in the list
soup.find_all('table',class_='wikitable sortable')[1]

#<table class="wikitable sortable jquery-tablesorter">
#<caption>

table = soup.find_all('table')[1]
print(table)

world_titles = table.find_all('th')
print(world_titles)

world_table_titles = [title.text.strip() for title in world_titles] #.strip removes the \n 
print(world_table_titles)

import pandas as pd
df = pd.DataFrame(columns=world_table_titles)
print(df)

column_data = table.find_all('tr')
for row in column_data[1:]: #eliminated the empty list
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    print(individual_row_data)
    length = len(df)
    df.loc[length] = individual_row_data
print(df)
df.to_csv(r'C:\Users\vyapti shah\OneDrive\Desktop\python_da\op_webscarping_csvconverted\Companies.csv',index=False)