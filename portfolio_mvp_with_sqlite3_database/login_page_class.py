import customtkinter as ctk
from database_crosscheck_login_control_func import login_control

class Log_in_page(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        log_in_label = ctk.CTkLabel(self, text="Login Page")
        log_in_label.pack(anchor="center", pady=(5, 5), padx=5)

        log_in_frame = ctk.CTkFrame(self)
        

        #Defining the register button function
        def register():
            controller.display_page("Register_page")
        
        def login():
            username = username_entry.get()
            password = password_entry.get()
            if login_control(username, password):
                controller.display_page("Candidate_page")


        login_labelFrame = ctk.CTkFrame(log_in_frame)

        login_labelFrame2 = ctk.CTkFrame(login_labelFrame, fg_color="purple", border_width=24, border_color="#FF4500")
        login_labelFrame2.pack(anchor="center", fill="y", padx=100, pady=20, ipady=40, ipadx=20, expand=True)

        #Creating log_in widgets
        username_label = ctk.CTkButton(login_labelFrame2, text="Username", font=("Arial", 16), 
                                       bg_color="#FF4500", fg_color="#FF4500", hover=False)
        username_entry = ctk.CTkEntry(login_labelFrame2, font=("Arial", 16))
        password_entry = ctk.CTkEntry(login_labelFrame2, show="*", font=("Arial", 16))
        password_label = ctk.CTkButton(login_labelFrame2, text="Password", font=("Arial", 16), 
                                       bg_color="#FF4500", fg_color="#FF4500", hover=False)
        login_button = ctk.CTkButton(login_labelFrame2, text="Login", font=("Arial", 16), hover=True, 
                                     hover_color="black", fg_color="#FF4500", corner_radius=30,
                                     command=login)
        register_button = ctk.CTkButton(login_labelFrame2, text="Sign up", font=("Arial", 16), hover=True, 
                                     hover_color="black", fg_color="green", corner_radius=30,
                                     command=register)

        #Placing widgets on the screen
        username_label.pack(pady=20, padx=40)
        username_entry.pack(pady=2, padx=40)
        password_label.pack(pady=10, padx=40)
        password_entry.pack(pady=2, padx=40)
        login_button.pack(pady=20, padx=40)
        register_button.pack(pady=15, padx=40)

        button_frame = ctk.CTkFrame(login_labelFrame, fg_color="#FF4500")
        button_frame.pack(anchor="center", pady=5, padx=5, fill="both")
        
        register_frame = ctk.CTkFrame(button_frame, fg_color="purple")  
        register_frame.pack(anchor="center", pady=10, padx=10, fill="both")

        login_labelFrame.pack(anchor="center", fill="both", expand=True, pady=10, padx=10)


        log_in_frame.pack(anchor="center", pady=5, padx=5, fill="both", expand=True)