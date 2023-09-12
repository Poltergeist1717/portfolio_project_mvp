import sqlite3
from tkinter import messagebox

def username_duplicated_control(username):
    connection = None
    cursor = None

    try:
        connection = sqlite3.connect("cruxaming.db")
        cursor = connection.cursor()
        value = username
        cursor.execute("SELECT * FROM registration_data_table WHERE username = ?", (value,))
        all_usernames = cursor.fetchall()
        for username in all_usernames:
            if value == username[0]:
                messagebox.showerror(title="Error!", message="Username already exists.\nPlease try another.")
                return False
        return True
    except Exception as e:
        messagebox.showerror(title="Error in database operation", message="An error occurred: " + str(e))
        return False
    finally:
        if cursor:
           cursor.close()
        if connection:
           connection.close()