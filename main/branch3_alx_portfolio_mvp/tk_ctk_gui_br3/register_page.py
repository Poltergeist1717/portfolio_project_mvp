import tkinter as tk
import customtkinter as ctk
from usernsme_password_control_func import username_password_control
from confirming_password_cnfrmpswd_func import confirming_password
from collect_registeration_data_func import collect_reg_data

class Register_page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        register_label = tk.Label(self, text="Register Page")
        register_label.pack(anchor="center", pady=(5, 5), padx=5)

        register_frame = ctk.CTkFrame(self)

        # username = username_entry.get()
        # password = password_entry.get()
        # confirm_password = confirm_password_entry.get()

        #Defining the username and password control function
        #username_password_control(username=username_entry.get(), password=password_entry.get(), confirm_password=confirm_password_entry.get())
        
        # Define a function to confirm the password
        #confirming_password(password=username_entry.get(), confirm_password = confirm_password_entry.get())
                
            #Defining registeration processor function    
        def register():
            username = username_entry.get()
            password = password_entry.get()
            confirm_password = confirm_password_entry.get()

            if username_password_control(username, password, confirm_password):
                if confirming_password(password, confirm_password):
                    collect_reg_data(username, password)
                    controller.display_page("Log_in_page")




        register_labelFrame = ctk.CTkFrame(register_frame)

        register_labelFrame2 = tk.LabelFrame(register_labelFrame, font=("Arial", 15), text="Register", 
                                          cursor="hand2", relief="solid", background="purple")
        register_labelFrame2.pack(anchor="center", ipadx=160, ipady=160, fill="both", padx=80, pady=50)

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
        
        register_labelFrame.pack(anchor="center", fill="both", pady=100, padx=100, expand=True)


        register_frame.pack(anchor="center", pady=5, padx=5, fill="both", expand=True)
