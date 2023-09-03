import json
from tkinter import messagebox


# Define a function to collect registration data
# Collect_reg_data(username=username_entry.get(), password=self.password_entry())

def collect_reg_data(username, password):
    # username = username_entry.get()
    # password = password_entry.get()

    username_password_dict = {username: password}

    try:
        with open("collected_username_password.json", "r") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []

    existing_data.append(username_password_dict)

    with open("collected_username_password.json", "w") as file:
        json.dump(existing_data, file, indent=4)

    messagebox.showinfo(title="Successful!", message="You have successfully registered")
