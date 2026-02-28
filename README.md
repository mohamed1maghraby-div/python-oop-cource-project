Bank Management System <br><br>
OOP Desktop Application using Python & Tkinter <br><br>

📌 Overview <br>

Bank Management System is a desktop application built using Python and Tkinter GUI.
The system simulates a real-world banking environment and demonstrates the implementation of core Object-Oriented Programming (OOP) principles. <br><br>

This project was developed as part of an OOP course to apply theoretical concepts in a practical. <br><br>


🎯 Features<br><br>
✅ Add New Customer<br>
✅ Create Bank Account<br>
✅ Deposit Money<br>
✅ Withdraw Money<br>
✅ Transfer Between Accounts<br>
✅ View Customers with Account Details<br>
✅ Savings Account (Interest Support)<br>
✅ Current Account (Overdraft Support)<br>
✅ File-Based Data Persistence (TXT Storage)<br><br>

🧠 OOP Principles Applied<br><br>
🔒 Encapsulation<br>
Private attributes (_balance, _id, etc.)<br>
Controlled access via getter methods<br>
Transactions handled internally within Account<br><br>

🧬 Inheritance<br>
Customer inherits from Person<br>
SavingsAccount and CurrentAccount inherit from Account<br><br>

🔁 Polymorphism<br>
withdraw() method overridden in CurrentAccount<br>
Same method behaves differently depending on account type<br><br>

🎭 Abstraction<br>
GUI interacts only with BankService<br>
Business logic separated from UI<br>
File operations handled via helper functions<br><br>

🏗️ System Architecture<br>
GUI (Tkinter)<br>
        ↓<br>
BankService<br>
        ↓<br>
Models (Customer / Account / etc.)<br>
        ↓<br>
File Helpers<br>
        ↓<br>
TXT Storage<br><br>

📁 Project Structure<br>
bank_system/<br>
│<br>
├── main.py<br>
│<br>
├── models/<br>
│   ├── person.py<br>
│   ├── customer.py<br>
│   ├── Account.py<br>
│   ├── SavingsAccount.py<br>
│   ├── CurrentAccount.py<br>
│   └── Transaction.py<br>
│<br>
├── services/<br>
│   └── bank_service.py<br>
│<br>
├── helpers/<br>
│   └── file_helper.py<br>
│<br>
└── data/<br>
    ├── customers.txt<br>
    └── accounts.txt<br><br>

💾 Data Storage<br>
The system uses TXT files for data persistence.<br><br>

Example: customers.txt<br>
id=1;name=Ahmed;age=30;country=Egypt;...<br>
Example: accounts.txt<br><br>

account_number=1001;customer_id=1;balance=500<br><br>

Helper functions used:<br>
insert_data()<br>
get_all_data()<br>
get_one_by_key()<br>
update_data()<br>


👨‍💻 Team Members & Responsibilities <br><br>
💳 Eng. Moamen<br>
Banking Logic Developer<br>
Implemented:<br>
Account<br>
SavingsAccount<br>
CurrentAccount<br>
Transaction<br>
Deposit / Withdraw / Transfer logic<br>
Interest calculation<br>
Overdraft handling<br>
Transaction auto-increment system<br><br>

👤 Eng. Mahmoud Ramadan<br>
Core System Developer<br>
Implemented:<br>
Person<br>
Customer<br>
BankService<br>
Customer-Account linking logic<br><br>

🖥️ Eng. Mohamed Maghraby<br>
GUI Developer<br>
Designed and implemented all Tkinter screens<br>
Connected GUI to business logic<br>
Input validation and user interaction handling<br>
Helpers Functions For Files Architecture<br><br>

🚀 How to Run<br>
1️⃣ Make sure Python is installed<br>
2️⃣ Run the project python main.py
