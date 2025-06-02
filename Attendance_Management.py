import tkinter as tk
from tkinter import ttk, messagebox
import csv
from datetime import datetime

# Global student list
students = ["John", "Mary", "Sam", "Alice", "Bob"]
attendance_data = {}

def mark_attendance(student, status):
    attendance_data[student] = status

def export_attendance():
    if not attendance_data:
        messagebox.showwarning("Export Failed", "No attendance data to export.")
        return

    date_str = datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename = f"Attendance_{date_str}.csv"

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Student Name", "Status", "Date"])
        for student, status in attendance_data.items():
            writer.writerow([student, status, datetime.now().strftime("%Y-%m-%d")])

    messagebox.showinfo("Export Successful", f"Attendance saved to {filename}")

def clear_attendance():
    attendance_data.clear()
    for var in status_vars:
        var.set("None")
    messagebox.showinfo("Clear", "Attendance data cleared successfully.")

def add_student():
    new_name = entry_new_student.get().strip()
    if new_name:
        if new_name in students:
            messagebox.showwarning("Duplicate", "Student already exists.")
        else:
            students.append(new_name)
            entry_new_student.delete(0, tk.END)
            refresh_table()
            messagebox.showinfo("Success", f"Student '{new_name}' added successfully.")

def refresh_table():
    for widget in frame_students.winfo_children()[1:]:  # Skip header
        widget.destroy()

    status_vars.clear()

    for i, student in enumerate(students):
        row_frame = tk.Frame(frame_students, bg="white")
        row_frame.pack(fill="x", pady=1)
        
        tk.Label(
            row_frame,
            text=student,
            font=("Helvetica", 10),
            bg="white",
            width=30
        ).pack(side="left", pady=5)

        var = tk.StringVar(value="None")
        status_vars.append(var)

        combo = ttk.Combobox(
            row_frame,
            textvariable=var,
            values=["Present", "Absent"],
            width=15,
            state="readonly"
        )
        combo.pack(side="left", pady=5)

def submit_attendance():
    empty_status = False
    for var in status_vars:
        if var.get() == "None":
            empty_status = True
            break
    
    if empty_status:
        messagebox.showwarning("Warning", "Please mark attendance for all students.")
        return

    for i, student in enumerate(students):
        mark_attendance(student, status_vars[i].get())

    messagebox.showinfo("Success", "Attendance marked successfully.")

# GUI Setup
root = tk.Tk()
root.title("Attendance Management System")
root.geometry("800x900")
root.configure(bg="#f0f0f0")

# Style configuration
style = ttk.Style()
style.configure("Header.TLabel", font=("Helvetica", 24, "bold"), background="#f0f0f0")
style.configure("SubHeader.TLabel", font=("Helvetica", 12), background="#f0f0f0")
style.configure("Custom.TCombobox", background="#ffffff")

# Title with better styling
title_frame = tk.Frame(root, bg="#1976D2", pady=20)
title_frame.pack(fill="x")
tk.Label(
    title_frame,
    text="Attendance Management System",
    font=("Helvetica", 24, "bold"),
    fg="white",
    bg="#1976D2"
).pack()

# Container frame
container = tk.Frame(root, bg="#f0f0f0", padx=40, pady=20)
container.pack(fill="both", expand=True)

# Student list frame
frame_students = tk.Frame(container, bg="white", relief="solid", borderwidth=1)
frame_students.pack(fill="x", padx=20, pady=10)

# Header for student list
header_frame = tk.Frame(frame_students, bg="#E3F2FD")
header_frame.pack(fill="x")
tk.Label(
    header_frame,
    text="Student Name",
    font=("Helvetica", 11, "bold"),
    bg="#E3F2FD",
    width=30
).pack(side="left", pady=10)
tk.Label(
    header_frame,
    text="Status",
    font=("Helvetica", 11, "bold"),
    bg="#E3F2FD",
    width=20
).pack(side="left", pady=10)

# Input section
input_frame = tk.Frame(container, bg="#f0f0f0", pady=20)
input_frame.pack(fill="x")

tk.Label(
    input_frame,
    text="Add New Student",
    font=("Helvetica", 12, "bold"),
    bg="#f0f0f0"
).pack()

entry_new_student = tk.Entry(
    input_frame,
    font=("Helvetica", 10),
    width=30
)
entry_new_student.pack(pady=10)

# Buttons
button_frame = tk.Frame(container, bg="#f0f0f0")
button_frame.pack(pady=20)

tk.Button(
    button_frame,
    text="Add Student",
    command=add_student,
    bg="#4CAF50",
    fg="white",
    font=("Helvetica", 10),
    width=15,
    relief="flat"
).pack(side="left", padx=5)

tk.Button(
    button_frame,
    text="Submit Attendance",
    command=submit_attendance,
    bg="#1976D2",
    fg="white",
    font=("Helvetica", 10),
    width=15,
    relief="flat"
).pack(side="left", padx=5)

tk.Button(
    button_frame,
    text="Export to CSV",
    command=export_attendance,
    bg="#FFC107",
    fg="black",
    font=("Helvetica", 10),
    width=15,
    relief="flat"
).pack(side="left", padx=5)

tk.Button(
    button_frame,
    text="Clear",
    command=clear_attendance,
    bg="#f44336",
    fg="white",
    font=("Helvetica", 10),
    width=15,
    relief="flat"
).pack(side="left", padx=5)

tk.Button(
    button_frame,
    text="Exit",
    command=root.quit,
    bg="#757575",
    fg="white",
    font=("Helvetica", 10),
    width=15,
    relief="flat"
).pack(side="left", padx=5)

status_vars = []
refresh_table()

root.mainloop()