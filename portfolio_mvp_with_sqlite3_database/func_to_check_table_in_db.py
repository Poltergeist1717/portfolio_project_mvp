import sqlite3
#import os

# Syntax to check if a file exists in a path
#os.path.exists("cruxaming.db")

connection = sqlite3.connect("cruxaming.db")
cursor = connection.cursor()

# To print a specific table
table = "registration_data_table"

cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name = '{table}';")
result = cursor.fetchone()

for table in result:
    print ("Single Table:", table)


#To print all tables
cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table';")
result = cursor.fetchall()
for table in result:
    print ("Table:", table[0])


connection.close()
