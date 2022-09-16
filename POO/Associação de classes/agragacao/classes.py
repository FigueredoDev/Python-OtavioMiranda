from typing import List, Union


class CarrinhoDeCompras:
    def __init__(self) -> None:
        self.produtos: List = []

    def inserir_produtos(self, produto) -> None:
        self.produtos.append(produto)

    def lista_produto(self) -> None:
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma(self) -> float:
        total = 0
        for produto in self.produtos:
            total += produto.valor

        return total


class Produto:
    def __init__(self, nome: str, valor: Union[int, float]) -> None:
        self.nome = nome
        self.valor = valor
