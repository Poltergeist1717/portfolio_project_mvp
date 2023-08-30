import json
from candidate_class import Candidate_page
#from datetime import datetime

class Candidate_Details_Collector(Candidate_page):
        def __init__(self, parent, controller):
            super().__init__(parent, controller)
            self.controller = controller 

        def candidate_names_collector(self):

            first_name = self.first_name_entry.get()
            middle_name = self.middle_name_entry.get()
            last_name = self.last_name_entry.get()
            address = self.address_entry.get()
            phone_number = self.phone_number_entry.get()
            email = self.email_entry.get()

            #Create a date of birth tuple
            day = self.day_dropdown.get()
            month = self.month_dropdown.get()
            year = self.year_dropdown.get()
            date_of_birth = (day, month, year)

            #create a candidate serial number string by concatenating 
            # #candidate number and candidate seat number
            candidate_number = self.candidate_number_entry.get()
            candidate_seat_number = self.candidate_seat_number_entry.get()
            candidate_serial_number = str(candidate_number + candidate_seat_number)

            #Initialize an dictionary to collect details of candidate 
            #using the candidate serial number as a key for easy access
            candidates_details_dict = {}

            #Initialize an empty dictionary to collect all the candidate's details
            full_name_collector_dict = {}

            # full_name_collector_dict["ID"] = datetime.now().strftime("%Y%m%d%H%M%S%f")  # Unique timestamp-based ID
            full_name_collector_dict["First Name"] = first_name
            full_name_collector_dict["Middle Name"] = middle_name
            full_name_collector_dict["Last Name"] = last_name
            full_name_collector_dict["Address"] = address
            full_name_collector_dict["Phone Number"] = phone_number
            full_name_collector_dict["Email"] = email
            full_name_collector_dict["Date of Birth"] = date_of_birth

            candidates_details_dict[candidate_serial_number] = full_name_collector_dict


            try:
                with open("collected_full_name.json", "r") as file:
                    existing_data = json.load(file)
            except FileNotFoundError:
                existing_data = []

            existing_data.append(candidates_details_dict)

            with open("collected_full_name.json", "w") as file:
                json.dump(existing_data, file, indent=4)

            return candidates_details_dict
