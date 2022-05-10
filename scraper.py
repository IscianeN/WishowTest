
import requests
from bs4 import BeautifulSoup
import pandas as pd  
from unidecode import unidecode
import sqlite3
from sqlite3 import Error



response = requests.get(
	url="https://fr.wikipedia.org/wiki/%C3%89tats_membres_de_l%27Union_europ%C3%A9enne",
)
url="https://fr.wikipedia.org/wiki/%C3%89tats_membres_de_l%27Union_europ%C3%A9enne"
soup = BeautifulSoup(response.text, 'html.parser')


# table = soup.find('table',{"class" : "wikitable"})
tables = soup.find_all('table')
table = soup.find('table', class_='wikitable sortable')
tbody = table.find('tbody')


# Defining of the dataframe
df = pd.DataFrame(columns=['Pays', 'Nom_officiel', 'Adhésion','Capitale','Superficie'])

# Collecting Ddata first step
for row in table.tbody.find_all('tr'):    
    # Find all data for each column
    columns = row.find_all('td')
    
  


    if(columns != []):
        country = columns[0].text.strip()
        official_name = columns[1].text.strip()
        date_of_join_eu = columns[2].span.content
        capital = columns[3].text.strip()
        area = columns[4].text.strip()
       
    
        df = df.append({'Pays': country,  'Nom_officiel': official_name,'Adhésion':date_of_join_eu,'Capitale':capital,'Superficie':area},ignore_index=True)

countries = df['Pays']
official_names=df['Nom_officiel']
dates_of_join_eu=df['Adhésion']
capitals = df['Capitale']
areas = df['Superficie']









   











