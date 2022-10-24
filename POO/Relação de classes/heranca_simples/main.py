"""
Associação - Usa | Agregação - Tem | Composição - É dono | Herança - É
"""
from classes import Cliente, Aluno

cliente1 = Cliente("Luiz", 25)
cliente1.falar()
cliente1.comprar()

aluno1 = Aluno("Maria", 15)
aluno1.falar()
aluno1.estudar()
