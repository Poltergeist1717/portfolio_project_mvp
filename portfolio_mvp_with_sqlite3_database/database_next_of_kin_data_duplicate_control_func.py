import sqlite3
from tkinter import messagebox

def database_nxt_of_kin_data_duplicated_control(candidate_serial_number):
    connection = None
    cursor = None

    try:
        connection = sqlite3.connect("cruxaming.db")
        cursor = connection.cursor()
        value = candidate_serial_number
        cursor.execute("SELECT COUNT(*) FROM next_of_kins_table WHERE candidate_serial_number = ?", (value,))
        all_candidate_serial_number = cursor.fetchone()

        if all_candidate_serial_number[0] > 0:
            messagebox.showerror(title="Error!", message="Candidate Serial Number already exists.\nPlease rechek your details carefully!.")
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