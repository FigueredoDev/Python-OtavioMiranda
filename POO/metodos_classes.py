# Métodos relacionados a classe
from random import randint


class Person:
    current_year = 2022

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_ano_nascimento(self):
        print(self.current_year - self.age)

    @classmethod
    def by_birth_year(cls, name, birth_year):
        age = cls.current_year - birth_year
        return cls(name, age)

    @staticmethod
    def generate_id():
        id = randint(0, 100)
        return id


person_one = Person.by_birth_year("Jhonata", 2001)
print(person_one.generate_id())
print(Person.generate_id())
