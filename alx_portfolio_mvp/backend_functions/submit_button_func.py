#!/usr/bin/env python3

from tkinter import messagebox
from entry_data_checker_func import Check_user_input
from nxt_of_kin_data_collector_func import Next_Of_Kin_Details_Collector
from candidate_data_collector_func import Candidate_Details_Collector

class Submit_task(Check_user_input):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.controller = controller

    def collect_next_of_kin_details(self):
        self.f = Next_Of_Kin_Details_Collector()
        self.f.next_of_kin_names_collector()

    def collect_candidate_details(self):
        self.h = Candidate_Details_Collector()
        self.h.candidate_names_collector() 
    
    def ignitor(self):
        try:
            user_input_checker = Check_user_input(self, self.controller)  # Create an instance of Check_user_input
            if self.candidate_submits.get():
                if user_input_checker.checker():  # Call the checker method on the instance
                    self.collect_candidate_details()
            elif self.nok_submits.get():
                if user_input_checker.checker():  # Call the checker method on the instance
                    self.collect_next_of_kin_details()
        except Exception as e:
            messagebox.showerror(title="Error", message="An Error occurred: " + str(e))
            #return False
