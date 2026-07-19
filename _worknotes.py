import tkinter as tk
from tkinter import ttk

def on_check(row_index):
    """Callback when a checkbox is toggled."""
    state = check_vars[row_index].get()
    print(f"Row {row_index + 1} checked: {bool(state)}")

# Sample data for rows
data = [
    ("Apple", 10, "$1.20"),
    ("Banana", 5, "$0.50"),
    ("Cherry", 20, "$2.00"),
]

root = tk.Tk()
root.title("Rows with Checkmarks")

# Create table headers
headers = ["Item", "Quantity", "Price", "Select"]
for col, text in enumerate(headers):
    ttk.Label(root, text=text, font=("Arial", 10, "bold")).grid(row=0, column=col, padx=5, pady=5)

check_vars = []  # Store IntVar for each checkbox

# Create rows
for row_index, (item, qty, price) in enumerate(data, start=1):
    ttk.Label(root, text=item).grid(row=row_index, column=0, padx=5, pady=2)
    ttk.Label(root, text=qty).grid(row=row_index, column=1, padx=5, pady=2)
    ttk.Label(root, text=price).grid(row=row_index, column=2, padx=5, pady=2)

    var = tk.IntVar(value=0)  # 0 = unchecked, 1 = checked
    check_vars.append(var)
    cb = ttk.Checkbutton(root, variable=var, command=lambda i=row_index-1: on_check(i))
    cb.grid(row=row_index, column=3, padx=5, pady=2)

root.mainloop()