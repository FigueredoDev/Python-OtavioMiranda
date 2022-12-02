from typing import Union


class Product:
    def __init__(self, name: str, price: Union[int, float]) -> None:
        self.nome = name
        self.price = price

    def discount(self, percentage: Union[int, float]) -> None:
        self.price -= (self.price * (percentage / 100))

    # Getter
    @property
    def price(self):
        return self._price

    # Setter
    @price.setter
    def price(self, value):
        if isinstance(value, str):
            value = float(value.replace("R$", ""))

        self._price = value


product_one = Product("Camiseta", 50)
product_one.discount(10)

print(product_one.price)

product_two = Product("Caneca", "R$15")  # type: ignore
product_two.discount(10)

print(product_two.price)
