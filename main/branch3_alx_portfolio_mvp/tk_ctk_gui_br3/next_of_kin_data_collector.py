import json
from tkinter import messagebox
import random


#Defining next of kin data collecting function
def next_of_kin_data_collector():

    #Create a date of birth tuple
    date_of_birth = (day, month, year)

    #create NoK serial number string by concatenating 
    #candidate year of birth, firstname, and a random 5 digits
            
    random_number = str(random.randint(10000, 99999))
    nok_serial_number = str(year + first_name + random_number)

    # Initiate a dictionary to collect next of kins' unique detail
    # Unique details: dictionary of nok_serial_number as key and nok_data_collector_dict as value 
    nok_unique_details_dict = {}

    # Initiate an empty dictionary to collect next of kin data
    nok_data_collector_dict = {}

    # populating the nok_data_collector_dict
    nok_data_collector_dict["First Name"] = first_name
    nok_data_collector_dict["Middle Name"] = middle_name
    nok_data_collector_dict["Last Name"] = last_name
    nok_data_collector_dict["Address"] = address
    nok_data_collector_dict["Phone Number"] = phone_number
    nok_data_collector_dict["Email"] = email
    nok_data_collector_dict["Date of Birth"] = date_of_birth
    nok_data_collector_dict["Profession"] = profession
    nok_data_collector_dict["Position"] = position
    nok_data_collector_dict["Company"] = company
    nok_data_collector_dict["Industry"] = industry

    # Populating the nok_unique_details_dict
    nok_unique_details_dict[nok_serial_number] = nok_data_collector_dict

    #Update the existing data and save it to the file
    try:
        with open("next_of_kin_collected_data.json", "r") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []

    existing_data.append(nok_unique_details_dict)

    with open("next_of_kin_collected_data.json", "w") as file:
        json.dump(existing_data, file, indent=4)

    messagebox.showinfo(title="Serial Number", message="Please write down your next of kin's serial number: " + str(nok_serial_number))

    #return nok_unique_details_dict