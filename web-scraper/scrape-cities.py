
import csv
import re
import requests
from bs4 import BeautifulSoup as bs4

# Get page content
page = requests.get('https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population')

# Create a BeautifulSoup object
soup = bs4(page.text, 'html.parser')

# Parse soup
raw_cities = []
for row in soup.find_all('table')[4].find('tbody').find_all('tr'):
    if row.find('td'):
        raw_cities.append(row.find_all('td')[1].text.rstrip())

# Clean data
cities = []
for city in raw_cities:
    cities.append(re.sub(r'[\(\[].*?[\)\]]', '', city))

# Create csv
with open('cities.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(cities)
