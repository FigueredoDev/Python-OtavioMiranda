from os import name, system
from time import sleep

from src.validate import ValidateResponse


def clear_terminal():
    return system("cls" if name == "nt" else "clear")


class ListOne(ValidateResponse):
    def list_menu(self):
        clear_terminal()

        validate_response = self.validate_list_menu()
        if validate_response == 1:
            self.question_one()
        elif validate_response == 2:
            self.question_two()
        else:
            return None

    def question_one(self):
        print("\n Resposta: Alo mundo \n\n Retornando ao menu.")
        sleep(3)

    def question_two(self):

        value = input("Digite um numero: ")

        if not value.isdigit():
            print("Digite apenas números inteiros, Tente novamente!")
            sleep(3)
        else:
            print(f"\n O número digitado foi {value} \n\n Retornando ao menu.")
            sleep(3)


class ListTwo(ValidateResponse):
    def list_menu(self):
        clear_terminal()

        validate_response = self.validate_list_menu()
        if validate_response == 3:
            self.question_one()
        elif validate_response == 4:
            self.question_two()
        else:
            return None

    def question_one(self):
        value = input("Digite um numero:")

        if not value.isdigit():
            print("Digite apenas números inteiros, Tente novamente!")
            sleep(2)
        else:
            value = int(value)
            if (value > 20):
                print("\n Maior que 20")
                sleep(2)
            else:
                print("\n Menor que 20")
                sleep(2)

    def question_two(self):
        value1 = input("\n Digite um numero: ")
        value2 = input("\n Digite um outro numero: ")

        if not value1.isdigit() and value2.isdigit():
            print("Digite apenas números inteiros, Tente novamente!")
            sleep(2)
        else:
            value1 = int(value1)
            value2 = int(value2)
            sum = value1 + value2

            if sum > 20:
                sum += 8
                print(f"\n Resultado: {sum}")
                sleep(2)
            elif sum <= 20:
                sum -= 5
                print(f"\n Resultado: {sum}")
                sleep(2)


class ListThree(ValidateResponse):
    def list_menu(self):
        clear_terminal()

        validate_response = self.validate_list_menu()
        if validate_response == 5:
            self.question_one()
        elif validate_response == 6:
            self.question_two()
        else:
            return None

    def question_one(self):
        soma = 0
        for i in range(5):
            value = input("\n Digite um numero:")
            if not value.isdigit():
                print("Digite apenas números inteiros, Tente novamente!")
                sleep(2)
            else:
                value = int(value)
                soma = soma + value
                media = soma / 5

        print("\n Soma :", soma)
        print(f"\n Média({soma}/5): {media}")
        sleep(3)

    def question_two(self):
        count = 0
        result = 0
        while count < 10:
            value = input("\n Digite um numero: ")

            if not value.isdigit():
                print("Digite apenas números inteiros, Tente novamente!")
                sleep(2)
            else:
                value = int(value)
                result += value
                count += 1

        print(f"\n Resultado: {result / 10}")
        sleep(2)


if __name__ == "__main__":
    l1 = ListThree()
    l1.list_menu()
