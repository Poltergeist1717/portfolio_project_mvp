import re
from tkinter import messagebox


#Defining the entry checker function
#To check candidate inputs are following intended standard
def cddt_entry_data_cntrl_checker(candidate_number, candidate_seat_number, first_name, middle_name, last_name, country, state, town_county, phone_number, email):
    def is_valid_name(name):
        return re.match(r'^[A-Za-z]+$', name) is not None

    def is_valid_location(location):
        return re.match(r'^[A-Za-z\s]+$', location) is not None

    def is_valid_phone_number(phone_number):
        return re.match(r'^\+\d{2,3}\s\d{9,15}$', phone_number) is not None

    def is_valid_email(email):
        return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$', email) is not None
        
    def is_valid_candidate_number(candidate_number):
        return re.match(r'^[A-Z]{3}\d+$', candidate_number) is not None
        
    def is_valid_candidate_seat_number(candidate_seat_number):
        return re.match(r'^[A-Z]\d+$', candidate_seat_number) is not None
        
    try:
        if not is_valid_candidate_number(candidate_number):
            messagebox.showerror(title="Error", message="Invalid input! \n Candidate Number should contain only alphanumeric \n starting with 3 uppercase alphabets and cannot be empty!")
            return False
                
        if is_valid_candidate_seat_number(candidate_seat_number):
            messagebox.showerror(title="Error", message="Invalid input! \n Candidate Seat Number should contain only alphanumeric \n starting an uppercase alphabet and cannot be empty!")
            return False
                
        if not is_valid_name(first_name) or (middle_name and not is_valid_name(middle_name)) or not is_valid_name(last_name):
            messagebox.showerror(title="Error", message="Invalid input! Names should contain only alphabets and cannot be empty!")
            return False
                
        if not is_valid_location(country) or not is_valid_location(state) or not is_valid_location(town_county):
            messagebox.showerror(title="Error", message="Invalid Input! \n Country, State and/or Town Inputs should contain only alphabets and cannot be empty!")
            return False
                
        if not is_valid_phone_number(phone_number):
            messagebox.showerror(title="Error", message="Invalid Phone Number format!")
            return False
                
        if not is_valid_email(email):
            messagebox.showerror(title="Error", message="Invalid Email format!")
            return False
                
    except ValueError as e:
        messagebox.showerror(title="Error", message = "Invalid input! Please check your input fields." + str(e))
        return False

    return True