#!/usr/bin/env python3

import tkinter as tk
import customtkinter as ctk

class Candidate_page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #Create Info page Label
        info_page_label = tk.Label(self, text="Candidate's Information Page")
        info_page_label.pack(anchor="center", pady=5, padx=5)

        #Create Info Page Frame
        info_page_frame = ctk.CTkFrame(self)

        #Creating Candidate SERIAL and SEAT numbers Entry Frame
        candidate_serial_number_entry_frame = ctk.CTkFrame(info_page_frame)
        candidate_serial_number_entry_frame.pack(fill="x", padx=20, pady=(10,10))
        candidate_serial_number_entry_frame_label = ctk.CTkLabel(candidate_serial_number_entry_frame, text="Candidate's Serial Number: ")
        candidate_serial_number_entry_frame_label.pack(anchor="w", padx=10, pady=(5,10))

        #Create Candidate's Number Entry
        candidate_number_entry = ctk.CTkEntry(candidate_serial_number_entry_frame, placeholder_text="Your Candidate Number",
                                       width=300, border_color="#FF4500")
        candidate_number_entry.pack(expand=True, side="left", padx=(40,40), pady=(10,10))
        #Create Candidate's Seat Number Entry
        candidate_seat_number_entry = ctk.CTkEntry(candidate_serial_number_entry_frame, placeholder_text="Your Seat Number",
                                       width=300, border_color="#FF4500")
        candidate_seat_number_entry.pack(expand=True, side="left", padx=(40,40), pady=(10,10))

        #Creating Names Entry Frame
        names_entry_frame = ctk.CTkFrame(info_page_frame)
        names_entry_frame.pack(fill="x", padx=20, pady=(10,10))
        names_entry_label = ctk.CTkLabel(names_entry_frame, text="Full Name: ")
        names_entry_label.pack(anchor="w", padx=10, pady=(5,10))

        #Create First Name Entry
        first_name_entry = ctk.CTkEntry(names_entry_frame, placeholder_text="Fisrt Name",
                                       width=300, border_color="#FF4500")
        first_name_entry.pack(expand=True, side="left", padx=(40,40), pady=(10,10))
        #Create Middle Name Entry
        middle_name_entry = ctk.CTkEntry(names_entry_frame, placeholder_text="Middle Name",
                                       width=300, border_color="#FF4500")
        middle_name_entry.pack(expand=True, side="left", padx=(40,40), pady=(10,10))
        #Create Last Name Entry
        last_name_entry = ctk.CTkEntry(names_entry_frame, placeholder_text="Last Name",
                                       width=300, border_color="#FF4500")
        last_name_entry.pack(expand=True, side="left", padx=(40,40), pady=(10,10))

        #Creating Date of Identity Entry Frame
        identity_entry_frame = ctk.CTkFrame(info_page_frame)
        identity_entry_frame.pack(fill="x", padx=20, pady=(10,10))
        identity_entry_frame_label = ctk.CTkLabel(identity_entry_frame, text="Identity: ")
        identity_entry_frame_label.pack(anchor="w", padx=10, pady=(5,10), expand=True)

        #Creating Title Entry Frame
        title_entry_frame = ctk.CTkFrame(identity_entry_frame)
        title_entry_frame.pack(side="left", padx=20, pady=(10,10), expand=True, fill="x")
        title_entry_label = ctk.CTkLabel(title_entry_frame, text="Title")
        title_entry_label.pack(anchor="w", padx=10, pady=(5,10))

        honorific_titles_dropdown = ctk.CTkComboBox(title_entry_frame, values= ["Mr", "Mrs", "Miss", "Dr", 
                                                                 "Prof", "Rev", "Capt", "Lt", "Col", "Sir"],
            fg_color="purple", border_color="purple", button_hover_color="purple", bg_color="purple",
            button_color="#FF4500", dropdown_hover_color="purple", justify="center", dropdown_fg_color="#FF4500",)
        honorific_titles_dropdown.pack(side="left", pady=15, padx=40)

        #Creating Gender Entry Frame
        gender_entry_frame = ctk.CTkFrame(identity_entry_frame)
        gender_entry_frame.pack(side="left", padx=20, pady=(10,10), expand=True, fill="x")
        gender_entry_label = ctk.CTkLabel(gender_entry_frame, text="Gender")
        gender_entry_label.pack(anchor="w", padx=10, pady=(5,10))

        gender_entry_dropdown = ctk.CTkComboBox(gender_entry_frame, values= ["Male", "Female", "Prefer Not To Say"],
            fg_color="purple", border_color="purple", button_hover_color="purple", bg_color="purple",
            button_color="#FF4500", dropdown_hover_color="purple", justify="center", dropdown_fg_color="#FF4500",)
        gender_entry_dropdown.pack(side="left", pady=15, padx=40)

        #Creating Date of Birth Entry Frame
        dob_entry_frame = ctk.CTkFrame(info_page_frame)
        dob_entry_frame.pack(fill="x", padx=20, pady=(10,10))
        dob_entry_label = ctk.CTkLabel(dob_entry_frame, text="Date Of Birth: ")
        dob_entry_label.pack(anchor="w", padx=10, pady=(5,10), expand=True)

        #Creating Day of Birth Entry Frame
        day_entry_frame = ctk.CTkFrame(dob_entry_frame)
        day_entry_frame.pack(side="left", padx=20, pady=(10,10), expand=True, fill="x")
        day_entry_label = ctk.CTkLabel(day_entry_frame, text="Day")
        day_entry_label.pack(anchor="w", padx=10, pady=(5,10))

        day_dropdown = ctk.CTkComboBox(day_entry_frame, values= ["1", "2", "3", "4", "5", "6", "7", "8", "9",
                                                                      "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
                                                                      "20", "21", "22", "23", "24", "25", "26", "27", "28", "29",
                                                                      "30", "31"],
            fg_color="purple", border_color="purple", button_hover_color="purple", bg_color="purple",
            button_color="#FF4500", dropdown_hover_color="purple", justify="center", dropdown_fg_color="#FF4500",)
        day_dropdown.pack(side="left", pady=15, padx=40)

        #Creating Month of Birth Entry Frame
        day_entry_frame = ctk.CTkFrame(dob_entry_frame)
        day_entry_frame.pack(side="left", padx=20, pady=(10,10), expand=True, fill="x")
        day_entry_label = ctk.CTkLabel(day_entry_frame, text="Month")
        day_entry_label.pack(anchor="w", padx=10, pady=(5,10))

        day_dropdown = ctk.CTkComboBox(day_entry_frame, values= ["January","February", "March", "April", "May", "June", "July", 
                                                                "August", "September", "October","November", "December"],
            fg_color="purple", border_color="purple", button_hover_color="purple", bg_color="purple",
            button_color="#FF4500", dropdown_hover_color="purple", justify="center", dropdown_fg_color="#FF4500",)
        day_dropdown.pack(side="left", pady=15, padx=40)

         #Creating Year of Birth Entry Frame
        year_entry_frame = ctk.CTkFrame(dob_entry_frame)
        year_entry_frame.pack(side="left", padx=20, pady=(10,10), expand=True, fill="x")
        year_entry_label = ctk.CTkLabel(year_entry_frame, text="Year")
        year_entry_label.pack(anchor="w", padx=10, pady=(5,10))

        year_dropdown = ctk.CTkComboBox(year_entry_frame, values= ["1990", "1991","1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999", "2000",
                                                                    "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010",
                                                                    "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021",
                                                                    "2022", "2023", "2024", "2025"],
            fg_color="purple", border_color="purple", button_hover_color="purple", bg_color="purple",
            button_color="#FF4500", dropdown_hover_color="purple", justify="center", dropdown_fg_color="#FF4500")
        year_dropdown.pack(side="left", pady=15, padx=40)


        #Creating Country-State-Town_County Entry Frame
        country_entry_frame = ctk.CTkFrame(info_page_frame)
        country_entry_frame.pack(fill="x", padx=20, pady=(10,10))
        country_entry_label = ctk.CTkLabel(country_entry_frame, text="Country/State/Town-County:")
        country_entry_label.pack(anchor="w", padx=10, pady=(5,10))

        #Create country Name Entry
        country_name_entry = ctk.CTkEntry(country_entry_frame, placeholder_text="Country",
                                       width=300, border_color="#FF4500")
        country_name_entry.pack(expand=True, side="left", padx=(40,40), pady=(10,10))
        #Create Middle Name Entry
        state_name_entry = ctk.CTkEntry(country_entry_frame, placeholder_text="State",
                                       width=300, border_color="#FF4500")
        state_name_entry.pack(expand=True, side="left", padx=(40,40), pady=(10,10))
        #Create Last Name Entry
        town_county_name_entry = ctk.CTkEntry(country_entry_frame, placeholder_text="Town or County",
                                       width=300, border_color="#FF4500")
        town_county_name_entry.pack(expand=True, side="left", padx=(40,40), pady=(10,10))

        #Create Contacts Entry Frame
        contact_entry_frame = ctk.CTkFrame(info_page_frame)
        contact_entry_frame.pack(fill="x", padx=20, pady=(10,10))
        contact_entry_label = ctk.CTkLabel(contact_entry_frame, text="Contacts: ")
        contact_entry_label.pack(anchor="w", padx=10, pady=(5,10))

        #Create country Name Entry
        phone_number_entry = ctk.CTkEntry(contact_entry_frame, placeholder_text="Phone Number (+234 800 0000000)",
                                       width=300, border_color="#FF4500")
        phone_number_entry.pack(expand=True, side="left", padx=(40,40), pady=(10,10), fill="both")

        email_entry = ctk.CTkEntry(contact_entry_frame, placeholder_text="Email (example@gmail.com)",
                                       width=300, border_color="#FF4500")
        email_entry.pack(expand=True, side="left", padx=(40,40), pady=(10,10), fill="both")

        #Create Residential Address Entry Frame
        res_address_entry_frame = ctk.CTkFrame(info_page_frame)
        res_address_entry_frame.pack(fill="x", padx=20, pady=(10,10))
        res_address_label = ctk.CTkLabel(res_address_entry_frame, text="Residential Address:")
        res_address_label.pack(anchor="w", padx=10, pady=(5,10))

        #Create Address Entry
        address_entry = ctk.CTkEntry(res_address_entry_frame, placeholder_text="Residential Address",
                                       width=300, border_color="#FF4500")
        address_entry.pack(expand=True, side="left", padx=(40,40), pady=(10,10), fill="both")

        #Create Candidate submit frame
        candidate_submit_frame = ctk.CTkFrame(info_page_frame)
        candidate_submit_frame.pack(expand=True, fill="x", padx=50, pady=30)
        #Create Candidate submit button
        candidate_submits = ctk.CTkButton(candidate_submit_frame, text="SUBMIT", 
                                            font=ctk.CTkFont(family="Sarif bold", size=15), 
                                            width=10, height=10, hover=True,
                                            corner_radius=15, bg_color="transparent",
                                            hover_color="Purple", fg_color="#FF4500", border_color="#FF4500",
                                            )
        candidate_submits.pack(side="left", pady=(15, 15), fill="x", padx=20, expand=True)

        #Packing Info Page Frame
        info_page_frame.pack(expand=True, fill="both", padx=50,)


        #Create bottom frame for NEXT and BACK buttons
        self.bottom_frame = ctk.CTkFrame(self)

        # #Create the BACK button
        # self.bottom_frame_button = ctk.CTkButton(self.bottom_frame, text="BACK", 
        #                                     font=ctk.CTkFont(family="Sarif bold", size=12), 
        #                                     width=10, height=10, hover=True,
        #                                     corner_radius=15, bg_color="transparent",
        #                                      hover_color="Purple", fg_color="#FF4500", border_color="#FF4500",
        #                                      command = lambda: controller.display_page("Home_page")
        #                                     )
        # self.bottom_frame_button.pack(side="left", pady=(15, 15), ipadx=2, padx=20)
        
        #Create the NEXT Button
        bottom_frame_button = ctk.CTkButton(self.bottom_frame, text="NEXT", 
                                            font=ctk.CTkFont(family="Sarif bold", size=12), 
                                            width=10, height=10, hover=True,
                                            corner_radius=15, bg_color="transparent",
                                            hover_color="purple", fg_color="#FF4500", border_color="#FF4500",
                                            command = lambda: controller.display_page("Next_Of_Kin_page")
                                            )
        bottom_frame_button.pack(side="right", pady=(15, 15), ipadx=2, padx=20)
        self.bottom_frame.pack(anchor="s", fill="x", padx=50, pady=(5, 15))
