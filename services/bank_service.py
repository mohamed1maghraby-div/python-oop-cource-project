from helpers.file_helper import *
from models.customer import Customer
from models.Account import Account

CUSTOMER_FILE = "data/customers.txt"
ACCOUNT_FILE = "data/accounts.txt"

class BankService:

    # --------------------
    # Customers
    # --------------------
    def add_customer(self, id, name, age, country, gaverment, gender, job):

        if get_one_by_key(CUSTOMER_FILE, "id", id):
            raise ValueError("Customer ID already exists")

        customer = Customer(id, name, age, country, gaverment, gender, job)
        insert_data(CUSTOMER_FILE, customer.to_dict())

    def get_customers(self):
        return [Customer.from_dict(c) for c in get_all_data(CUSTOMER_FILE)]

    # --------------------
    # Accounts
    # --------------------
    def create_account(self, account_number, customer_id):

        if get_one_by_key(ACCOUNT_FILE, "account_number", account_number):
            raise ValueError("Account already exists")

        account = Account(account_number)

        insert_data(ACCOUNT_FILE, {
            "account_number": account.account_number,
            "customer_id": customer_id,
            "balance": account.balance
        })

        customer_data = get_one_by_key(CUSTOMER_FILE, "id", customer_id)
        customer = Customer.from_dict(customer_data)

        customer.add_account(account_number)

        update_data(CUSTOMER_FILE, "id", customer_id, customer.to_dict())

    # --------------------
    # Deposit
    # --------------------

    def deposit(self, account_number, amount):

        data = get_one_by_key(ACCOUNT_FILE, "account_number", account_number)
        account = Account(account_number)
        account._balance = float(data["balance"])

        account.deposit(float(amount))

        update_data(ACCOUNT_FILE, "account_number", account_number, {
            "account_number": account.account_number,
            "customer_id": data["customer_id"],
            "balance": account.balance
        })

    # --------------------
    # Withdraw
    # --------------------

    def withdraw(self, account_number, amount):

        data = get_one_by_key(ACCOUNT_FILE, "account_number", account_number)
        account = Account(account_number)
        account._balance = float(data["balance"])

        account.withdraw(float(amount))

        update_data(ACCOUNT_FILE, "account_number", account_number, {
            "account_number": account.account_number,
            "customer_id": data["customer_id"],
            "balance": account.balance
        })

    # --------------------
    # Transfer
    # --------------------
    
    def transfer(self, from_account_number, to_account_number, amount):

        if from_account_number == to_account_number:
            raise ValueError("Cannot transfer to same account")

        from_data = get_one_by_key(ACCOUNT_FILE, "account_number", from_account_number)
        to_data = get_one_by_key(ACCOUNT_FILE, "account_number", to_account_number)

        if not from_data:
            raise ValueError("Sender account not found")

        if not to_data:
            raise ValueError("Receiver account not found")

        # Create account objects
        from_account = Account(from_account_number)
        to_account = Account(to_account_number)

        from_account._balance = float(from_data["balance"])
        to_account._balance = float(to_data["balance"])

        # Perform transfer using your Account logic
        from_account.transfer(to_account, float(amount))

        # Update sender
        update_data(ACCOUNT_FILE, "account_number", from_account_number, {
            "account_number": from_account.account_number,
            "customer_id": from_data["customer_id"],
            "balance": from_account.balance
        })

        # Update receiver
        update_data(ACCOUNT_FILE, "account_number", to_account_number, {
            "account_number": to_account.account_number,
            "customer_id": to_data["customer_id"],
            "balance": to_account.balance
        })

    # --------------------
    # View
    # --------------------
    def get_customers_with_accounts(self):

        customers = self.get_customers()
        accounts_data = get_all_data(ACCOUNT_FILE)

        result = []

        for cust in customers:
            info = {
                "name": cust.get_name(),
                "id": cust.get_id(),
                "accounts": []
            }

            for acc_num in cust.get_accounts():
                acc_data = next(
                    (a for a in accounts_data if a["account_number"] == acc_num),
                    None
                )

                if acc_data:
                    info["accounts"].append(
                        (acc_data["account_number"], acc_data["balance"])
                    )

            result.append(info)

        return result