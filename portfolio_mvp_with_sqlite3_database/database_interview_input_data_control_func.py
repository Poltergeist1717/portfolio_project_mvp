from tkinter import messagebox

def empty_or_not(interview_serial_number, candidate_serial_number):
    if len(interview_serial_number) < 1:
        messagebox.showerror(title="Error!", message="Interview Serial Number cannot be empty!")
        return False
    
    if len(candidate_serial_number) < 1:
        messagebox.showerror(title="Error!", message="Candidate Serial Number cannot be empty!")
        return False
    
    return True
    

def pref_feature(feature_value1, feature_value2):
    feature = ""
    if feature_value1 == "on" and feature_value2 == "on":
        feature = "Database and API"
    elif feature_value2 == "on":
        feature = "API"
    elif feature_value1 == "on":
        feature = "Database"
    else:
        feature = "None"
    return feature
