# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 14:31:47 2023

@author: James Fehr
# Animal Class definition, my start with oop in python
"""

class Animal:
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print("Woof!" * 3)


class Cat(Animal):
    def make_sound(self):
        print("Meow!" * 3)


def make_animal_sound(animal):
    animal.make_sound()


my_dog = Dog()
my_cat = Cat()

make_animal_sound(my_dog)  # Output: Woof! * 3
make_animal_sound(my_cat)  # Output: Meow! * 3
