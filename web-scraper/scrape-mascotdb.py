import csv
import requests
from bs4 import BeautifulSoup as bs4

# Get page content
page = requests.get('https://www.mascotdb.com/browse')

# Create a BeautifulSoup object
soup = bs4(page.text, 'html.parser')

# Parse soup
links = soup.find_all(class_='field-content')
mascots = []
for link in links:
    mascots.append(link.text)

# Create csv
with open('mascots.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(mascots)