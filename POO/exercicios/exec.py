"""
Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor

Ultilizando typing annotations, encapsulamento, setter.
"""


class Bola:
    def __init__(self, cor: str, material: str, circunferencia: float) -> None:
        self._cor = cor
        self._material = material
        self._circunferencia = circunferencia

    @property
    def cor(self) -> str:
        return self._cor

    @property
    def material(self) -> str:
        return self._material

    @property
    def circunferencia(self) -> float:
        return self._circunferencia

    def troca_cor(self, cor: str) -> None:
        self._cor = cor

    def mostra_cor(self) -> str:
        return self._cor


bola = Bola("preta", "borracha", 1.45)
print(bola.mostra_cor())
bola.troca_cor("Azul")
print(bola.mostra_cor())
