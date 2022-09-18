"""
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""
from typing import Union


class Quadrado:
    def __init__(self, tamanho_lado: Union[int, float]) -> None:
        self._tamanho_lado = tamanho_lado

    @property  # Retornar valor do Lado
    def tamanho_lado(self) -> Union[int, float]:
        return self._tamanho_lado

    def mudar_lado(self, valor: Union[int, float]) -> None:
        self._tamanho_lado = valor

    def calular_area(self) -> float:
        self.area = self._tamanho_lado * 2
        return self.area


# Retornar valor do lado
quadrado1 = Quadrado(20)
print(quadrado1.tamanho_lado)

# Mudar o valor do lado
quadrado1.mudar_lado(25)
print(quadrado1.tamanho_lado)

# Calular area do quadrado
area = quadrado1.calular_area()
print("A area do quadrado: %d" % area)
