from models.Transaction import Transaction

class Account:
    def __init__(self, account_number):
        self._account_number = account_number
        self._balance = 0
        self._transactions = []

    @property
    def account_number(self):
        return self._account_number

    @property
    def balance(self):
        return self._balance

    @property
    def transactions(self):
        return self._transactions.copy()
        
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        self._balance += amount

        transaction = Transaction("deposit", amount)
        self._add_transaction(transaction)

        return self._balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self._balance:
            raise ValueError("Insufficient balance")

        self._balance -= amount

        transaction = Transaction("withdraw", amount)
        self._add_transaction(transaction)

        return self._balance

    def transfer(self, target_account, amount):
        if not isinstance(target_account, Account):
            raise TypeError("Target must be an Account")

        self.withdraw(amount)
        target_account.deposit(amount)

        transaction = Transaction(
            "transfer",
            amount
        )
        self._add_transaction(transaction)

    def _add_transaction(self, transaction):
        self._transactions.append(transaction)
