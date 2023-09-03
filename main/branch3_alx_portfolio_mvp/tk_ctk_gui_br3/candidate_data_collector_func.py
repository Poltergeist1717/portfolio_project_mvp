import json
from tkinter import messagebox

#Defining the candidates data collecting function
#To collect candidates inputs
def candidate_data_collector(first_name, middle_name, last_name, address, phone_number, email, day, month, year, candidate_number, candidate_seat_number):
    
    # Create a date of birth tuple
    date_of_birth = (day, month, year)

    # create a candidate serial number string by concatenating 
    candidate_serial_number = str(candidate_number + candidate_seat_number)

    #Initialize an dictionary to collect details of candidate 
    #using the candidate serial number as a key for easy access
    candidates_details_dict = {}

    #Initialize an empty dictionary to collect all the candidate's details
    full_name_collector_dict = {}

    full_name_collector_dict["First Name"] = first_name
    full_name_collector_dict["Middle Name"] = middle_name
    full_name_collector_dict["Last Name"] = last_name
    full_name_collector_dict["Address"] = address
    full_name_collector_dict["Phone Number"] = phone_number
    full_name_collector_dict["Email"] = email
    full_name_collector_dict["Date of Birth"] = date_of_birth

    candidates_details_dict[candidate_serial_number] = full_name_collector_dict


    try:
        with open("collected_candidate_data.json", "r") as file:
                existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []

    existing_data.append(candidates_details_dict)

    with open("collected_candidate_data.json", "w") as file:
        json.dump(existing_data, file, indent=4)

    messagebox.showinfo(title="Serial Number", message="Please write down your serial number: " + str(candidate_serial_number))