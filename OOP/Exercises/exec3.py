"""
Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: base, altura (ou Comprimento e Largura, ou base e altura) # noqa
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro; 
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
"""


from typing import Tuple, Union


class Retangulo:
    def __init__(self, base: Union[int, float], altura: Union[int, float]):
        self.base = base
        self.altura = altura

    def valores(self) -> Tuple:
        return (self.base, self.altura)

    def mudar_lado(self, valorA: Union[int, float], valorB: Union[int, float]):
        self.base = valorA
        self.altura = valorB

    def calular_area(self) -> Union[int, float]:
        area = self.base * self.altura
        return area

    def calular_perimetro(self) -> Union[int, float]:
        perimetro = (self.base + self.altura) * 2
        return perimetro


base = float(input("Digite o valor da base: "))
altura = float(input("Digite o valor da altura: "))

local = Retangulo(base, altura)

print(
    f"Sera necessario {local.calular_area()}m quadrados de piso e {local.calular_perimetro()}m de rodapes para local")  # noqa E501
