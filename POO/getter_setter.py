from typing import Union


class Produto:
    def __init__(self, nome: str, preco: Union[int, float]) -> None:
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual: Union[int, float]) -> None:
        self.preco -= (self.preco * (percentual / 100))

    # Getter
    @property
    def preco(self):
        return self._preco

    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace("R$", ""))

        self._preco = valor


produto1 = Produto("Camiseta", 50)
produto1.desconto(10)

print(produto1.preco)

produto2 = Produto("Caneca", "R$15")  # type: ignore
produto2.desconto(10)

print(produto2.preco)
