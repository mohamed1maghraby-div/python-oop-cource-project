import tkinter as tk
from tkinter import ttk, messagebox
from services.bank_service import BankService


class BankGUI:

    def __init__(self, root):
        self.bank = BankService()
        self.root = root
        self.root.title("Bank System")
        self.root.geometry("600x600")
        self.main_menu()

    # -------------------------
    # Helpers
    # -------------------------
    def clear(self):
        for w in self.root.winfo_children():
            w.destroy()

    # -------------------------
    # Main Menu
    # -------------------------
    def main_menu(self):
        self.clear()

        tk.Label(self.root, text="Bank System", font=("Arial", 18)).pack(pady=20)

        tk.Button(self.root, text="Add Customer", width=25,
                  command=self.add_customer).pack(pady=5)

        tk.Button(self.root, text="Create Account", width=25,
                  command=self.create_account).pack(pady=5)

        tk.Button(self.root, text="Deposit", width=25,
                  command=self.deposit).pack(pady=5)

        tk.Button(self.root, text="Withdraw", width=25,
                  command=self.withdraw).pack(pady=5)
        
        tk.Button(self.root, text="Transfer", width=25,
          command=self.transfer).pack(pady=5)

        tk.Button(self.root, text="View Customers", width=25,
                  command=self.view_customers).pack(pady=5)

    # -------------------------
    # Add Customer
    # -------------------------
    def add_customer(self):
        self.clear()

        fields = ["ID", "Name", "Age", "Country", "Gaverment", "Gender", "Job"]

        entries = {}

        for f in fields:
            tk.Label(self.root, text=f).pack()
            e = tk.Entry(self.root, width=60)
            e.pack()
            entries[f] = e

        def save():
            try:
                self.bank.add_customer(
                    entries["ID"].get(),
                    entries["Name"].get(),
                    int(entries["Age"].get()),
                    entries["Country"].get(),
                    entries["Gaverment"].get(),
                    entries["Gender"].get(),
                    entries["Job"].get()
                )
                messagebox.showinfo("Success", "Customer Added")
                self.main_menu()

            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(self.root, text="Save", command=save).pack(pady=10)
        tk.Button(self.root, text="Back",
                  command=self.main_menu).pack()

    # -------------------------
    # Create Account
    # -------------------------
    def create_account(self):
        self.clear()

        tk.Label(self.root, text="Account Number").pack()
        acc_entry = tk.Entry(self.root)
        acc_entry.pack()

        tk.Label(self.root, text="Customer ID").pack()

        customers = [c.get_id() for c in self.bank.get_customers()]
        combo = ttk.Combobox(self.root, values=customers)
        combo.pack()

        def create():
            try:
                self.bank.create_account(
                    acc_entry.get(),
                    combo.get()
                )
                messagebox.showinfo("Success", "Account Created")
                self.main_menu()

            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(self.root, text="Create", command=create).pack(pady=10)
        tk.Button(self.root, text="Back",
                  command=self.main_menu).pack()

    # -------------------------
    # Deposit
    # -------------------------
    def deposit(self):
        self.clear()

        tk.Label(self.root, text="Account Number").pack()
        acc_entry = tk.Entry(self.root)
        acc_entry.pack()

        tk.Label(self.root, text="Amount").pack()
        amount_entry = tk.Entry(self.root)
        amount_entry.pack()

        def do_deposit():
            try:
                self.bank.deposit(
                    acc_entry.get(),
                    float(amount_entry.get())
                )
                messagebox.showinfo("Success", "Deposit Done")
                self.main_menu()

            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(self.root, text="Deposit",
                  command=do_deposit).pack(pady=10)

        tk.Button(self.root, text="Back",
                  command=self.main_menu).pack()

    # -------------------------
    # Withdraw
    # -------------------------
    def withdraw(self):
        self.clear()

        tk.Label(self.root, text="Account Number").pack()
        acc_entry = tk.Entry(self.root)
        acc_entry.pack()

        tk.Label(self.root, text="Amount").pack()
        amount_entry = tk.Entry(self.root)
        amount_entry.pack()

        def do_withdraw():
            try:
                self.bank.withdraw(
                    acc_entry.get(),
                    float(amount_entry.get())
                )
                messagebox.showinfo("Success", "Withdraw Done")
                self.main_menu()

            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(self.root, text="Withdraw",
                  command=do_withdraw).pack(pady=10)

        tk.Button(self.root, text="Back",
                  command=self.main_menu).pack()
        
    # -------------------------
    # Transfer
    # -------------------------
    def transfer(self):
        self.clear()

        tk.Label(self.root, text="From Account").pack()
        from_entry = tk.Entry(self.root)
        from_entry.pack()

        tk.Label(self.root, text="To Account").pack()
        to_entry = tk.Entry(self.root)
        to_entry.pack()

        tk.Label(self.root, text="Amount").pack()
        amount_entry = tk.Entry(self.root)
        amount_entry.pack()

        def do_transfer():
            try:
                self.bank.transfer(
                    from_entry.get(),
                    to_entry.get(),
                    float(amount_entry.get())
                )
                messagebox.showinfo("Success", "Transfer Completed")
                self.main_menu()

            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(self.root, text="Transfer",
                  command=do_transfer).pack(pady=10)

        tk.Button(self.root, text="Back",
                  command=self.main_menu).pack()

    # -------------------------
    # View Customers
    # -------------------------
    def view_customers(self):
        self.clear()

        data = self.bank.get_customers_with_accounts()

        for c in data:
            tk.Label(self.root,
                     text=f"{c['name']} (ID: {c['id']})",
                     font=("Arial", 12, "bold")).pack(pady=5)

            for acc in c["accounts"]:
                tk.Label(self.root,
                         text=f"   Account: {acc[0]} | Balance: {acc[1]}"
                         ).pack()

        tk.Button(self.root, text="Back",
                  command=self.main_menu).pack(pady=20)