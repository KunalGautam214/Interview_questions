import typing


class Person:
    name = 'Kunal'

    def __init__(self):
        self.age = 25
        self._college_id = 0

    def __str__(self):
        return 'Person object'

    def __call__(self, *args, **kwargs):
        return 'Person object is callable'

    @property
    def college_id(self):
        print('getter is called')
        return self._college_id

    @college_id.setter
    def college_id(self, college_id):
        print('setter is called to set college id')
        self._college_id = college_id

    @classmethod
    def print_name(cls):
        print('My name is ', cls.name)

    @classmethod
    def print_age(cls):
        print('Can not access instance variable in class methods')
        # print('My age is ', cls.age, self.age)

    @staticmethod
    def college_name():
        print('This is an utility method not bound to class or a instance variable')

    @typing.final
    def final_method(self):
        print('This is a final method can not be overridden in the child class')

Person().print_name()
Person.college_name()
Person().final_method()
p = Person()
p.college_id = 1234
print(p.college_id)
print(p)
print(p())

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    #inherited class will implement this abstractmethod


