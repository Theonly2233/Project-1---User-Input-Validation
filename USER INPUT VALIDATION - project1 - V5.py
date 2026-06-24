# ==========================================
# PROJECT 1 - USER INPUT VALIDATION
# ==========================================
# Version 5
# - Added a new function to remove "while" loops in the main execution.
# - Added .strip() to remove whitespace from user input.
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
    variable = variable.strip()
    if type_of_input == "name":
        if not variable.isalpha():
            print('''Invalid name.
Name should only include letters.
''')
        else:
            return variable.capitalize()
    elif type_of_input == "age":
        if not variable.isdecimal():
            print('''Invalid age.
Age should only include numbers.
''')
        elif int(variable) < 14:
            print('''Invalid age.
Must be 14 years or older to register.
''')
        else:
            return int(variable)
    else:
        return None

def get_input(prompt, type_of_input):
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

while True:
    education_input = input('''Whats your education level?
A: Some Highschool
B: Highschool Diploma
C: Some College
D: Associate Degree
E: Bachelor's Degree
F: Graduate's Degree
''').strip().lower()
    education = EDUCATION_DICT.get(education_input)
    if education:
        break
    else:
        print('''Please answer in one letter, A through F
''')

print(f'{first_name} {last_name} is {age} years old, and has an education level of: {education}')
