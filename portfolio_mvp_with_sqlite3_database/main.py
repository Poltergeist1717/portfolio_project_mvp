import customtkinter as ctk
from tkinter import messagebox
from candidate_page_class import Candidate_page
from next_of_kin_page_class import Next_Of_Kin_page
from interview_page_class import Interview_page
from login_page_class import Log_in_page
from register_page_class import Register_page
from front_page_class import Front_page

class App(ctk.CTk):
    def __init__(self, *arg, **kwarg):
        ctk.CTk.__init__(self, *arg, **kwarg)

        #Create the main Frame
        root = ctk.CTkFrame(self)

         #Function for changing THEME
        def change_theme():
            try:
                if theme_button.get() == 1:
                    ctk.set_appearance_mode("system")
                else:
                    ctk.set_appearance_mode("dark")
            except Exception as y:
                messagebox.showerror(title="Error", message= "An error occurred while changing the theme: " + str(y))
                ctk.set_appearance_mode("dark")

        #Defining the function to EXIT the program

        def exit():
            result = messagebox.askyesno(title="Quit", message="Are you sure you want to exit?")
            if result:
                root.quit()


        #Create the Theme Frame
        theme_frame = ctk.CTkFrame(self)
        theme_frame.pack(anchor="e" ,padx = 20, fill="both", ipadx=20)

        #create theme button
        theme_button = ctk.CTkSwitch(theme_frame, text= "Change Theme", 
                            font=ctk.CTkFont(size= 15, weight= "normal"), command= change_theme,
                            onvalue = 1, offvalue = 0, fg_color="#FFFFFF", progress_color="#FFFFFF", 
                            border_color="#000000", button_color="#000000", button_hover_color="#FFFFFF",)
        theme_button.pack(side="right", padx=10, pady=20)

        #Create the EXIT button
        exit_button = ctk.CTkButton(theme_frame, text="EXIT", 
                                            font=ctk.CTkFont(family="Sarif bold", size=12), 
                                            width=30, height=30, hover=True,
                                            corner_radius=15, bg_color="transparent",
                                             hover_color="black", fg_color="red", border_color="red",
                                             command= exit)
        exit_button.pack(side="left", pady=10, padx=20)

        self.title("CruxAming")

        ctk.set_appearance_mode("dark")

        self.screen_width = root.winfo_screenwidth() #Variable to dynamically catch the screen wdith 
        self.screen_height = root.winfo_screenheight() #Variable to dynamically catch the screen height

        self.geometry("{}x{}".format(self.screen_height, self.screen_width))

        #Pack the root frame
        root.pack(expand=True, fill = "both", pady=10)
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

        #Create an empty dictionary to store pages
        self.frames = {} 

        for page in (Front_page ,Log_in_page, Register_page, Candidate_page, Next_Of_Kin_page, Interview_page):
            page_name = page.__name__
            frame = page(root, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.display_page("Front_page")
        
    def display_page(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop()