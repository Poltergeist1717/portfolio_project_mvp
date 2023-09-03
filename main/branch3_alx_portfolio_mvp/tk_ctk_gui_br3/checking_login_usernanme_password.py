from tkinter import messagebox
from dynmc_import_file_func import check_file_presence_rtn_file


def check_username_password(username, password):
    # username = username_entry.get()
    # password = password_entry.get()

    existing_usr_lst = check_file_presence_rtn_file()

    for item in existing_usr_lst:
        if username in item.keys() and password == item.get(username):
            messagebox.showinfo(title="Success!", message="Login successful!")
            return True  # Username and password match

    for item in existing_usr_lst:
        if password == item.get(username) and username not in item.keys():
            messagebox.showerror(title="Error!", message="Incorrect username!")
            return False
                
        if username in item.keys() and password != item.get(username):
            messagebox.showerror(title="Error!", message="Incorrect password!")
            return False 
                
        if username not in item.keys() and password != item.get(username):
            messagebox.showerror(title="Error!", message="User does not exist!")
            return False