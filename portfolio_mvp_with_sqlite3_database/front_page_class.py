import customtkinter as ctk
#from PIL import ImageTk, Image

class Front_page(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        #Create Info page Label
        front_page_label = ctk.CTkLabel(self, text="You Are Welcome To CruxAming")
        front_page_label.pack(anchor="center", pady=5, padx=5)

        #Create Info Page Frame
        front_page_frame = ctk.CTkFrame(self)

        #Defining the function to EXIT the program

        # def exit():
        #     result = messagebox.askyesno(title="Quit", message="Are you sure you want to exit?")
        #     if result:
        #         controller.destroy()

        page_frame = ctk.CTkFrame(front_page_frame, fg_color="#FF4500")

        page_frame_button = ctk.CTkButton(page_frame, text="Welcome to \nCruxAming", width=900, height=300, 
                                            font=ctk.CTkFont(family="Times New Roman", size=100), hover=True,
                                            corner_radius=15, bg_color="transparent",
                                            hover_color="black", fg_color="purple", border_color="purple")
        page_frame_button.pack(side="right", padx=10, pady=(10, 10), expand=True, ipadx=20)
    
        page_frame.pack(fill="both", expand=True, padx=10, pady=10)


         #Create bottom frame for NEXT and BACK buttons
        bottom_frame = ctk.CTkFrame(page_frame, fg_color="purple")

        #Create the REGISTER button
        bottom_frame_button1 = ctk.CTkButton(bottom_frame, text="Sign Up", 
                                            font=ctk.CTkFont(family="Sarif bold", size=12), 
                                            width=30, height=30, hover=True,
                                            corner_radius=15, bg_color="transparent",
                                             hover_color="black", fg_color="#FF4500", border_color="#FF4500",
                                             command= lambda: controller.display_page("Register_page"))
        bottom_frame_button1.pack(anchor="w", pady=(85, 35), ipadx=2, padx=20)
        
        #Create the LOGIN Button
        bottom_frame_button2 = ctk.CTkButton(bottom_frame, text="Sign In", 
                                            font=ctk.CTkFont(family="Sarif bold", size=12), 
                                            width=30, height=30, hover=True,
                                            corner_radius=15, bg_color="transparent",
                                            hover_color="black", fg_color="#FF4500", border_color="#FF4500",
                                            command = lambda: controller.display_page("Log_in_page"))
        bottom_frame_button2.pack(anchor="n", pady=(35, 65), ipadx=2, padx=20)
        bottom_frame.pack(side="left", fill="y", padx=20, pady=(5, 15))

        page_frame2 = ctk.CTkFrame(front_page_frame, fg_color="purple")

        # display_image = ImageTk.PhotoImage(Image.open("5.jpg"))
        # label = ctk.CTkLabel(page_frame2, image=display_image)
        # label.pack()

        page_frame2.pack(anchor="center", fill="both", expand=True, padx=10, pady=10)


        front_page_frame.pack(fill="both", padx=50)
