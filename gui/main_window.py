import tkinter as tk
from tkinter import ttk, messagebox
from services.bank_service import BankService


class BankGUI:
    # Color scheme
    PRIMARY_COLOR = "#2C3E50"
    SECONDARY_COLOR = "#3498DB"
    ACCENT_COLOR = "#E74C3C"
    BG_COLOR = "#ECF0F1"
    TEXT_COLOR = "#2C3E50"
    SUCCESS_COLOR = "#27AE60"
    
    FONT_TITLE = ("Segoe UI", 16, "bold")
    FONT_LABEL = ("Segoe UI", 10)
    FONT_BUTTON = ("Segoe UI", 10, "bold")

    def __init__(self, root):
        self.bank = BankService()
        self.root = root
        self.root.title("Bank System")
        self.root.geometry("700x750")
        self.root.configure(bg=self.BG_COLOR)
        self.root.resizable(False, False)
        
        # Center window on screen
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        
        self.main_menu()

    # -------------------------
    # Helpers
    # -------------------------
    def clear(self):
        for w in self.root.winfo_children():
            w.destroy()

    def create_header(self, text):
        """Create a styled header frame"""
        header = tk.Frame(self.root, bg=self.PRIMARY_COLOR, height=60)
        header.pack(fill=tk.X)
        
        label = tk.Label(header, text=text, font=self.FONT_TITLE, 
                        bg=self.PRIMARY_COLOR, fg="white")
        label.pack(pady=15)
        return header

    def create_button(self, parent, text, command, color=None, width=30):
        """Create a styled button"""
        if color is None:
            color = self.SECONDARY_COLOR
        
        btn = tk.Button(parent, text=text, command=command, 
                       font=self.FONT_BUTTON, width=width,
                       bg=color, fg="white", 
                       activebackground=color,
                       activeforeground="white",
                       relief=tk.FLAT, cursor="hand2",
                       padx=10, pady=8)
        return btn

    def create_entry_field(self, parent, label_text):
        """Create a styled entry field with label"""
        frame = tk.Frame(parent, bg=self.BG_COLOR)
        
        label = tk.Label(frame, text=label_text, font=self.FONT_LABEL, 
                        fg=self.TEXT_COLOR, bg=self.BG_COLOR)
        label.pack(anchor="w", padx=5, pady=(10, 3))
        
        entry = tk.Entry(frame, font=self.FONT_LABEL, width=45,
                        relief=tk.SOLID, borderwidth=1)
        entry.pack(padx=5, pady=(0, 5), fill=tk.X)
        
        return frame, entry

    # -------------------------
    # Main Menu
    # -------------------------
    def main_menu(self):
        self.clear()

        self.create_header("🏦 Bank System")

        # Main content frame
        content = tk.Frame(self.root, bg=self.BG_COLOR)
        content.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Button layout in grid for better organization
        buttons_info = [
            ("➕ Add Customer", self.add_customer),
            ("🏧 Create Account", self.create_account),
            ("💰 Deposit", self.deposit),
            ("🚀 Withdraw", self.withdraw),
            ("🔄 Transfer", self.transfer),
            ("👥 View Customers", self.view_customers),
        ]

        for i, (text, command) in enumerate(buttons_info):
            btn = self.create_button(content, text, command, width=40)
            btn.pack(fill=tk.X, pady=8)


    # -------------------------
    # Add Customer
    # -------------------------
    def add_customer(self):
        self.clear()

        self.create_header("➕ Add New Customer")

        # Create a scrollable frame for better form handling
        main_frame = tk.Frame(self.root, bg=self.BG_COLOR)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Canvas with scrollbar for forms that might exceed screen height
        canvas = tk.Canvas(main_frame, bg=self.BG_COLOR, highlightthickness=0)
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=self.BG_COLOR)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill=tk.BOTH, expand=True)
        scrollbar.pack(side="right", fill="y")

        # Form fields
        fields = ["ID", "Name", "Age", "Country", "Government", "Gender", "Job"]
        entries = {}

        for f in fields:
            frame, entry = self.create_entry_field(scrollable_frame, f)
            frame.pack(fill=tk.X, padx=20)
            entries[f] = entry

        # Button frame
        button_frame = tk.Frame(self.root, bg=self.BG_COLOR)
        button_frame.pack(fill=tk.X, padx=20, pady=15)

        def save():
            try:
                self.bank.add_customer(
                    entries["ID"].get(),
                    entries["Name"].get(),
                    int(entries["Age"].get()),
                    entries["Country"].get(),
                    entries["Government"].get(),
                    entries["Gender"].get(),
                    entries["Job"].get()
                )
                messagebox.showinfo("✓ Success", "Customer added successfully!")
                self.main_menu()

            except ValueError:
                messagebox.showerror("✗ Error", "Please enter valid age (number)")
            except Exception as e:
                messagebox.showerror("✗ Error", str(e))

        self.create_button(button_frame, "💾 Save", save, 
                          color=self.SUCCESS_COLOR).pack(side=tk.LEFT, padx=5)
        self.create_button(button_frame, "← Back", self.main_menu, 
                          color=self.SECONDARY_COLOR).pack(side=tk.LEFT, padx=5)

    # -------------------------
    # Create Account
    # -------------------------
    def create_account(self):
        self.clear()

        self.create_header("🏧 Create New Account")

        content = tk.Frame(self.root, bg=self.BG_COLOR)
        content.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        frame1, acc_entry = self.create_entry_field(content, "Account Number")
        frame1.pack(fill=tk.X)

        tk.Label(content, text="Customer ID", font=self.FONT_LABEL, 
                fg=self.TEXT_COLOR, bg=self.BG_COLOR).pack(anchor="w", padx=5, pady=(10, 3))

        customers = [c.get_id() for c in self.bank.get_customers()]
        combo = ttk.Combobox(content, values=customers, font=self.FONT_LABEL, 
                            width=42, state="readonly")
        combo.pack(padx=5, pady=(0, 5), fill=tk.X)

        button_frame = tk.Frame(self.root, bg=self.BG_COLOR)
        button_frame.pack(fill=tk.X, padx=20, pady=15)

        def create():
            try:
                self.bank.create_account(
                    acc_entry.get(),
                    combo.get()
                )
                messagebox.showinfo("✓ Success", "Account created successfully!")
                self.main_menu()

            except Exception as e:
                messagebox.showerror("✗ Error", str(e))

        self.create_button(button_frame, "✓ Create", create, 
                          color=self.SUCCESS_COLOR).pack(side=tk.LEFT, padx=5)
        self.create_button(button_frame, "← Back", self.main_menu, 
                          color=self.SECONDARY_COLOR).pack(side=tk.LEFT, padx=5)

    # -------------------------
    # Deposit
    # -------------------------
    def deposit(self):
        self.clear()

        self.create_header("💰 Deposit Money")

        content = tk.Frame(self.root, bg=self.BG_COLOR)
        content.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        frame1, acc_entry = self.create_entry_field(content, "Account Number")
        frame1.pack(fill=tk.X)

        frame2, amount_entry = self.create_entry_field(content, "Amount")
        frame2.pack(fill=tk.X)

        button_frame = tk.Frame(self.root, bg=self.BG_COLOR)
        button_frame.pack(fill=tk.X, padx=20, pady=15)

        def do_deposit():
            try:
                self.bank.deposit(
                    acc_entry.get(),
                    float(amount_entry.get())
                )
                messagebox.showinfo("✓ Success", "Deposit completed successfully!")
                self.main_menu()

            except ValueError:
                messagebox.showerror("✗ Error", "Please enter valid amount")
            except Exception as e:
                messagebox.showerror("✗ Error", str(e))

        self.create_button(button_frame, "✓ Deposit", do_deposit, 
                          color=self.SUCCESS_COLOR).pack(side=tk.LEFT, padx=5)
        self.create_button(button_frame, "← Back", self.main_menu, 
                          color=self.SECONDARY_COLOR).pack(side=tk.LEFT, padx=5)

    # -------------------------
    # Withdraw
    # -------------------------
    def withdraw(self):
        self.clear()

        self.create_header("🚀 Withdraw Money")

        content = tk.Frame(self.root, bg=self.BG_COLOR)
        content.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        frame1, acc_entry = self.create_entry_field(content, "Account Number")
        frame1.pack(fill=tk.X)

        frame2, amount_entry = self.create_entry_field(content, "Amount")
        frame2.pack(fill=tk.X)

        button_frame = tk.Frame(self.root, bg=self.BG_COLOR)
        button_frame.pack(fill=tk.X, padx=20, pady=15)

        def do_withdraw():
            try:
                self.bank.withdraw(
                    acc_entry.get(),
                    float(amount_entry.get())
                )
                messagebox.showinfo("✓ Success", "Withdrawal completed successfully!")
                self.main_menu()

            except ValueError:
                messagebox.showerror("✗ Error", "Please enter valid amount")
            except Exception as e:
                messagebox.showerror("✗ Error", str(e))

        self.create_button(button_frame, "✓ Withdraw", do_withdraw, 
                          color=self.SUCCESS_COLOR).pack(side=tk.LEFT, padx=5)
        self.create_button(button_frame, "← Back", self.main_menu, 
                          color=self.SECONDARY_COLOR).pack(side=tk.LEFT, padx=5)
        
    # -------------------------
    # Transfer
    # -------------------------
    def transfer(self):
        self.clear()

        self.create_header("🔄 Transfer Money")

        content = tk.Frame(self.root, bg=self.BG_COLOR)
        content.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        frame1, from_entry = self.create_entry_field(content, "From Account")
        frame1.pack(fill=tk.X)

        frame2, to_entry = self.create_entry_field(content, "To Account")
        frame2.pack(fill=tk.X)

        frame3, amount_entry = self.create_entry_field(content, "Amount")
        frame3.pack(fill=tk.X)

        button_frame = tk.Frame(self.root, bg=self.BG_COLOR)
        button_frame.pack(fill=tk.X, padx=20, pady=15)

        def do_transfer():
            try:
                self.bank.transfer(
                    from_entry.get(),
                    to_entry.get(),
                    float(amount_entry.get())
                )
                messagebox.showinfo("✓ Success", "Transfer completed successfully!")
                self.main_menu()

            except ValueError:
                messagebox.showerror("✗ Error", "Please enter valid amount")
            except Exception as e:
                messagebox.showerror("✗ Error", str(e))

        self.create_button(button_frame, "✓ Transfer", do_transfer, 
                          color=self.SUCCESS_COLOR).pack(side=tk.LEFT, padx=5)
        self.create_button(button_frame, "← Back", self.main_menu, 
                          color=self.SECONDARY_COLOR).pack(side=tk.LEFT, padx=5)

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