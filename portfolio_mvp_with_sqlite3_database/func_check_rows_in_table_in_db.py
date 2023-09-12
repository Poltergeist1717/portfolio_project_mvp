import sqlite3
from tkinter import messagebox

connection = sqlite3.connect("cruxaming.db")
cursor = connection.cursor()

try:

    # To check all the data inside the particular table
    table_name = "interview_answers_table"
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        print("\n")

    columns_names = [description[0] for description in cursor.description]
    print(columns_names)

    # # +++++ BE CAREFUL: COMMAND TO DELETE A TABLE+++++
    # table_name = ""
    # cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

    # cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    # tables_name = cursor.fetchall()
    # for table in tables_name:
    #     print("=======================================")
    #     print(table[0], "\n")
    #     cursor.execute(f"PRAGMA table_info({table[0]});")
    #     columns = cursor.fetchall()
    #     for column in columns:
    #         print(column[1])  # Print the column name

    #     #print("\n")
    #     print("====================================")


except sqlite3.Error as e:
    messagebox.showerror(title="Error!", message="There was an error:" + str(e))
finally:
    cursor.close()
    connection.close()