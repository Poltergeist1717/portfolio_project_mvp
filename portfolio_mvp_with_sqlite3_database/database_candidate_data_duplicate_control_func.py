import sqlite3
from tkinter import messagebox

def database_cddt_data_duplicated_control(candidate_serial_number_entry_value):
    connection = None
    cursor = None

    try:
        connection = sqlite3.connect("cruxaming.db")
        cursor = connection.cursor()
        value = candidate_serial_number_entry_value
        cursor.execute("SELECT * FROM candidates_table WHERE candidate_serial_number = ?", (value,))
        all_candidate_serial = cursor.fetchall()
        for candidate_serial in all_candidate_serial:
            if value == candidate_serial[0]:
                messagebox.showerror(title="Error!", message="Serial Number already exists.\nPlease rechek your details carefully!.")
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
