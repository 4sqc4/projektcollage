from bank_account import BankAccount
from exceptions import InsufficientFundsError

class PremiumAccount(BankAccount):
    def __init__(self, owner_name, balance, overdraft_limit=50000):
        super().__init__(owner_name, balance)
        self.overdraft_limit = overdraft_limit
        self.fee = 500

    def withdraw(self, amount):
        self._check_status()

        if amount > (self._balance + self.overdraft_limit):
            raise InsufficientFundsError("Превышен лимит овердрафта")
        self._balance -= amount
