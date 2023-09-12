import sqlite3
from tkinter import messagebox

connection = sqlite3.connect("cruxaming.db")
cursor = connection.cursor()

def interview_database_data_entry_collector(interview_serial_number, candidate_serial_number, preferred_feature, position, about_you, chosen_language_value, experience_value, interview_score):
    sqlt_candidate_statement = """INSERT INTO interview_answers_table (
        interview_serial_number,
        candidate_serial_number,
        preferred_feature,
        position,
        about_you,
        chosen_language_value,
        experience_value,
        interview_score) VALUES (?, ?, ?, ?, ?, ?, ?, ?);"""
    
    try:
        values = (interview_serial_number, candidate_serial_number, preferred_feature, position, about_you, chosen_language_value, experience_value, interview_score)  
        # Use placeholders (?) in the SQL statement and pass values as a tuple to cursor.execute
        cursor.execute(sqlt_candidate_statement, values)
        # To commit the changes to the database
        connection.commit()
        
        if interview_score > 70:
            messagebox.showinfo(title="Congratulations!", message="You Passed. Your score is: " + str(interview_score))
        else:
            messagebox.showinfo(title="Sorry!", message="You failed. Your score is: " + str(interview_score))

        messagebox.showinfo(title="Thank you for coming!", message="Weather you passed or failed the test we wish you a sucessful career ahead.\nIf you passed, we would contact you soon. Congratulations once again!")

        return True
    except Exception as e:
        messagebox.showerror(title="Error", message="An Error occurred: " + str(e))
        return False  # Return False to indicate an error
    finally:
        connection.close()