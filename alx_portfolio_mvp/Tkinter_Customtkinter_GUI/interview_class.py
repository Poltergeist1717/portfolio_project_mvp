import tkinter as tk
import customtkinter as ctk

class Interview_page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller 

        #Create Interview page Label
        interview_page_label = tk.Label(self, text="Interview Page")
        interview_page_label.pack(anchor="center", pady=5, padx=5)

        #Create Interview page Frame
        interview_page_frame = ctk.CTkFrame(self)

         #Create the Language Frame
        language_frame = ctk.CTkFrame(interview_page_frame)
        language_frame.pack(padx=100, pady=(25, 7), fill="both")
        language_label = ctk.CTkLabel(
            language_frame, text="Programming Language", font=ctk.CTkFont(weight="bold"))
        language_label.pack(pady = 9)
        language_dropdown = ctk.CTkComboBox(
            language_frame, values= ["HTML", "CSS", "Java", "Javascript", "Python", "C", "C++", "PHP", "C#"],
            fg_color="purple", border_color="purple", button_hover_color="purple", bg_color="purple",
              button_color="#FF4500", dropdown_hover_color="purple", justify="center", 
              dropdown_fg_color="#FF4500",)
        language_dropdown.pack(pady = 5)

        #Create the Difficulty Frame
        difficulty_frame = ctk.CTkFrame(interview_page_frame)
        difficulty_frame.pack(padx=100, pady=5, fill="both")
        difficulty_label = ctk.CTkLabel(
            difficulty_frame, text="Project Difficulty", font=ctk.CTkFont(weight="bold")
        )
        difficulty_label.pack(pady = 8)
        difficulty_value = ctk.StringVar(value="Easy")
        radiobutton1 = ctk.CTkRadioButton(
            difficulty_frame, text="Easy", variable = difficulty_value, value="Easy", 
            fg_color="#FF4500", border_color="#FF4500", hover_color="purple", border_width_checked=9)
        radiobutton2 = ctk.CTkRadioButton(
            difficulty_frame, text="Medium", variable = difficulty_value, value="Medium", 
            fg_color="#FF4500", border_color="#FF4500", hover_color="purple", border_width_checked=9)
        radiobutton3 = ctk.CTkRadioButton(
            difficulty_frame, text="Hard", variable = difficulty_value, value="Hard", 
            fg_color="#FF4500", border_color="#FF4500", hover_color="purple", border_width_checked=9)

        #Packing difficulty radiobuttons
        radiobutton1.pack(side="left", padx=60, pady=10, expand = True)
        radiobutton2.pack(side="left", padx=60, pady=10, expand = True)
        radiobutton3.pack(side="left", padx=60, pady=10, expand = True)

        #Creating Experience Frame
        experience_frame = ctk.CTkFrame(interview_page_frame)
        experience_frame.pack(padx=100, pady=5, fill="both")
        experience_label = ctk.CTkLabel(
            experience_frame, text="Experience Level", font=ctk.CTkFont(weight="bold")
        )
        experience_label.pack(pady = 8)
        experience_value = ctk.StringVar(value="Easy")
        radiobutton1 = ctk.CTkRadioButton(
            experience_frame, text="Beginner", variable = experience_value, value="Beginner", 
            fg_color="#FF4500", border_color="#FF4500", hover_color="purple", border_width_checked=9)
        radiobutton2 = ctk.CTkRadioButton(
            experience_frame, text="Professional", variable = experience_value, value="Professional", 
            fg_color="#FF4500", border_color="#FF4500", hover_color="purple", border_width_checked=9)
        radiobutton3 = ctk.CTkRadioButton(
            experience_frame, text="Expert", variable = experience_value, value="Expert",
            fg_color="#FF4500", border_color="#FF4500", hover_color="purple", border_width_checked=9)

        #Packing experience radiobuttons
        radiobutton1.pack(side="left", padx=60, pady=10, expand = True)
        radiobutton2.pack(side = "left", padx=60, pady=10, expand = True)
        radiobutton3.pack(side="left", padx=60, pady=10, expand = True)

        #Create Feature Frame
        features_frame = ctk.CTkFrame(interview_page_frame)
        features_frame.pack(padx=100, pady=10, fill="both")
        features_label = ctk.CTkLabel(
            features_frame, text="Features", font=ctk.CTkFont(weight="bold")
        )
        features_label.pack()
        features_checkbox1 = ctk.CTkCheckBox(features_frame, text="Database", text_color="white",
                                             fg_color="#FF4500", border_color="#FF4500", 
                                             hover_color="purple")
        features_checkbox2 = ctk.CTkCheckBox(features_frame, text="API", text_color="white",
                                             fg_color="#FF4500", border_color="#FF4500", 
                                             hover_color="purple")

        features_checkbox1.pack(side ="left", padx= 80, pady= 10, expand = True)
        features_checkbox2.pack(side ="left", padx= 80, pady= 10, expand = True)

        #Create Position Entry Frame
        position_entry_frame = ctk.CTkFrame(interview_page_frame)
        position_entry_frame.pack(fill="x", padx=100, pady=(10,10))
        position_entry_label = ctk.CTkLabel(position_entry_frame, text="Position you applied for:")
        position_entry_label.pack(anchor="w", padx=10, pady=(5,10))

        #Create Address Entry
        address_entry = ctk.CTkEntry(position_entry_frame, placeholder_text="Product Manager",
                                       width=300, border_color="#FF4500")
        address_entry.pack(expand=True, side="left", padx=80, pady=(10,10), fill="both")

        #Create text box to display suggestions results
        result = ctk.CTkTextbox(interview_page_frame, font=ctk.CTkFont(size= 15))
        result.pack(padx=50, fill = "both", pady =(5, 15), expand=True)

         #Create button to generate suggestions
        button = ctk.CTkButton(interview_page_frame, text= "Generate Suggestions", 
                            font=ctk.CTkFont(size= 20, weight="bold"), hover_color="Purple", 
                            fg_color="#FF4500", border_color="#FF4500",)
        button.pack(padx=50, fill = "both", pady =(5, 10))


        #Pack Interview page Frame
        interview_page_frame.pack(expand=True, fill="both", padx=50)


         #Create bottom frame for BACK and NEXT buttons
        self.bottom_frame = ctk.CTkFrame(self)
        #Create the BACK button
        self.bottom_frame_button = ctk.CTkButton(self.bottom_frame, text="BACK", 
                                            font=ctk.CTkFont(family="Sarif bold", size=12), 
                                            width=10, height=10, hover=True,
                                            corner_radius=15, bg_color="transparent",
                                             hover_color="Purple", fg_color="#FF4500", border_color="#FF4500",
                                             command = lambda: controller.display_page("Next_Of_Kin_page")
                                            )
        self.bottom_frame_button.pack(side="left", pady=(15, 15), ipadx=2, padx=20)
        
        # #Create the NEXT Button
        # bottom_frame_button = ctk.CTkButton(self.bottom_frame, text="NEXT", 
        #                                     font=ctk.CTkFont(family="Sarif bold", size=12), 
        #                                     width=10, height=10, hover=True,
        #                                     corner_radius=15, bg_color="transparent",
        #                                      hover_color="purple", fg_color="#FF4500", border_color="#FF4500",
        #                                      command = lambda: controller.display_page("Interview_page")
        #                                     )
        # bottom_frame_button.pack(side="right", pady=(15, 15), ipadx=2, padx=20)
        
        #Pack Bottom Frame 
        self.bottom_frame.pack(anchor="s", fill="x", padx=50, pady=(5, 15))

