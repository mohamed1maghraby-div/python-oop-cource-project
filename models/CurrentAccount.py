from models.Account import Account
from models.Transaction import Transaction

class CurrentAccount(Account):
    def __init__(self, account_number, overdraft_limit):
        super().__init__(account_number)
        self._overdraft_limit = overdraft_limit

    
    @property
    def overdraft_limit(self):
        return self._overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self.balance + self._overdraft_limit:
            raise ValueError("Overdraft limit exceeded")

        self._balance -= amount

        transaction = Transaction("withdraw", amount)
        self._add_transaction(transaction)

        return self._balance
