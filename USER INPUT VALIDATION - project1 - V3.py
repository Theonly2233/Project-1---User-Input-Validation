# ==========================================
# PROJECT 1 - USER INPUT VALIDATION
# ==========================================
# Version 3
# - Added a dictionary to store education levels.
# ==========================================

def valid_name(variable):
    if not variable.isalpha():
        print('''Invalid name.
Name should only include letters.
''')
    else:
        return variable.capitalize()

while True:
    first_name = input('Hello, what is your name?')
    first_name = valid_name(first_name)
    if not first_name:
        continue
    else:
        break

while True:
    last_name = input(f'Whats your last name, {first_name}?')
    last_name = valid_name(last_name)
    if not last_name:
        continue
    else:
        break

while True:
    age = input(f'How old are you {first_name} {last_name}?')
    if not age.isdecimal():
        print('''Invalid age.
Age should only include numbers
''')
    elif int(age) < 14:
        print('''User is too young.
Must be 14 years or older to register
''')
    else:
        break

education_dict = {
'a': 'Some Highschool',
'b': 'Highschool Diploma',
'c': 'Some College',
'd': 'Associate Degree',
'e': "Bachelor's Degree",
'f': "Graduate's Degree"
}

while True:
    education_input = input('''Whats your education level?
A: Some Highschool
B: Highschool Diploma
C: Some College
D: Associate Degree
E: Bachelor's Degree
F: Graduate's Degree
''').lower()
    education = education_dict.get(education_input)
    if education:
        break
    else:
        print('''Please answer in one letter, A through F
''')

print(f'{first_name} {last_name} is {age} years old, and has an education level of: {education}')
