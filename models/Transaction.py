class Transaction:
    _next_id = 1

    def __init__(self, transaction_type, amount):
        self._transaction_id = Transaction._next_id
        Transaction._next_id += 1

        self._transaction_type = transaction_type
        self._amount = amount

    @property
    def transaction_id(self):
        return self._transaction_id

    @property
    def transaction_type(self):
        return self._transaction_type

    @property
    def amount(self):
        return self._amount

    def __str__(self):
        return f"Transaction {self._transaction_id} | {self._transaction_type} | {self._amount}"