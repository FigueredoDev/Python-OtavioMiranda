from abc import ABC


class People(ABC):
    def __init__(self, name: str, phone: str, email: str) -> None:
        self._name = name
        self._phone = phone
        self._email = email

    @property
    def name(self) -> str:
        return self._name

    @property
    def phone(self) -> str:
        return self._phone

    @property
    def email(self) -> str:
        return self._email

    def update_data(self) -> str:
        return 'Updating DataBase'
