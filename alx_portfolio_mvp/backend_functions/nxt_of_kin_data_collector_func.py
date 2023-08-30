#!/usr/bin/env python3

import json
from candidate_data_control_function import Candidate_Details_Collector
from next_of_kin_class import Next_Of_Kin_page

class Next_Of_Kin_Details_Collector(Candidate_Details_Collector, Next_Of_Kin_page):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.controller = controller 

    def next_of_kin_names_collector(self):
        
        self.candidate_names_collector()

        profession = self.profession_name_entry.get()
        position = self.position_entry.get()
        company = self.company_entry.get()
        industry = self.industry_entry.get()

        candidate_serial_number = str(self.candidate_number_entry.get() + self.candidate_seat_number_entry.get())

        nok_candidates_details_dict = {}

        nof_full_name_collector_dict = {}


        nof_full_name_collector_dict["Profession"] = profession
        nof_full_name_collector_dict["Position"] = position
        nof_full_name_collector_dict["Company"] = company
        nof_full_name_collector_dict["Industry"] = industry

        nok_candidates_details_dict[candidate_serial_number] = nof_full_name_collector_dict

        #Update the existing data and save it to the file
        try:
            with open("nof_collected_full_name.json", "r") as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            existing_data = []

            existing_data.append(nok_candidates_details_dict)

        with open("collected_full_name.json", "w") as file:
            json.dump(existing_data, file, indent=4)

        return nok_candidates_details_dict
