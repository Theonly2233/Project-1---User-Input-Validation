# ==========================================
# PROJECT 1 - USER INPUT VALIDATION
# ==========================================
# Version 6
# - Added education validation to the valid_input function.
# - Used \n for new lines in print statements to improve readability.
# - Improved code formatting and readability.
# - Added docstrings to functions for better documentation.
# - removed redundant .strip() and .lower() calls in the main execution.
# ==========================================

# ==========================================
# CONSTANTS
# ==========================================
EDUCATION_DICT = {
'a': 'Some Highschool',
'b': 'Highschool Diploma',
'c': 'Some College',
'd': 'Associate Degree',
'e': "Bachelor's Degree",
'f': "Graduate's Degree"
}

# ==========================================
# FUNCTIONS
# ==========================================
def valid_input(variable, type_of_input):
    """
    Validates and formats user input based on the specified category.
    
    Args:
       variable (str): The raw input string to validate.
       type_of_input (str): The category of validation ('name', 'age', 'education').
    
    Returns:
        str/int/None: The formatted value if valid, otherwise None.
    """
    variable = variable.strip()

    if type_of_input == "name":
        if not variable.isalpha():
            print('''Invalid name.\nName should only include letters.''')
        else:
            return variable.capitalize()
        
    elif type_of_input == "age":
        if not variable.isdecimal():
            print('''Invalid age.\nAge should only include numbers.''')
        elif int(variable) < 14:
            print('''Invalid age.\nMust be 14 years or older to register.''')
        else:
            return int(variable)
        
    elif type_of_input == "education":
        education_input = variable.lower()
        education = EDUCATION_DICT.get(education_input)
        if education:
            return education
        else:
            print('''Invalid education level.\nPlease answer in one letter, A through F.''')
    else:
        return None

def get_input(prompt, type_of_input):
    """Repeatedly prompts user until valid input is provided."""
    while True:
        variable = input(prompt)
        result = valid_input(variable, type_of_input)
        if result:
            return result

# ==========================================
# MAIN EXECUTION
# ==========================================
first_name = get_input('Hello, what is your name?', "name")
last_name = get_input(f'Whats your last name, {first_name}?', "name")
age = get_input(f'How old are you {first_name} {last_name}?', "age")
education = get_input('''whats your education level? 
A: Some Highschool
B: Highschool Diploma
C: Some College
D: Associate Degree
E: Bachelor's Degree
F: Graduate's Degree''', "education")

print(f'{first_name} {last_name} is {age} years old, and has an education level of: {education}')
