import requests
from bs4 import BeautifulSoup

response = requests.get(
	url="https://fr.wikipedia.org/wiki/%C3%89tats_membres_de_l%27Union_europ%C3%A9enne",
)

soup = BeautifulSoup(response.content, 'html.parser')

title = soup.find(id="firstHeading")
print(title.string)

table = soup.find('table',{"class" : "wikitable"})

tbody = table.find('tbody')

print(tbody.find_all('tr'))


# h1 = soup.find("table", {"class" : "wikitable sortable jquery-tablesorter"})
# print(h1)

print(response.status_code)