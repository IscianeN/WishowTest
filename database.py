# import sqlite3
# from sqlite3 import Error
# import scraper

# def create_connection(db_file):
#     """ create a database connection to a SQLite database """
#     conn = None
#     try:
#         conn = sqlite3.connect(db_file)
#         print(sqlite3.version)
#     except Error as e:
#         print(e)
#     finally:
#         if conn:
#             conn.close()


# if __name__ == '__main__':
#     create_connection(r"C:\Users\iscia\Documents\AdaTechSchool\workflow\WishowTest\SQLite_python.db")


# connection = sqlite3.connect('SQLite_python.db')
# cursor_obj = connection.cursor()



# # cursor_obj.execute('''CREATE TABLE members_states
# #                (country, official_name, date_of_join, capital, aera)''')

# # print("Table is Ready")

# df.to_sql('members_states', connection, if_exists='replace', index = False)
 
# connection.commit()
# # Close the connection
# connection.close()