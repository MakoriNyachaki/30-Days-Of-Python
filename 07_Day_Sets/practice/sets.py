from __future__ import print_function

# sets
it_companies = {
        'Facebook', 'Google', 'Microsoft',
        'Apple', 'IBM', 'Oracle', 'Amazon'
        }
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Length of the set it_companies

print(f"\nLength of it_companies: {len(it_companies)}\n")

# Add twitter to it_companies

it_companies.add("Twitter")
print(f"After adding Twitter\n{it_companies}\n")

# Insert multiple IT companies at once to the set it_companies

it_companies.update(['Sesoft', 'HP', 'Alibaba', 'Toshiba', 'Dell'])
print(f"After adding multiple\n{it_companies}\n")

# Remove one of the companies from the set it_companies

it_companies.remove("Sesoft")
print(f"Removed Sesoft\n{it_companies}\n")

# What is the difference between remove and discard

"""
Both are used to remove elements from a set. However, remove prints an error
if the element to be removed is not found while discard removes an element
silently without printing an error even if when the element is not found
"""

# Join A and B

print(f"A and B joined\n{A.union(B)}\n")

# Find A intersection B

print(f"Intersection between A and B\n{A.intersection(B)}\n")

# Is A subset of B

print(f"A is a subset of B\n{A.issubset(B)}\n")

# Are A and B disjoint sets

print(f"Are A and B disjoint sets?\n{A.isdisjoint(B)}\n")

# Join A with B and B with A

print(f"A with B\n{A.union(B)}\nB with A\n{B.union(A)}\n")

# What is the symmetric difference between A and B

print(f"Symmetric difference between A and B\n{A.symmetric_difference(B)}\n")

# Delete the sets completely

del A
del B

# Convert the ages to a set and compare the length
# of the list and the set, which one is bigger?

age_set = set(age)
print(f"\nConverted age into a set\n{age_set}\n")

if len(age) > len(age_set):
    print(
            f"Age list is greater than the age set\n" +
            f"Age_list\tgreater than\tage_set\n" +
            f"{len(age)}\t\t > \t\t{len(age_set)}\n"
            )
elif len(age_set) > len(age):
    print(
            f"Age set is greater than age list" +
            f"\nage_set\tgreater than\tage_list\n" +
            f"{len(age_set)}\t\t > \t\t{len(age)}\n"
            )
else:
    print(
            f"Age_set is equal to age list\nage_set" +
            f"\tequal to\tage_list\n{len(age_set)}\t=\t{len(age)}\n"
            )

# Explain the difference between the following data types:
# string, list, tuple and set

"""
string -
list - a ordered list of elements of either the same type or dffernt types
tuple - an immutable list
set - an unordered list of unique elements
"""

"""
I am a teacher and I love to inspire and teach people.
How many unique words have been used in the sentence?
Use the split methods and set to get the unique words.
"""

sentence = "I am a teacher and I love to inspire and teach people"

lst = sentence.split(' ')
set_lst = set(lst)
print(f"There are {len(set_lst)} unique words\n")
