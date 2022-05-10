import requests
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

# def get_db():
#     conn = sqlite3.connect('SQLite_python.db')
#     return conn

connection = sqlite3.connect('SQLite_python.db')
cursor_obj = connection.cursor()
cursor_obj.execute("""CREATE TABLE IF NOT EXISTS members_states
                (country VARCHAR(255), official_name VARCHAR(255), date_of_join_eu VARCHAR(255), capital VARCHAR(255), area VARCHAR(255))""")


for country,official_name,capital,area in zip(countries,official_names,capitals,areas):
    query = '''INSERT INTO members_states (country, official_name, capital, area) VALUES ("{0}","{0}","{0}","{0}")'''.format(country,official_name,capital,area)
    cursor_obj.execute(query)
    print('data inserted')

connection.commit()
connection.close()
# def create_table():
#     table = ("""CREATE TABLE IF NOT EXISTS members_states
#                (country VARCHAR(255), official_name VARCHAR(255), date_of_join_eu VARCHAR(255), capital VARCHAR(255), area VARCHAR(255))""")
#     db=get_db()
#     cursor = db.cursor()
#     cursor.execute(table)

# create_table()



# def insert_data():
#     db=get_db()
#     cursor =db.cursor()
#     query = '''INSERT INTO members_states (country, official_name, capital, area) VALUES ("{0}","{0}","{0}","{0}")'''.format(country,official_name,capital,area)
#     for country,official_name,capital,area in zip(countries,official_names,capitals,areas):
#         cursor.execute(query)

# insert_data()

print("Table is Ready")



# for country,official_name,capital,area in zip(countries,official_names,capitals,areas):
#     query = '''INSERT INTO members_states (country, official_name, capital, area) VALUES ("{0}","{0}","{0}","{0}")'''.format(country,official_name,capital,area)
#     cursor_obj.execute(query)


