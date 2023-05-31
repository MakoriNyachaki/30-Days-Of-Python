from __future__ import print_function

"""
Create an empty dictionary called dog
Add name, color, breed, legs, age to the dog dictionary
"""

dog = {}
dog['name'] = "Simba"
dog['color'] = "black"
dog['breed'] = "German Shephard"
dog['legs'] = 4
dog['age'] = 1.5

print(f"\n{dog}\n")


"""
Create a student dictionary and add first_name, last_name,
gender, age, marital status, skills, country, city and
address as keys for the dictionary
"""


student = {
        "first_name": "Faithful",
        "last_name": "Onwes",
        "gender": "Female",
        "age": 39,
        "marital_status": "Single",
        "skills": "Python, Java, Microsoft Office Packages",
        "country": "Kenya",
        "city": "Nyamokenye",
        "address": "4560-45000, Nyamokenye"
        }

print(student)

for r, v in student.items():
    print(f"{r}:{r}")

# Length

print(f"\nLength: {len(student)}")

# Skills value

student['skills'] = "Python, Java, Microsoft Office Packages, HTML, SQL"

# Get skills

print(f"\nskills: {student.get('skills')}")

# Keys as a list

k = student.keys()

print(f"\nKeys\n {k}")

# Values of a list

v = student.values()
print(f"\nValues\n {v}")

# Dictonary to a list of items

print(f"\nList of Items\n{student.items()}")

# Delete one of the items from the dictionary

print(student.pop("marital_status"))

print(f"\nMarital Status deleted\n{student}")

# Delete one of the dictionaries

del dog
