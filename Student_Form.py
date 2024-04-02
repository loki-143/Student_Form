# Importing necessary packages

import tkinter as tk
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table
import time


# List to store multiple entries and store timestamp for pdf name
entries = []
timestamp = time.strftime("%Y%m%d%H%M%S")

# Function for Validating the Data Entered
def validate_data():
    name = name_entry.get().strip()
    aicte_id = aicte_id_entry.get().strip()
    email = email_entry.get().strip()
    phone_no = phone_no_entry.get().strip()
    college_name = college_name_entry.get().strip()

    if not name:
        messagebox.showerror("Error", "Name is required")
        return False
    if not aicte_id:
        messagebox.showerror("Error", "AICTE id is required")
        return False
    if not email:
        messagebox.showerror("Error", "Email is required")
        return False
    if not phone_no:
        messagebox.showerror("Error", "Phone number is required")
        return False
    if not college_name:
        messagebox.showerror("Error", "College name is required")
        return False

    if not validate_email(email):
        messagebox.showerror("Error", "Invalid email format")
        return False

    if not validate_phone(phone_no):
        messagebox.showerror("Error", "Invalid phone number format")
        return False

    return True

def validate_email(email):
    import re
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email)

def validate_phone(phone):
    import re
    pattern = r"^\d{10}$"  # Assuming 10-digit phone number
    return re.match(pattern, phone)

# Function for Generating pdf file
def generate_pdf():
    if validate_data():
        append_data()
        # Generate a unique filename with timestamp
        filename = f"candidate_data_{timestamp}.pdf"
        # Include all entries in the PDF
        data = [["Name", "AICTE ID", "Email", "Phone No.", "College Name"]] + entries

        doc = SimpleDocTemplate(filename, pagesize=letter)
        table = Table(data)
        doc.build([table])
        messagebox.showinfo("Success", "PDF generated successfully")


# Confirmation for Generating pdf file
def confirm_generate_pdf():
    confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to generate PDF?")
    if confirmation:
        generate_pdf()

#Function for Clearing fields for entering new data
def clear_fields():
    name_entry.delete(0, tk.END)
    aicte_id_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_no_entry.delete(0, tk.END)
    college_name_entry.delete(0, tk.END)

#Function Appends list each time while entering new data
def append_data():
    name = name_entry.get().strip()
    aicte_id = aicte_id_entry.get().strip()
    email = email_entry.get().strip()
    phone_no = phone_no_entry.get().strip()
    college_name = college_name_entry.get().strip()

    # Add current entry to the list
    entries.append([name, aicte_id, email, phone_no, college_name])

# Function for Entering new person data
def enter_another_person_data():
    append_data()
    clear_fields()

# Function for Opening pdf file
def open_pdf():
    import os
    import webbrowser
    filepath = os.path.abspath(f"candidate_data_{timestamp}.pdf")
    webbrowser.open_new(filepath)

# Function for Closing the application
def close_application():
    app.destroy()

# Creating tkinter application root window
app = tk.Tk()
app.title("Candidate Data Input")

# Container for the input fields
input_container = tk.Frame(app, bg="white")
input_container.grid(row=0, column=0, padx=10, pady=10)

# Input fields
name_label = tk.Label(input_container, text="Name", font=("Helvetica", 14, "bold"), bg="white")
name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
name_entry = tk.Entry(input_container, font=("Helvetica", 12), width=30, borderwidth=2, relief="solid")
name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

aicte_id_label = tk.Label(input_container, text="AICTE ID", font=("Helvetica", 14, "bold"), bg="white")
aicte_id_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
aicte_id_entry = tk.Entry(input_container, font=("Helvetica", 12), width=30, borderwidth=2, relief="solid")
aicte_id_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

email_label = tk.Label(input_container, text="Email", font=("Helvetica", 14, "bold"), bg="white")
email_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
email_entry = tk.Entry(input_container, font=("Helvetica", 12), width=30, borderwidth=2, relief="solid")
email_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

phone_no_label = tk.Label(input_container, text="Phone No.", font=("Helvetica", 14, "bold"), bg="white")
phone_no_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
phone_no_entry = tk.Entry(input_container, font=("Helvetica", 12), width=30, borderwidth=2, relief="solid")
phone_no_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

college_name_label = tk.Label(input_container, text="College Name", font=("Helvetica", 14, "bold"), bg="white")
college_name_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
college_name_entry = tk.Entry(input_container, font=("Helvetica", 12), width=30, borderwidth=2, relief="solid")
college_name_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")

# Clear button
clear_button = tk.Button(input_container, text="Clear", font=("Helvetica", 14, "bold"), bg="white",
                         fg="blue", borderwidth=3, command=clear_fields)
clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=(10, 0))

# Buttons
submit_button = tk.Button(input_container, text="Generate PDF", font=("Helvetica", 14, "bold"),
                          bg="white", fg="green", borderwidth=3, command=confirm_generate_pdf)
submit_button.grid(row=6, column=0, padx=5, pady=20, sticky="w")
another_person_button = tk.Button(input_container, text="Enter Another Person Data",
                                   font=("Helvetica", 14, "bold"), bg="white", fg="orange",
                                   borderwidth=3, command=enter_another_person_data)
another_person_button.grid(row=6, column=1, padx=5, pady=20, sticky="w")

open_pdf_button = tk.Button(input_container, text="Open PDF", font=("Helvetica", 14, "bold"),
                            bg="white", fg="blue", borderwidth=3, command=open_pdf)
open_pdf_button.grid(row=7, column=0, padx=5, pady=10, sticky="w")

close_button = tk.Button(input_container, text="Close", font=("Helvetica", 14, "bold"),
                         bg="white", fg="red", borderwidth=3, command=close_application)
close_button.grid(row=7, column=1, padx=100, pady=10, sticky="w")

app.mainloop()
