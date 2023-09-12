#Defining calculator function
#Returns score

def database_score_update(question1_value, question2_value, question3_value, question4_value, question5_value):

    # question1_value = question1_var_value.get()
    # question2_value = question2_var_value.get()
    # question3_value = question3_var_value.get()
    # question4_value = question4_var_value.get()
    # question5_value = question5_var_value.get()

    score = 0

    if question1_value == "Ambivert":
        score += 20

    if question2_value == "Both, depending on the situation":
        score += 20

    if question3_value == "Embrace criticism and use it for improvement":
        score += 20

    if question4_value == "Very adaptable":
        score += 20
    
    if question5_value == "Stay calm and focused":
        score += 20

    return score
