from models.Account import Account

class SavingsAccount(Account):
    def __init__(self, account_number, interest_rate):
        super().__init__(account_number)
        self._interest_rate = interest_rate

    
    @property
    def interest_rate(self):
        return self._interest_rate

    def calculate_interest(self):
        return self.balance * self._interest_rate

    def apply_interest(self):
        interest = self.calculate_interest()
        self.deposit(interest)   
        return interest