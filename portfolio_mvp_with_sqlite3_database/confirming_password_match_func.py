from tkinter import messagebox

def confirming_password(password, confirm_password):
    try:
        if password == confirm_password:
            return True
        else:
            messagebox.showerror(title="Error!", message="Password does not match confirm password!")
            return False
    except ValueError:
            return False