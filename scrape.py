import requests
from bs4 import BeautifulSoup

url = 'YOUR WEBSITE URL HERE'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

print(soup.prettify())
