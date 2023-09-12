import customtkinter as ctk
from tkinter import messagebox
from collecting_interview_data_into_database_func import interview_database_data_entry_collector
from interview_score_calculator_for_database_func import database_score_update
from database_interview_data_duplicate_control_func import interview_data_duplicated_control
from database_interview_input_data_control_func import empty_or_not, pref_feature

class Interview_page(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller 

        #Create Interview page Label
        interview_page_label = ctk.CTkLabel(self, text="Interview Page")
        interview_page_label.pack(anchor="center", pady=5, padx=5)

        #Create Interview page Frame
        interview_page_frame = ctk.CTkScrollableFrame(self)

        #Defining the submit button

        def submit():
            chosen_language_value = chosen_language_var_value.get()
            experience_value = experience_var_value.get()

            candidate_serial_number = candidate_serial_number_entry.get()
            interview_serial_number = interview_Serial_number_entry.get()

            feature_value1 = features_checkbox1_var.get()
            feature_value2 = features_checkbox2_var.get()
            
            preferred_feature = pref_feature(feature_value1, feature_value2)

            position = position_entry.get()

            about_you = about_you_text_entry.get("0.0", "end")

            question1_value = question1_var_value.get()
            question2_value = question2_var_value.get()
            question3_value = question3_var_value.get()
            question4_value = question4_var_value.get()
            question5_value = question5_var_value.get()

            interview_score = database_score_update(question1_value, question2_value, question3_value, question4_value, question5_value)
            
            try:
                 if empty_or_not(interview_serial_number, candidate_serial_number):
                    if interview_data_duplicated_control(interview_serial_number, candidate_serial_number):
                        messagebox.showwarning(title="Warning!", message="Please chcek your answers properly.\nIf you submit now, it's final.")
                        control = messagebox.askyesno(title="Submit", message="Do you want to proceed?")
                        if control:
                            interview_database_data_entry_collector(interview_serial_number, candidate_serial_number, preferred_feature, position, about_you, chosen_language_value, experience_value, interview_score)

            except Exception as e:
                messagebox.showerror(title="Error", message="An Error occurred: " + str(e))

        
        #Creating CANDIDATE and INTERVIEW SERIAL NUMBERS Entry Frame
        candidate_serial_number_entry_frame = ctk.CTkFrame(interview_page_frame)
        candidate_serial_number_entry_frame.pack(fill="x", padx=20, pady=(10,10))
        candidate_serial_number_entry_frame_label = ctk.CTkLabel(candidate_serial_number_entry_frame, text="Serial Numbers (MUST MATCH WITH PREVIOUSLY PROVIDED NUMBER!): ",
                                                                 font=ctk.CTkFont(family="Arial", size=15, weight="bold"), text_color="red")
        candidate_serial_number_entry_frame_label.pack(anchor="w", padx=10, pady=(5,10))

        #Create Candidate's Number Entry
        candidate_serial_number_entry = ctk.CTkEntry(candidate_serial_number_entry_frame, placeholder_text="Your Candidate SERIAL NUMBER (MUST MATCH):",
                                       width=400, border_color="#FF4500")
        candidate_serial_number_entry.pack(expand=True, side="left", padx=(40,40), pady=(10,10))
        #Create Candidate's Seat Number Entry
        interview_Serial_number_entry = ctk.CTkEntry(candidate_serial_number_entry_frame, placeholder_text="Interview SERIAL NUMBER (MUST MATCH):",
                                       width=400, border_color="#FF4500")
        interview_Serial_number_entry.pack(expand=True, side="left", padx=(40,40), pady=(10,10))

        
        #Create the Language Frame
        language_frame = ctk.CTkFrame(interview_page_frame)
        language_frame.pack(padx=100, pady=(25, 7), fill="both")
        language_label = ctk.CTkLabel(
            language_frame, text=" What is your preferred Programming Language?", font=ctk.CTkFont(weight="bold"))
        language_label.pack(pady = 9)

        chosen_language_var_value = ctk.StringVar(value="HTML")
        chosen_language_dropdown = ctk.CTkComboBox(
            language_frame, values= ["HTML", "CSS", "Java", "Javascript", "Python", "C", "C++", "PHP", "C#"],
            fg_color="purple", border_color="purple", button_hover_color="purple", bg_color="purple",
              button_color="#FF4500", dropdown_hover_color="purple", justify="center", 
              dropdown_fg_color="#FF4500", variable=chosen_language_var_value)
        chosen_language_dropdown.pack(pady = 5)

        
        #Creating Question Frame

        question1_frame = ctk.CTkFrame(interview_page_frame)
        question1_frame.pack(padx=10,pady=10, expand=True, anchor="center", fill="both")

        #Create Question1 Frame
        difficulty_frame = ctk.CTkFrame(question1_frame)
        difficulty_frame.pack(padx=100, pady=5, fill="both")
        difficulty_label = ctk.CTkLabel(difficulty_frame, text="Are you more introverted or extroverted?", 
                                        font=ctk.CTkFont(weight="bold", family="Arial", size=20))
        difficulty_label.pack(pady = 8)

        question1_var_value = ctk.StringVar()
        radiobutton1 = ctk.CTkRadioButton(
            difficulty_frame, text="Introverted", variable = question1_var_value, value="Introverted", 
            fg_color="#FF4500", border_color="#FF4500", hover_color="purple", border_width_checked=9)
        radiobutton2 = ctk.CTkRadioButton(
            difficulty_frame, text="Extroverted", variable = question1_var_value, value="Extroverted", 
            fg_color="#FF4500", border_color="#FF4500", hover_color="purple", border_width_checked=9)
        radiobutton3 = ctk.CTkRadioButton(
            difficulty_frame, text="Ambivert", variable = question1_var_value, value="Ambivert", 
            fg_color="#FF4500", border_color="#FF4500", hover_color="purple", border_width_checked=9)
        radiobutton4 = ctk.CTkRadioButton(
            difficulty_frame, text="I prefer not to answer", variable = question1_var_value, value="I prefer not to answer", 
            fg_color="#FF4500", border_color="#FF4500", hover_color="purple", border_width_checked=9)

        #Packing Question1 radiobuttons
        radiobutton1.pack(side="left", padx=20, pady=20, expand = True)
        radiobutton2.pack(side="left", padx=20, pady=20, expand = True)
        radiobutton3.pack(side="left", padx=20, pady=20, expand = True)
        radiobutton4.pack(side="left", padx=20, pady=20, expand = True)

        #Create Question2 Frame
        question2_frame = ctk.CTkFrame(interview_page_frame)
        question2_frame.pack(padx=10,pady=10, expand=True, anchor="center", fill="both")

        difficulty_frame = ctk.CTkFrame(question2_frame)
        difficulty_frame.pack(padx=100, pady=5, fill="both")
        difficulty_label = ctk.CTkLabel(difficulty_frame, text="Do you prefer working independently or in a team?", 
                                        font=ctk.CTkFont(weight="bold", family="Arial", size=20))
        difficulty_label.pack(pady = 8)

        question2_var_value = ctk.StringVar()
        radiobutton1 = ctk.CTkRadioButton(
            difficulty_frame, text="Independently", variable = question2_var_value, value="Independently", 
            fg_color="#FF4500", border_color="#FF4500", hover_color="purple", border_width_checked=9)
        radiobutton2 = ctk.CTkRadioButton(
            difficulty_frame, text="In a team", variable = question2_var_value, value="In a team", 
            fg_color="#FF4500", border_color="#FF4500", hover_color="purple", border_width_checked=9)
        radiobutton3 = ctk.CTkRadioButton(
            difficulty_frame, text="Both, depending on the situation", variable = question2_var_value, value="Both, depending on the situation", 
            fg_color="#FF4500", border_color="#FF4500", hover_color="purple", border_width_checked=9)
        radiobutton4 = ctk.CTkRadioButton(
            difficulty_frame, text="I prefer not to answer", variable = question2_var_value, value="I prefer not to answer", 
            fg_color="#FF4500", border_color="#FF4500", hover_color="purple", border_width_checked=9)

        #Packing Question2 radiobuttons
        radiobutton1.pack(side="left", padx=20, pady=20, expand = True)
        radiobutton2.pack(side="left", padx=20, pady=20, expand = True)
        radiobutton3.pack(side="left", padx=20, pady=20, expand = True)
        radiobutton4.pack(side="left", padx=20, pady=20, expand = True)

        #Create Question3 Frame
        question3_frame = ctk.CTkFrame(interview_page_frame)
        question3_frame.pack(padx=10,pady=10, expand=True, anchor="center", fill="both")

        difficulty_frame = ctk.CTkFrame(question3_frame)
        difficulty_frame.pack(padx=100, pady=5, fill="both")
        difficulty_label = ctk.CTkLabel(difficulty_frame, text="How do you handle criticism?", 
                                        font=ctk.CTkFont(weight="bold", family="Arial", size=20))
        difficulty_label.pack(pady = 8)

        question3_var_value = ctk.StringVar()
        radiobutton1 = ctk.CTkRadioButton(
            difficulty_frame, text="Embrace criticism and use it for improvement", variable = question3_var_value, value="Embrace criticism and use it for improvement", 
            fg_color="#FF4500", border_color="#FF4500", hover_color="purple", border_width_checked=9)
        radiobutton2 = ctk.CTkRadioButton(
            difficulty_frame, text="Take criticism personally", variable = question3_var_value, value="Take criticism personally", 
            fg_color="#FF4500", border_color="#FF4500", hover_color="purple", border_width_checked=9)
        radiobutton3 = ctk.CTkRadioButton(
            difficulty_frame, text="Analyze criticism objectively", variable = question3_var_value, value="Analyze criticism objectively", 
            fg_color="#FF4500", border_color="#FF4500", hover_color="purple", border_width_checked=9)
        radiobutton4 = ctk.CTkRadioButton(
            difficulty_frame, text="I prefer not to answer", variable = question3_var_value, value="I prefer not to answer", 
            fg_color="#FF4500", border_color="#FF4500", hover_color="purple", border_width_checked=9)

        #Packing Question3 radiobuttons
        radiobutton1.pack(side="left", padx=20, pady=20, expand = True)
        radiobutton2.pack(side="left", padx=20, pady=20, expand = True)
        radiobutton3.pack(side="left", padx=20, pady=20, expand = True)
        radiobutton4.pack(side="left", padx=20, pady=20, expand = True)

        #Create Question4 Frame
        question4_frame = ctk.CTkFrame(interview_page_frame)
        question4_frame.pack(padx=10,pady=10, expand=True, anchor="center", fill="both")

        difficulty_frame = ctk.CTkFrame(question4_frame)
        difficulty_frame.pack(padx=100, pady=5, fill="both")
        difficulty_label = ctk.CTkLabel(difficulty_frame, text="How adaptable are you to change?", 
                                        font=ctk.CTkFont(weight="bold", family="Arial", size=20))
        difficulty_label.pack(pady = 8)

        question4_var_value = ctk.StringVar()
        radiobutton1 = ctk.CTkRadioButton(
            difficulty_frame, text="Very adaptable", variable = question4_var_value, value="Very adaptable", 
            fg_color="#FF4500", border_color="#FF4500", hover_color="purple", border_width_checked=9)
        radiobutton2 = ctk.CTkRadioButton(
            difficulty_frame, text="Somewhat adaptable", variable = question4_var_value, value="Somewhat adaptable", 
            fg_color="#FF4500", border_color="#FF4500", hover_color="purple", border_width_checked=9)
        radiobutton3 = ctk.CTkRadioButton(
            difficulty_frame, text="Resistant to change", variable = question4_var_value, value="Resistant to change", 
            fg_color="#FF4500", border_color="#FF4500", hover_color="purple", border_width_checked=9)
        radiobutton4 = ctk.CTkRadioButton(
            difficulty_frame, text="I prefer not to answer", variable = question4_var_value, value="I prefer not to answer", 
            fg_color="#FF4500", border_color="#FF4500", hover_color="purple", border_width_checked=9)

        #Packing Question4 radiobuttons
        radiobutton1.pack(side="left", padx=20, pady=20, expand = True)
        radiobutton2.pack(side="left", padx=20, pady=20, expand = True)
        radiobutton3.pack(side="left", padx=20, pady=20, expand = True)
        radiobutton4.pack(side="left", padx=20, pady=20, expand = True)

        #Create Question5 Frame
        question5_frame = ctk.CTkFrame(interview_page_frame)
        question5_frame.pack(padx=10,pady=10, expand=True, anchor="center", fill="both")

        difficulty_frame = ctk.CTkFrame(question5_frame)
        difficulty_frame.pack(padx=100, pady=5, fill="both")
        difficulty_label = ctk.CTkLabel(
            difficulty_frame, text="How do you manage stress in high-pressure situations?", font=ctk.CTkFont(weight="bold", family="Arial", size=20))
        difficulty_label.pack(pady = 8)

        question5_var_value = ctk.StringVar()
        radiobutton1 = ctk.CTkRadioButton(
            difficulty_frame, text="Stay calm and focused", variable = question5_var_value, value="Stay calm and focused", 
            fg_color="#FF4500", border_color="#FF4500", hover_color="purple", border_width_checked=9)
        radiobutton2 = ctk.CTkRadioButton(
            difficulty_frame, text="Get anxious and lose focus", variable = question5_var_value, value="Get anxious and lose focus", 
            fg_color="#FF4500", border_color="#FF4500", hover_color="purple", border_width_checked=9)
        radiobutton3 = ctk.CTkRadioButton(
            difficulty_frame, text="Seek support from others", variable = question5_var_value, value="Seek support from others", 
            fg_color="#FF4500", border_color="#FF4500", hover_color="purple", border_width_checked=9)
        radiobutton4 = ctk.CTkRadioButton(
            difficulty_frame, text="I prefer not to answer", variable = question5_var_value, value="I prefer not to answer", 
            fg_color="#FF4500", border_color="#FF4500", hover_color="purple", border_width_checked=9)

        #Packing Question5 radiobuttons
        radiobutton1.pack(side="left", padx=20, pady=20, expand = True)
        radiobutton2.pack(side="left", padx=20, pady=20, expand = True)
        radiobutton3.pack(side="left", padx=20, pady=20, expand = True)
        radiobutton4.pack(side="left", padx=20, pady=20, expand = True)



        #Creating Experience Frame
        experience_wrap_frame = ctk.CTkFrame(interview_page_frame)
        experience_wrap_frame.pack(padx=10,pady=10, expand=True, anchor="center", fill="both")

        experience_frame = ctk.CTkFrame(experience_wrap_frame)
        experience_frame.pack(padx=100, pady=5, fill="both")
        experience_label = ctk.CTkLabel(
            experience_frame, text="What is your Experience Level?", font=ctk.CTkFont(weight="bold"))
        experience_label.pack(pady = 8)

        experience_var_value = ctk.StringVar()
        radiobutton1 = ctk.CTkRadioButton(
            experience_frame, text="Beginner", variable = experience_var_value, value="Beginner", 
            fg_color="#FF4500", border_color="#FF4500", hover_color="purple", border_width_checked=9)
        radiobutton2 = ctk.CTkRadioButton(
            experience_frame, text="Professional", variable = experience_var_value, value="Professional", 
            fg_color="#FF4500", border_color="#FF4500", hover_color="purple", border_width_checked=9)
        radiobutton3 = ctk.CTkRadioButton(
            experience_frame, text="Expert", variable = experience_var_value, value="Expert",
            fg_color="#FF4500", border_color="#FF4500", hover_color="purple", border_width_checked=9)

        #Packing experience radiobuttons
        radiobutton1.pack(side="left", padx=60, pady=10, expand = True)
        radiobutton2.pack(side = "left", padx=60, pady=10, expand = True)
        radiobutton3.pack(side="left", padx=60, pady=10, expand = True)


        #Create Feature Frame
        feature_wrap_frame = ctk.CTkFrame(interview_page_frame)
        feature_wrap_frame.pack(padx=10,pady=10, expand=True, anchor="center", fill="both")

        features_frame = ctk.CTkFrame(feature_wrap_frame)
        features_frame.pack(padx=100, pady=10, fill="both")
        features_label = ctk.CTkLabel(
            features_frame, text="Which of the two options do you work best with? (Choose both if you can do both)", font=ctk.CTkFont(weight="bold")
        )
        features_label.pack()

        features_checkbox1_var = ctk.StringVar()
        features_checkbox1 = ctk.CTkCheckBox(features_frame, text="Database", text_color="white",
                                             fg_color="#FF4500", border_color="#FF4500", 
                                             hover_color="purple", variable=features_checkbox1_var, 
                                             onvalue="on", offvalue="off")
        
        features_checkbox2_var = ctk.StringVar()
        features_checkbox2 = ctk.CTkCheckBox(features_frame, text="API", text_color="white",
                                             fg_color="#FF4500", border_color="#FF4500", 
                                             hover_color="purple", variable=features_checkbox2_var, 
                                             onvalue="on", offvalue="off")

        features_checkbox1.pack(side ="left", padx= 80, pady= 10, expand = True)
        features_checkbox2.pack(side ="left", padx= 80, pady= 10, expand = True)

        #Create Position Entry Frame
        position_entry_frame = ctk.CTkFrame(interview_page_frame)
        position_entry_frame.pack(fill="x", padx=100, pady=(10,10))
        position_entry_label = ctk.CTkLabel(position_entry_frame, text="Position you are applying for:")
        position_entry_label.pack(anchor="w", padx=10, pady=(5,10))

        #Create Address Entry
        position_entry = ctk.CTkEntry(position_entry_frame, placeholder_text="Product Manager",
                                       width=300, border_color="#FF4500")
        position_entry.pack(expand=True, side="left", padx=80, pady=(10,10), fill="both")


        #Create About you Entry Frame
        about_you_entry_frame = ctk.CTkFrame(interview_page_frame)
        about_you_entry_frame.pack(fill="x", padx=100, pady=(10,10))
        about_you_entry_frame_label = ctk.CTkLabel(about_you_entry_frame, text="Tell us about yourself:")
        about_you_entry_frame_label.pack(anchor="w", padx=10, pady=(5,10))

        #Create text box for about you
        about_you_text_entry = ctk.CTkTextbox(about_you_entry_frame, font=ctk.CTkFont(size= 15))
        about_you_text_entry.pack(padx=50, fill = "both", pady =(5, 15), expand=True)

        #Create button to generate suggestions
        button = ctk.CTkButton(interview_page_frame, text= "Submit", 
                            font=ctk.CTkFont(size= 15, weight="bold"), hover_color="Purple", 
                            fg_color="#FF4500", border_color="#FF4500", command=submit)
        button.pack(padx=50, anchor="center", pady =(5, 10))


        #Create bottom frame for Log out and NEXT buttons
        self.bottom_frame = ctk.CTkFrame(interview_page_frame)
        #Create the BACK button
        self.bottom_frame_button = ctk.CTkButton(self.bottom_frame, text="BACK", 
                                            font=ctk.CTkFont(family="Sarif bold", size=12), 
                                            width=10, height=10, hover=True,
                                            corner_radius=15, bg_color="transparent",
                                             hover_color="Purple", fg_color="#FF4500", border_color="#FF4500",
                                             command = lambda: controller.display_page("Next_Of_Kin_page")
                                            )
        self.bottom_frame_button.pack(side="left", pady=(15, 15), ipadx=2, padx=20)
        
        #Create the Log out Button
        bottom_frame_button = ctk.CTkButton(self.bottom_frame, text="Log Out", 
                                            font=ctk.CTkFont(family="Sarif bold", size=12), 
                                            width=10, height=10, hover=True,
                                            corner_radius=15, bg_color="transparent",
                                             hover_color="purple", fg_color="red", border_color="#FF4500",
                                             command = lambda: controller.display_page("Front_page")
                                            )
        bottom_frame_button.pack(side="right", pady=(15, 15), ipadx=2, padx=20)
        
        #Pack Bottom Frame 
        self.bottom_frame.pack(anchor="s", fill="x", padx=50, pady=(5, 15))

        #Pack Interview page Frame
        interview_page_frame.pack(expand=True, fill="both", padx=50)


