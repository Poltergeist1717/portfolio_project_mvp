import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from usernsme_password_control_func import username_password_control
from confirming_password_match_func import confirming_password
from collecting_username_password_data_into_database_func import username_password_database_data_entry_collector
from database_username_duplcate_ctrl_func import username_duplicated_control

class Register_page(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        register_label = ctk.CTkLabel(self, text="Register Page")
        register_label.pack(anchor="center", pady=(5, 5), padx=5)

        register_frame = ctk.CTkFrame(self)
                
            #Defining registeration processor function    
        def register():
            username = username_entry.get()
            password = password_entry.get()
            confirm_password = confirm_password_entry.get()

            try:
                if username_duplicated_control(username):
                    if username_password_control(username, password, confirm_password):
                        if confirming_password(password, confirm_password):
                            username_password_database_data_entry_collector(username, password, confirm_password)
                            controller.display_page("Log_in_page")
            except Exception as e:
                messagebox.showerror(title="Error occured in register!", message="There was an error:" + str(e))    
        def back():
            controller.display_page("Log_in_page")


        register_labelFrame = ctk.CTkFrame(register_frame)

        register_labelFrame2 = tk.LabelFrame(register_labelFrame, font=("Arial", 15), text="Register", 
                                          cursor="hand2", relief="solid", background="purple")
        register_labelFrame2.pack(anchor="center", ipadx=160, ipady=160, fill="both", padx=80, pady=20)

        #Creating log_in widgets
        username_label = ctk.CTkButton(register_labelFrame2, text="Username", font=("Arial", 16), 
                                       bg_color="#FF4500", fg_color="#FF4500", hover=False)
        username_entry = ctk.CTkEntry(register_labelFrame2, font=("Arial", 16))
        password_entry = ctk.CTkEntry(register_labelFrame2, show="*", font=("Arial", 16))
        password_label = ctk.CTkButton(register_labelFrame2, text="Password", font=("Arial", 16), 
                                       bg_color="#FF4500", fg_color="#FF4500", hover=False)
        confirm_password_entry = ctk.CTkEntry(register_labelFrame2, show="*", font=("Arial", 16))
        confirm_password_label = ctk.CTkButton(register_labelFrame2, text="Confirm Password", font=("Arial", 16), 
                                       bg_color="#FF4500", fg_color="#FF4500", hover=False)
        register_button = ctk.CTkButton(register_labelFrame2, text="Register", font=("Arial", 16), hover=True, 
                                     hover_color="black", fg_color="#FF4500", corner_radius=30, command= register)

        #Placing widgets on the screen
        username_label.place(y=50, x=385)
        username_entry.place(x=530, y=50)
        password_label.place(y=100, x=385)
        password_entry.place(x=530, y=100)
        confirm_password_entry.place(x=530, y=150)
        confirm_password_label.place(y=150, x=385)
        register_button.place(y=195, x=530)


        back_frame = ctk.CTkFrame(register_labelFrame, fg_color="purple")
        back_frame.pack(anchor="center", pady=5, padx=5, fill="both", expand=True)

        return_frame = ctk.CTkFrame(back_frame, fg_color="#FF4500")
        return_frame_button = ctk.CTkButton(return_frame, text="Back", font=("Arial", 15), hover=True, 
                                     hover_color="black", fg_color="purple", corner_radius=30,
                                     command=back)
        return_frame_button.pack(side="left", padx=20, pady=30)
        return_frame.pack(anchor="center", pady=10, padx=150, fill="both")

        return_frame.pack(anchor="center", fill="both", pady=10, padx=10, expand=True)
        
        register_labelFrame.pack(anchor="center", fill="both", pady=20, padx=100, expand=True)


        register_frame.pack(anchor="center", pady=5, padx=5, fill="both", expand=True)
