import json
import os

# Function to dynamically find file 
# From a targeted folder/dir and other parralel folder/dir and parent folder/dir until root
# Breaks when it reahes the root 
# Returns none if no file of the name provided is present 

def find_file(start_dir, target_folder, filename):
    current_dir = start_dir

    while True:
        # Construct the path to check for the JSON file
        file_path = os.path.join(current_dir, target_folder, filename)

        if os.path.exists(file_path):
            return file_path

        # Construct the path to check for the JSON file within the current directory
        file_path_same_level = os.path.join(current_dir, filename)

        if os.path.exists(file_path_same_level):
            return file_path_same_level

        # Move up one level in the directory structure
        current_dir = os.path.dirname(current_dir)

        # Check if we've reached the root directory (e.g., on Unix-like systems, '/')
        if current_dir == os.path.dirname(current_dir):
            break

    return None

#Function to check if file is present in path
#Returns file if present
def check_file_presence_rtn_file():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Specify the target folder and JSON file name
    target_folder = "branch3_alx_portfolio_mvp"
    json_filename = "collected_username_password.json"

    # Find the JSON file path
    json_file_path = find_file(script_dir, target_folder, json_filename)

    if json_file_path:
        try:
             with open(json_file_path, "r") as file:
                json_data = json.load(file)
                return json_data
        except FileNotFoundError:
            return None
    #print(f"File '{json_file_path}' not found.")
    else:
        print(f"JSON file '{json_filename}' not found in '{target_folder}' or its parent directories.")