from classes.account_savings import AccountSavings
from classes.checking_account import AccountChecking

account = AccountSavings(111, 222, 0)
account.deposit(10)
account.withdraw(2)

print("##################")

account_check = AccountChecking(3333, 444, 0)
account_check.withdraw(500)
account_check.withdraw(1000)
