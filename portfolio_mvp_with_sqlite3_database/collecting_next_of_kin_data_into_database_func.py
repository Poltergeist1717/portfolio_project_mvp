import sqlite3
from tkinter import messagebox

connection = sqlite3.connect("cruxaming.db")
cursor = connection.cursor()

def next_of_kin_database_data_entry_collector(next_of_kin_serial_number, candidate_serial_number, first_name, middle_name, last_name, full_name, address, phone_number, email, date_of_birth, profession, position, company, industry, country, state, town_county):
    sqlt_candidate_statement = """INSERT INTO next_of_kins_table (
        next_of_kin_serial_number,
        candidate_serial_number,
        first_name,
        middle_name,
        last_name,
        full_name,
        address,
        phone_number,
        email,
        date_of_birth,
        profession,
        position,
        company,
        industry,
        country,
        state,
        town_county) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
    
    try:
        values = (next_of_kin_serial_number, candidate_serial_number, first_name, middle_name, last_name, full_name, address, phone_number, email, date_of_birth, profession, position, company, industry, country, state, town_county)  
        # Use placeholders (?) in the SQL statement and pass values as a tuple to cursor.execute
        cursor.execute(sqlt_candidate_statement, values)
        # To commit the changes to the database
        connection.commit()
        messagebox.showinfo(title="Serial Number", message="Please write down your next of kin's serial number: " + str(next_of_kin_serial_number))
        return True
    except Exception as e:
        messagebox.showerror(title="Error", message="An Error occurred: " + str(e))
        return False  # Return False to indicate an error
    finally:
        connection.close()