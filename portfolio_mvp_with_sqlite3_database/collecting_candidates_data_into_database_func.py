import sqlite3
from tkinter import messagebox

connection = sqlite3.connect("cruxaming.db")
cursor = connection.cursor()

def candidates_database_data_entry_collector(candidate_serial_number_entry_value, interview_serial_number_entry_value, first_name, middle_name, last_name, full_name, address, phone_number, email, date_of_birth, country, state, town_county):
    sqlt_candidate_statement = """INSERT INTO candidates_table (
        candidate_serial_number,
        interview_serial_number,
        first_name,
        middle_name,
        last_name,
        full_name,
        address,
        phone_number,
        email,
        date_of_birth,
        country,
        state,
        town_county ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
    
    try:
        values = (candidate_serial_number_entry_value, interview_serial_number_entry_value, first_name, middle_name, last_name, full_name, address, phone_number, email, date_of_birth, country, state, town_county)  
        # Use placeholders (?) in the SQL statement and pass values as a tuple to cursor.execute
        cursor.execute(sqlt_candidate_statement, values)
        # To commit the changes to the database
        connection.commit()
        return True
    except Exception as e:
        messagebox.showerror(title="Error", message="An Error occurred: " + str(e))
        return False  # Return False to indicate an error
    finally:
        connection.close()