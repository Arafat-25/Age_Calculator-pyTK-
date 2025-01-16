import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Function to calculate age
def calculate_age():
    try:
        dob = dob_entry.get()
        dob_date = datetime.strptime(dob, "%Y-%m-%d")
        today = datetime.now()
        age_years = today.year - dob_date.year
        if today.month < dob_date.month or (today.month == dob_date.month and today.day < dob_date.day):
            age_years -= 1
        result_label.config(text=f"Your Age: {age_years} years")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter the date in YYYY-MM-DD format.")

# Create the main window
root = tk.Tk()
root.title("Age Calculator")
root.geometry("300x200")

# Widgets
title_label = tk.Label(root, text="Age Calculator", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

dob_label = tk.Label(root, text="Enter Date of Birth (YYYY-MM-DD):", font=("Arial", 12))
dob_label.pack()

dob_entry = tk.Entry(root, font=("Arial", 12))
dob_entry.pack(pady=5)

calculate_button = tk.Button(root, text="Calculate Age", font=("Arial", 12), command=calculate_age)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14), fg="green")
result_label.pack(pady=10)

# Run the application
root.mainloop()



