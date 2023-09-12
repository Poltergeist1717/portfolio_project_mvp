import sqlite3
from tkinter import messagebox

def login_control(username, password):
    connection = None
    cursor = None

    try:
        connection = sqlite3.connect("cruxaming.db")
        cursor = connection.cursor()
        
        # Use a single SQL query to check for both username and password
        cursor.execute("SELECT * FROM registration_data_table WHERE username = ? AND password = ?", (username, password))
        result = cursor.fetchone()  # Fetch a single matching row

        if result:
            return True # Both username and password are correct
        else:
            # Check if the username exists in the database
            cursor.execute("SELECT * FROM registration_data_table WHERE username = ?", (username,))
            username_result = cursor.fetchone()

            if username_result:
                messagebox.showerror(title="Password Error!", message="Incorrect Password or Empty!")
                return  False # Username is correct, but the password is incorrect
            else:
                messagebox.showerror(title="Username Error!", message="Incorrect Username or Username does not exist!")
                return False  # Username does not exist in the database
            
    except Exception as e:
        messagebox.showerror(title="Error in database operation", message="An error occurred: " + str(e))
        return "Error"
    finally:
        if cursor:
           cursor.close()
        if connection:
           connection.close()
