
import sqlite3
from sqlite3 import Error
from scraper import *



def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection(r"C:\Users\iscia\Documents\AdaTechSchool\workflow\WishowTest\SQLite_python.db")


conn = sqlite3.connect('SQLite_python.db')
cursor_obj = conn.cursor()

#create table 
cursor_obj.execute("""CREATE TABLE IF NOT EXISTS members_states
                (country VARCHAR(255), official_name VARCHAR(255), date_of_join_eu VARCHAR(255), capital VARCHAR(255), area VARCHAR(255))""")

#insert data into table
for country,official_name,capital,area in zip(countries,official_names,capitals,areas):
    query = '''INSERT INTO members_states (country, official_name, date_of_join_eu, capital, area) VALUES ("{0}","{1}","NULL","{3}","{4}")'''.format(country,official_name,date_of_join_eu,capital,area)
    cursor_obj.execute(query)

conn.commit()

print("Table is Ready")


