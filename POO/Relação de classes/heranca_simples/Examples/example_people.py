"""
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão,
a cada ano que nossa pessoa envelhece,
sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
"""


from typing import Union


class People:
    def __init__(self, name: str, age: int, weight: Union[int, float], height: Union[int, float]):  # noqa: E501
        self._name = name
        self._age = age
        self._weight = weight
        self._height = height

    @property
    def age(self):
        return self._age

    @property
    def weight(self):
        return self._weight

    @property
    def height(self):
        return self._height

    def get_old(self, age: int):
        if not isinstance(age, int):
            return 'the value of age must be int or float'

        if self._age <= 21:
            height = (age * 0.5)
            self._height += height
            self._age += age

            return f'You grew {self._height} and aged {self._age} years'

    def fatten(self, weight: Union[int, float]) -> Union[str, int, float]:
        if not isinstance(weight, (int, float)):
            return 'Wight must be int or float'

        self._weight += weight
        return self._weight

    def lose_weigh(self, weight: Union[int, float]) -> Union[str, int, float]:
        if not isinstance(weight, (int, float)):
            return 'Wight must be int or float'

        self._weight -= weight
        return self._weight

    def grow_up(self, height: Union[int, float]):
        if not isinstance(height, (int, float)):
            return 'Height must be int or float'

        self._height += height
        return self._height


people = People("Figueredo", 20, 70, 1.80)
print(people.height)
print(people.get_old(1))
print(people.height)
