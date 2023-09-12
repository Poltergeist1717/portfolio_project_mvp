import json
from tkinter import messagebox

def interview_data_duplicate_control(candidate_serial_number_entry_value):
    try:
        with open("answers_for_interview.json", "r") as file:
            existing_list = json.load(file)
            for item in existing_list:
                for key in item.keys():
                    if candidate_serial_number_entry_value == key:
                        messagebox.showerror(title="Serial number already submitted!", message="You cannot submit twice. Thank You!")
                        return False
            return True  # This line executes only if no matching key is found
    except FileNotFoundError as e:
        messagebox.showinfo(title="Error!", message="Something went wrong: " + str(e))