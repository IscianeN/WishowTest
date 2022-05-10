import requests
from bs4 import BeautifulSoup
import pandas as pd 


response = requests.get(
	url="https://fr.wikipedia.org/wiki/%C3%89tats_membres_de_l%27Union_europ%C3%A9enne",
)

soup = BeautifulSoup(response.content, 'html.parser')

# title = soup.find(id="firstHeading")
# print(title.string)

# table = soup.find('table',{"class" : "wikitable"})

# tbody = table.find('tbody').encode("utf-8")
# print(tbody)

# print('Classes of each table:')
# for table in soup.find_all('table'):
# 	print(table.get('class')) 

tables = soup.find_all('table')
table = soup.find('table', class_='wikitable sortable')

# Defining of the dataframe
df = pd.DataFrame(columns=['Pays', 'Nom officiel'])
# , 'Adhésion', 'Capitale', 'Superficie'

# Collecting Ddata
for row in table.tbody.find_all('tr'):    
    # Find all data for each column
    columns = row.find_all('td')
    
    if(columns != []):
        country = columns[0].text.strip()
        official_name = columns[1].text.strip()
        # date_of_join_eu = columns[2].span.contents[0].strip('&0.')
        # capital = columns[3].span.contents[0].strip('&0.')
        # aera = columns[4].span.contents[0].strip('&0.')
       

        df = df.pandas.concat({'Pays': country,  'Nom officiel': official_name},ignore_index=True)
		# 'Adhésion': date_of_join_eu, 'Capitale': capital, 'Superficie': aera},


df.head()
# print(tbody.find_all('tr'))




print(response.status_code)