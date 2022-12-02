from abc import ABC


class Person(ABC):
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age


class Client(Person):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
