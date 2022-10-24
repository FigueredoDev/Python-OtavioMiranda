from abc import ABC, abstractclassmethod
from typing import Union


class Account(ABC):
    def __init__(self, agency, account, balance):
        self._agency = agency
        self._account = account
        self._balance = balance

    @property
    def agency(self):
        return self._agency

    @property
    def account(self):
        return self._account

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance: Union[int, float]):
        if not isinstance(balance, (int, float)):
            raise ValueError('Your balance must be a numeric value.')

        self._balance = balance

    def deposit(self, value: Union[int, float]):
        if not isinstance(value, (int, float)):
            raise ValueError('Your value deposit must be numeric')

        self.balance += value

    def details(self):
        print(f'Agency: {self.agency}', end=' ')
        print(f'account: {self.account}', end=' ')
        print(f'balance: {self.balance}')

    @abstractclassmethod
    def withdraw(self, value: Union[int, float]):
        ...
