from __future__ import print_function
"""
Instance attributes - They can be accessed
globally through the class
"""


class Person:
    counter = 0

    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country
        Person.counter += 1

    def greet(self):
        return (f'Hi, I am {self.name}, {self.age}' +
                f' years old and from {self.country}.')


p1 = Person('Jane Nyagaka',  34, 'Kenya')
p2 = Person('Darius Abu', 26, 'Rwanda')
p3 = Person('Dennis Oka', 45, 'Nigeria')

print(Person.counter)  # Output: 3
