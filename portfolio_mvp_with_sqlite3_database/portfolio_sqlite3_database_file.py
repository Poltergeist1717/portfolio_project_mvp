import sqlite3
from tkinter import messagebox
#import uuid

try:
    connection = sqlite3.connect("cruxaming.db")
    cursor = connection.cursor()

    # Creating CANDIDATES table in the database.
    sql_statement_for_candidates_table = """
    CREATE TABLE IF NOT EXISTS candidates_table (
        candidate_serial_number VARCHAR(50) PRIMARY KEY,
        interview_serial_number VARCHAR(50),
        first_name TEXT,
        middle_name TEXT,
        last_name TEXT,
        full_name TEXT,
        address TEXT,
        phone_number TEXT,
        email TEXT,
        date_of_birth DATE,
        country TEXT,
        state TEXT,
        town_county TEXT
    );"""

    cursor.execute(sql_statement_for_candidates_table)  # Executing the command and committing it to the database

    # Creating NEXT OF KINS table in the database
    sql_statement_for_next_of_kin_table = """
    CREATE TABLE IF NOT EXISTS next_of_kins_table (
        next_of_kin_serial_number VARCHAR(50) PRIMARY KEY,
        candidate_serial_number VARCHAR(50),
        first_name TEXT,
        middle_name TEXT,
        last_name TEXT,
        full_name TEXT,
        address TEXT,
        phone_number TEXT,
        email TEXT,
        date_of_birth DATE,
        profession TEXT,
        position TEXT,
        company TEXT,
        industry TEXT,
        country,
        state,
        town_county,
        FOREIGN KEY (candidate_serial_number) REFERENCES candidates(candidate_serial_number)
    );"""

    cursor.execute(sql_statement_for_next_of_kin_table)  # Executing the command and committing it to the database

    # Creating INTERVIEW ANSWERS table in the database.
    sql_statement_for_interview_answers_table = """
    CREATE TABLE IF NOT EXISTS interview_answers_table (
        interview_serial_number VARCHAR(50) PRIMARY KEY,
        candidate_serial_number VARCHAR(50),
        preferred_feature TEXT,
        position TEXT,
        about_you TEXT,
        chosen_language_value TEXT,
        experience_value TEXT,
        interview_score INTEGER,
        FOREIGN KEY (candidate_serial_number) REFERENCES candidates(candidate_serial_number)
    );"""

    cursor.execute(sql_statement_for_interview_answers_table)  # Executing the command and committing it to the database

    # Creating REGISTRATION DATA TABLE in the database
    sql_statement_for_registration_data_table = """
    CREATE TABLE IF NOT EXISTS registration_data_table (
        username VARCHAR(30) PRIMARY KEY,
        password VARCHAR,
        confirm_password VARCHAR);"""

    cursor.execute(sql_statement_for_registration_data_table)  # Executing the command and committing it to the database
    connection.commit()

except sqlite3.Error as e:
    messagebox.showerror(title="Error!", message="There was an error:" + str(e))

finally:
    connection.close()
