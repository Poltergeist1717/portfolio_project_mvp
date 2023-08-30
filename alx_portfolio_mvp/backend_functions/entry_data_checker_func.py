#!/usr/bin/env python3

import re
from tkinter import messagebox
from candidate_class import Candidate_page
from next_of_kin_class import Next_Of_Kin_page

class Check_user_input(Candidate_page, Next_Of_Kin_page):
    def __init__(self, parent, controller):
        super().__init__(self, parent)
        self.controller = controller 
    
    def checker(self):
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

        candidate_number = self.candidate_number_entry.get()
        candidate_seat_number = self.candidate_seat_number_entry.get()

        first_name = self.first_name_entry.get()
        middle_name = self.middle_name_entry.get()
        last_name = self.last_name_entry.get()

        country = self.country_name_entry.get()
        state = self.state_name_entry.get()
        town_county = self.town_county_name_entry.get()

        phone_number = self.phone_number_entry.get()
        email = self.email_entry.get()
        
        try:
            if not is_valid_candidate_number(candidate_number):
                messagebox.showerror(title="Error", message="Invalid input! \n Candidate Number should contain only alphanumeric \n starting with 3 uppercase alphabets and cannot be empty!")
                return False
            elif is_valid_candidate_seat_number(candidate_seat_number):
                messagebox.showerror(title="Error", message="Invalid input! \n Candidate Seat Number should contain only alphanumeric \n starting an uppercase alphabet and cannot be empty!")
                return False
            elif not is_valid_name(first_name) or (middle_name and not is_valid_name(middle_name)) or not is_valid_name(last_name):
                messagebox.showerror(title="Error", message="Invalid input! Names should contain only alphabets and cannot be empty!")
                return False
            elif not is_valid_location(country) or not is_valid_location(state) or not is_valid_location(town_county):
                messagebox.showerror(title="Error", message="Invalid Input! \n Country, State and/or Town Inputs should contain only alphabets and cannot be empty!")
                return False
            elif not is_valid_phone_number(phone_number):
                messagebox.showerror(title="Error", message="Invalid Phone Number format!")
                return False
            elif not is_valid_email(email):
                messagebox.showerror(title="Error", message="Invalid Email format!")
                return False
        except ValueError as e:
            messagebox.showerror(title="Error", message = "Invalid input! Please check your input fields." + str(e))
            return False

        return True
