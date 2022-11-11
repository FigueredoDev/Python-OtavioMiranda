from account import Account


class AccountSavings(Account):
    def withdraw(self, value):
        if self.balance < value:
            print('Your balance is negative')
            return

        self.balance -= value
        self.details()
