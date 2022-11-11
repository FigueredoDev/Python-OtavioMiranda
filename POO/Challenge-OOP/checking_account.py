from account import Account


class AccountChecking(Account):
    def __init__(self, agency, account, balance, limit=1000):
        super().__init__(agency, account, balance)
        self._limit = limit

    @property
    def limit(self):
        return self._limit

    def withdraw(self, value):
        if (self.balance + self.limit) < value:
            print('Your balance is negative')
            return

        self.balance -= value
        self.details()
