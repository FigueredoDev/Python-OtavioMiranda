# cSpell: disable
from os import name, system

from src.list_task import ListOne, ListThree, ListTwo
from src.validate import ValidateResponse


def clear_terminal(): return system("cls" if name == "nt" else "clear")


while True:
    class Menu(ValidateResponse):
        def __init__(self) -> None:
            clear_terminal()

            print("""
Escolha uma das listas de atividades:

                Fundamentos do python

1 -  Faça um Programa que mostre a mensagem "Alo mundo" na tela.

2 - Faça um Programa que peça um número e então mostre a mensagem:
    número informado foi [número].

                Estruturas condicionais

3 - Faça um programa que receba um número inteiro e verifique se este número é maior que 20,
em caso afirmativo o programa deverá imprimir a mensagem: "Maior que 20".

4 - Faça um programa que leia dois valores inteiros e efetue a adição. Caso o valor somado seja maior que 20,
este deverá ser apresentado somando-se a ele mais 8, caso o valor somado seja menor ou igual a 20,
este deverá ser apresentado subtraindo-se 5.

                Estruturas de repetição

5 - Faça um programa que leia 5 números e informe a soma e a média dos números.

6 - Faça um programa que leia 10 valores e ao final imprima a média aritmética valores lidos.

                Finalizar programa!

7 - Fechar Menu

Digite o numero referente a atividade. Exemplo: 1 para abrir a atividade 1 de Fundamentos de Python.
            """)

            self.switch(self.validate_main_menu())

        def switch(self, value):
            return getattr(self, "list_" + str(value), lambda: "Invalida")()

        def list_1(self):
            return ListOne().question_one()

        def list_2(self):
            return ListOne().question_two()

        def list_3(self):
            return ListTwo().question_one()

        def list_4(self):
            return ListTwo().question_two()

        def list_5(self):
            return ListThree().question_one()

        def list_6(self):
            return ListThree().question_two()

        def list_7(self):
            option = input("\n Deseja mesmo sair? [S/N] ").lower()
            if option == "s":
                print("Finalizando")
                exit()
            elif option == "n":
                return
            else:
                print("Opcao invalida!")

    if __name__ == "__main__":
        menu = Menu()
