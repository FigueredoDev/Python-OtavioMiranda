from time import sleep


class ValidateResponse:
    def validate_main_menu(self):
        number = input("-> ")

        if not number.isdigit():
            print("Digite apenas números inteiros, Tente novamente!")
            sleep(2)
        else:
            number = int(number)
            if not number <= 0 and not number < 8:
                print("Digite apenas números dentre as opções disponíveis no menu!")  # noqa: E501
                sleep(2)

        return number
