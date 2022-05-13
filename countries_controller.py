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


def get_details(a_country):
        print(a_country)
        conn=sqlite3.connect('SQlite_python.db')
        cursor_obj =conn.cursor()
        cursor_obj.execute("SELECT * FROM members_states WHERE country = ?", [a_country])
        details = []
        result = cursor_obj.fetchall()
        print('result:',result)
        details.append(result)
        print('details :',details)
        details_str=' '.join([str(a_country) for a_country in details])
        
        return details_str


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











