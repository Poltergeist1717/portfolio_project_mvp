import projects_sug_generator
import json

# def generate():
#     prompt = "Please generate best 10 suggestions for codind projects."
#     language = language_dropdown.get()
#     prompt += "The programming language is " + language + "."
#     difficulty = difficulty_value.get()
#     prompt += "The difficulty for the project should be " + difficulty + "."
#     experience_level = experience_value.get()
#     prompt += "My experience level is " + experience_level + "."

#     if feature_checkbox1.get():
#         prompt += "The project should include a database."
#     if feature_checkbox2.get():
#         prompt += "The project should include API."


# def change_theme():
#     if theme_button.get() == 1:
#         ctk.set_appearance_mode("dark")
#     else:
#         ctk.set_appearance_mode("system")

# def call_pack():
#     screen_width = root.winfo_screenwidth()
#     screen_height = root.winfo_screenheight()
#     if screen_height <= 720 and screen_width <= 1600:
#         radiobutton1.pack(side="top", padx=60, pady=10, expand = True)
#         radiobutton2.pack(side="top", padx=60, pady=10, expand = True)
#         radiobutton3.pack(side="top", padx=60, pady=10, expand = True)
#     else:
#         radiobutton1.pack(side="left", padx=60, pady=10, expand = True)
#         radiobutton2.pack(side="left", padx=60, pady=10, expand = True)
#         radiobutton3.pack(side="left", padx=60, pady=10, expand = True)


def chatgpt_cache(prompt, answer):
    cached_dict = {}
    cached_dict[prompt] = answer
    with open ("cached_dict_file.json", "w") as cached_file:
        json.dump(cached_dict, cached_file)

def read_cached():
    with open ("cached_dict_file.json", "r") as cached_file:
        #read_cached_file = json.load(cached_file.read())
        return json.load(cached_file)
    
def checking_cached_file(prompt):
    cached_file = read_cached()
    try:
        if prompt in cached_file.keys():
            checked_key = prompt
            answer = cached_file.get(checked_key,)
            return answer
        else:
            return prompt
    except Exception as y:
        print (y)