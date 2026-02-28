Bank Management System
OOP Desktop Application using Python & Tkinter

📌 Overview

Bank Management System is a desktop application built using Python and Tkinter GUI.
The system simulates a real-world banking environment and demonstrates the implementation of core Object-Oriented Programming (OOP) principles.

This project was developed as part of an OOP course to apply theoretical concepts in a practical.

🎯 Features
✅ Add New Customer
✅ Create Bank Account
✅ Deposit Money
✅ Withdraw Money
✅ Transfer Between Accounts
✅ View Customers with Account Details
✅ Savings Account (Interest Support)
✅ Current Account (Overdraft Support)
✅ File-Based Data Persistence (TXT Storage)

🧠 OOP Principles Applied
🔒 Encapsulation
Private attributes (_balance, _id, etc.)
Controlled access via getter methods
Transactions handled internally within Account

🧬 Inheritance
Customer inherits from Person
SavingsAccount and CurrentAccount inherit from Account

🔁 Polymorphism
withdraw() method overridden in CurrentAccount
Same method behaves differently depending on account type

🎭 Abstraction
GUI interacts only with BankService
Business logic separated from UI
File operations handled via helper functions

🏗️ System Architecture
GUI (Tkinter)
        ↓
BankService
        ↓
Models (Customer / Account / etc.)
        ↓
File Helpers
        ↓
TXT Storage

📁 Project Structure
bank_system/
│
├── main.py
│
├── models/
│   ├── person.py
│   ├── customer.py
│   ├── Account.py
│   ├── SavingsAccount.py
│   ├── CurrentAccount.py
│   └── Transaction.py
│
├── services/
│   └── bank_service.py
│
├── helpers/
│   └── file_helper.py
│
└── data/
    ├── customers.txt
    └── accounts.txt

💾 Data Storage
The system uses TXT files for data persistence.

Example: customers.txt
id=1;name=Ahmed;age=30;country=Egypt;...
Example: accounts.txt
account_number=1001;customer_id=1;balance=500

Helper functions used:
insert_data()
get_all_data()
get_one_by_key()
update_data()

👨‍💻 Team Members & Responsibilities

💳 Eng. Moamen
Banking Logic Developer
Implemented:
Account
SavingsAccount
CurrentAccount
Transaction
Deposit / Withdraw / Transfer logic
Interest calculation
Overdraft handling
Transaction auto-increment system

👤 Eng. Mahmoud Ramadan
Core System Developer
Implemented:
Person
Customer
BankService
Customer-Account linking logic

🖥️ Eng. Mohamed Maghraby
GUI Developer
Designed and implemented all Tkinter screens
Connected GUI to business logic
Input validation and user interaction handling
Helpers Functions For Files Architecture

🚀 How to Run
1️⃣ Make sure Python is installed
2️⃣ Run the project python main.py
