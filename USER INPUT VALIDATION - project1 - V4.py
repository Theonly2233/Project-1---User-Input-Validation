# ==========================================
# PROJECT 1 - USER INPUT VALIDATION
# ==========================================
# Version 4
# - Added a new function to validate both name and age inputs.
# - Added a constant to store the education levels dictionary.
# - Formatting changes to improve readability.
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

# ==========================================
# MAIN EXECUTION
# ==========================================
while True:
    first_name = input('Hello, what is your name?')
    first_name = valid_input(first_name, "name")
    if not first_name:
        continue
    else:
        break

while True:
    last_name = input(f'Whats your last name, {first_name}?')
    last_name = valid_input(last_name, "name")
    if not last_name:
        continue
    else:
        break

while True:
    age = input(f'How old are you {first_name} {last_name}?')
    age = valid_input(age, "age")
    if not age:
        continue
    else:
        break

while True:
    education_input = input('''Whats your education level?
A: Some Highschool
B: Highschool Diploma
C: Some College
D: Associate Degree
E: Bachelor's Degree
F: Graduate's Degree
''').lower()
    education = EDUCATION_DICT.get(education_input)
    if education:
        break
    else:
        print('''Please answer in one letter, A through F
''')

print(f'{first_name} {last_name} is {age} years old, and has an education level of: {education}')
