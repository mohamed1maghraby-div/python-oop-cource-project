# from helpers.file_helper import (
#     insert_data,
#     get_all_data,
#     get_one_by_key,
#     update_data,
#     delete_data
# )

# # =========================
# # Insert Data
# # =========================

# new_customer = {
#     "name": "Ali",
#     "national_id": "123",
#     "phone": "01000000000"
# }

# insert_data("data/customers.txt", new_customer)

# # =========================
# # Get All Data
# # =========================

# customers = get_all_data("data/customers.txt")

# for customer in customers:
#     print(customer["name"], customer["phone"])


# # =========================
# # Find By Column
# # =========================

# customer = get_one_by_key("data/customers.txt", "national_id", "123" )

# if customer:
#     print("Found:", customer)
# else:
#     print("Customer not found")


# # =========================
# # Find data By Column & Update Data 
# # =========================

# updated_customer = {
#     "name": "Ali Ahmed",
#     "national_id": "123",
#     "phone": "01111111111"
# }

# update_data("data/customers.txt", "national_id", "123", updated_customer )

# # =========================
# # Find data By Column & Delete Data 
# # =========================

# delete_data( "data/customers.txt", "national_id", "123" )


import tkinter as tk
from gui.main_window import BankGUI

root = tk.Tk()
app = BankGUI(root)
root.mainloop()