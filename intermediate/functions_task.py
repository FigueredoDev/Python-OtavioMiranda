def multiply(*args):
    total = 1
    for arg in args:
        total *= arg

    return total


def speak(number):
    if number % 2 == 0:
        return "Numero Par"

    return "Numero Impar"


print(speak(1))
