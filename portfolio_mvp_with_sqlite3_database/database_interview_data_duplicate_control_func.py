import sqlite3
from tkinter import messagebox

def interview_data_duplicated_control(interview_serial_number, candidate_serial_number):
    connection = None
    cursor = None

    try:
        connection = sqlite3.connect("cruxaming.db")
        cursor = connection.cursor()
        value = interview_serial_number
        value2 = candidate_serial_number

        cursor.execute("SELECT COUNT(*) FROM interview_answers_table WHERE interview_serial_number = ? AND candidate_serial_number = ?", (value, value2))
        both_serial_numbers = cursor.fetchone()

        if both_serial_numbers[0] > 0:
            messagebox.showerror(title="Error!", message="Both Serial Numbers already exist.\nYou cannot submit twice\nPlease chek your details carefully!.")
            return False
        else:
            cursor.execute("SELECT COUNT(*) FROM interview_answers_table WHERE interview_serial_number = ?", (value,))
            result1 = cursor.fetchone()
            if result1[0] > 0:
                messagebox.showerror(title="Interview Serial Number Error!", message="Interviwe Serial Number already exist.\nPlease chek your details carefully!")
                return False
            
            cursor.execute("SELECT COUNT(*) FROM interview_answers_table WHERE candidate_serial_number = ?", (value2,))
            result2 = cursor.fetchone()

            if result2[0] > 0:
                messagebox.showerror(title="Candidate Serial Number Error!", message="Candidate Serial Number already exist.\nPlease chek your details carefully!")
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