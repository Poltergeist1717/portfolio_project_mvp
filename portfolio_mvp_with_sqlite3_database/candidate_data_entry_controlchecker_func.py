import re
from tkinter import messagebox


#Defining the entry checker function
#To check candidate inputs are following intended standard
def cddt_entry_data_cntrl_checker(interview_serial_number_entry_value, candidate_number, candidate_seat_number, first_name, middle_name, last_name, country, state, town_county, phone_number, email, address):
    def is_valid_name(name):
        return re.match(r'^[A-Za-z]+$', name) is not None

    def is_valid_location(location):
        return re.match(r'^[A-Za-z]+$', location) is not None

    def is_valid_phone_number(phone_number):
        return re.match(r'^\+\d{2,3}\s\d{9,15}$', phone_number) is not None

    def is_valid_email(email):
        return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$', email) is not None
    
    def is_valid_candidate_number(candidate_number):
        return re.match(r'^[A-Z0-9]+$', candidate_number) is not None
    
    def is_valid_candidate_seat_number(candidate_seat_number):
        return re.match(r'^[A-Z0-9]+$', candidate_seat_number) is not None

    def is_valid_interview_serial_number(interview_serial_number):
        return re.match(r'^[A-Z0-9]+$', interview_serial_number) is not None
        
    try:
        if not is_valid_interview_serial_number(interview_serial_number_entry_value):
            messagebox.showerror(title="Error", message="Invalid input! \Interview Serial Number should contain only uppercase alphanumeric and cannot be empty!")
            return False
            
        if not is_valid_candidate_number(candidate_number):
            messagebox.showerror(title="Error", message="Invalid input! \nCandidate Number should contain only uppercase alphanumeric and cannot be empty!")
            return False
                    
        if not is_valid_candidate_seat_number(candidate_seat_number):
            messagebox.showerror(title="Error", message="Invalid input! \nCandidate Seat Number should contain only uppercase alphanumeric and cannot be empty!")
            return False
                        
        if not is_valid_name(first_name) or (middle_name and not is_valid_name(middle_name)) or not is_valid_name(last_name):
            messagebox.showerror(title="Error", message="Invalid input! Names should contain only alphabets and cannot be empty!")
            return False
        
        if not (is_valid_location(country) or  is_valid_location(state) or is_valid_location(town_county)):
            messagebox.showerror(title="Error", message="Invalid Input! Country, State, and Town or County should contain only alphabets and cannot be empty!")
            return False
     
        if not is_valid_phone_number(phone_number):
            messagebox.showerror(title="Error", message="Invalid Phone Number format!")
            return False
                
        if not is_valid_email(email):
            messagebox.showerror(title="Error", message="Invalid Email format!")
            return False
        
        if len(address) <= 0:
            messagebox.showerror(title="Invalid Address Input!", message="Address is too short and cannot be empty!")
            return False
        
        if len(address) >= 151:
            messagebox.showerror(title="Invalid Address Input!", message="Address is too long!")
            return False
                
                
    except ValueError as e:
        messagebox.showerror(title="Error", message = "Invalid input! Please check your input fields." + str(e))
        return False

    return True