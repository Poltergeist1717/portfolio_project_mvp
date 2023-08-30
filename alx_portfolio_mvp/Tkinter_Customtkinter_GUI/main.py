import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from candidate_class import Candidate_page
from next_of_kin_class import Next_Of_Kin_page
from interview_class import Interview_page

class App(tk.Tk):
    def __init__(self, *arg, **kwarg):
        tk.Tk.__init__(self, *arg, **kwarg)

        #Create the main Frame
        root = ctk.CTkScrollableFrame(self, height=1900)

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


        #Create the Theme Frame
        theme_frame = ctk.CTkFrame(self)
        theme_frame.pack(anchor="e" ,padx = 50, pady = (5, 5), fill="both")

        #create theme button
        theme_button = ctk.CTkSwitch(theme_frame, text= "Change Theme", 
                            font=ctk.CTkFont(size= 15, weight= "normal"), command= change_theme,
                            onvalue = 1, offvalue = 0, fg_color="#FFFFFF", progress_color="#FFFFFF", 
                            border_color="#000000", button_color="#000000", button_hover_color="#FFFFFF",)
        theme_button.pack(anchor = "e", padx=5, pady =(5, 5))

        self.title("Projects Suggestions Generator")

        ctk.set_appearance_mode("dark")

        self.screen_width = root.winfo_screenwidth() #Variable to dynamically catch the screen wdith 
        self.screen_height = root.winfo_screenheight() #Variable to dynamically catch the screen height

        self.geometry("{}x{}".format(self.screen_height, self.screen_width))

        #Pack the root frame
        root.pack(expand = True, fill = "both", pady=10)
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

        #Create an empty dictionary to store pages
        self.frames = {} 

        for page in (Candidate_page, Next_Of_Kin_page, Interview_page):
            page_name = page.__name__
            frame = page(root, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.display_page("Candidate_page")
        
    def display_page(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop()