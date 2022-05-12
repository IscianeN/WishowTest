import requests
import sqlite3
from sqlite3 import Error
from scraper import *
from connection_to_db import *
import json


conn = sqlite3.connect('SQlite_python.db')
cursor_obj  = conn.cursor()

def list_to_string(mylist):
    mystring =' '.join(map(str,mylist))
    return mystring

def get_details(country):
    conn = sqlite3.connect('SQlite_python.db')
    cursor_obj  = conn.cursor()
    query = """SELECT * FROM members_states WHERE country = "{0}";""".format(country)
    cursor_obj.execute(query)
    result=cursor_obj.fetchall()
    country_details=' '.join([str(country) for country in result])
    return country_details
    
def get_details_country():
        for country in countries:
            details = get_details(country)
        return details
    

def get_countries():
    conn = sqlite3.connect('SQLite_python.db')
    cursor_obj = conn.cursor()
    query = "SELECT country FROM members_states"
    cursor_obj.execute(query) 
    result = cursor_obj.fetchall()
    return result

all_countries=get_countries()
countries_str = list_to_string(all_countries)


conn.commit()
conn.close()











