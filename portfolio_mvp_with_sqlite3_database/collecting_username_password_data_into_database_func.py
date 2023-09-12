import sqlite3
from tkinter import messagebox

connection = sqlite3.connect("cruxaming.db")
cursor = connection.cursor()

def username_password_database_data_entry_collector(username, password, confirm_password):
    sqlt_candidate_statement = """INSERT INTO registration_data_table (
        username,
        password,
        confirm_password) VALUES (?, ?, ?);"""
    
    try:
        values = (username, password, confirm_password)  
        # Use placeholders (?) in the SQL statement and pass values as a tuple to cursor.execute
        cursor.execute(sqlt_candidate_statement, values)
        # To commit the changes to the database
        
        connection.commit()

        messagebox.showinfo(title="Success!", message="You are now registered!")

        return True
    except Exception as e:
        messagebox.showerror(title="Error", message="An Error occurred: " + str(e))
        return False  # Return False to indicate an error
    finally:
        connection.close()