from __future__ import print_function
"""
An example of the implementing a Person class
"""


class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def greet(self):
        return (f'Hi, I am {self.name} and am ' +
                f'{self.age} years old from {self.country}')


person = Person('Herbert', 20, 'Kenya')

print(person.greet())
