import re
from tkinter import messagebox

#Defining the entry checker function 
def NoK_data_entry_cntrlcheck(first_name, middle_name, last_name, country, state, town_county, address, phone_number, email, profession, position, company, industry):
    def is_valid_name(name):
        return re.match(r'^[A-Za-z]{2,20}$', name) is not None

    def is_valid_profession(profession):
        return re.match(r'^[A-Za-z\s]+$', profession) is not None
            
    def is_valid_location(location):
        return re.match(r'^[A-Za-z\s]+$', location) is not None

    def is_valid_phone_number(phone_number):
        return re.match(r'^\+\d{2,3}\s\d{9,15}$', phone_number) is not None

    def is_valid_email(email):
        return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$', email) is not None    
        
        
    try:
        if not is_valid_name(first_name) or (middle_name and not is_valid_name(middle_name)) or not is_valid_name(last_name):
            messagebox.showerror(title="Error", message="Invalid input! Names should contain only alphabets and cannot be empty!")
            return False
                
        if not is_valid_profession(profession) or not is_valid_profession(position) or not is_valid_profession(company) or not is_valid_profession(industry):
            messagebox.showerror(title="Error", message="Invalid Input! \n Profession, Position, Company or Industry Inputs should contain only alphabets and cannot be empty!")
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