from models.person import Person
class Customer(Person):
    def __init__(self, id, name, age, country, gaverment, gender, job, accounts = None):
        super().__init__( id, name, age, country, gaverment, gender, job)
        self._accounts = accounts if accounts else []

    def add_account(self, account_number):
        return self._accounts.append(account_number)
    
    def get_accounts(self):
        return self._accounts
        
    def to_dict(self):
        data = super().to_dict()
        data["accounts"]=",".join(self._accounts)
        return data
