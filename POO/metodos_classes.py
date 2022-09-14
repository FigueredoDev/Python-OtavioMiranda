# Metodos relacionados a classe
from random import randint


class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        id = randint(0, 100)
        return id


p1 = Pessoa.por_ano_nascimento("Jhonata", 2001)
print(p1.gera_id())
print(Pessoa.gera_id())
