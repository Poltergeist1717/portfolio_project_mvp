import tkinter as tk
import customtkinter as ctk
from checking_login_usernanme_password import check_username_password

class Log_in_page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        log_in_label = tk.Label(self, text="Login Page")
        log_in_label.pack(anchor="center", pady=(5, 5), padx=5)

        log_in_frame = ctk.CTkFrame(self)
        

        #Defining the register button function
        def register():
            controller.display_page("Register_page")
        
        def login():
            username = username_entry.get()
            password = password_entry.get()
            if check_username_password(username, password):
                controller.display_page("Candidate_page")


        login_labelFrame = ctk.CTkFrame(log_in_frame)

        login_labelFrame2 = tk.LabelFrame(login_labelFrame, font=("Arial", 15), text="Log In", 
                                          cursor="hand2", relief="solid", background="purple")
        login_labelFrame2.pack(anchor="center", ipadx=160, ipady=160, fill="both", padx=80, pady=50)

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

        #Placing widgets on the screen
        username_label.place(y=50, x=385)
        username_entry.place(x=530, y=50)
        password_label.place(y=100, x=385)
        password_entry.place(x=530, y=100)
        login_button.place(y=135, x=530)
        
        register_frame = ctk.CTkFrame(login_labelFrame)
        register_button = ctk.CTkButton(register_frame, text="Register", font=("Arial", 16), hover=True, 
                                     hover_color="black", fg_color="green", corner_radius=30,
                                     command=register)
        register_button.pack(side="right", fill="both", padx=30, pady=35)
        register_frame.pack(anchor="center", pady=20, padx=150, fill="both")

        login_labelFrame.pack(anchor="center", fill="both")


        log_in_frame.pack(anchor="center", pady=5, padx=5, fill="both", expand=True)