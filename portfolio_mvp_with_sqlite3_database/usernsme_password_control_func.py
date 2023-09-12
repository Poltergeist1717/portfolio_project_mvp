import re
from tkinter import messagebox

#Defining the username and password control function
def username_password_control(username, password, confirm_password):
            # username = username_entry.get()
            # password = password_entry.get()
            # confirm_password = confirm_password_entry.get()

            def is_valid_username(username):
                return re.match(r'^[A-Za-z]+\d+$', username) is not None
            
            def is_valid_password(password):
                return re.match(r'^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+[\]{};:"\\|,.<>?/]).+$', password) is not None
            try:
                if not is_valid_username(username):
                    messagebox.showerror(title="Error!", message="Invalid data input! \nUsername should be alphanumeric!")
                    return False
                
                if not is_valid_password(password) and not is_valid_password(confirm_password):
                    messagebox.showerror(title="Error!", message="Your password should contain: \n1. At least one uppercase letter. \n2. At least one digit. \n3. At least one special character")
                    return False
            except ValueError as e:
                messagebox.showerror(title="Error", message = "Invalid input! Please check your input fields." + str(e))
                return False
            return True