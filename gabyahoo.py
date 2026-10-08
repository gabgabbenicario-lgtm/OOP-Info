import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


# DATABASE
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        email TEXT NOT NULL,
        phone TEXT NOT NULL,
        city TEXT NOT NULL,
        age INTEGER NOT NULL,
        occupation TEXT NOT NULL
    )
""")

conn.commit()


# CREATE
def add_student():
    full_name = name_entry.get().strip()
    email = email_entry.get().strip()
    phone = phone_entry.get().strip()
    city = city_entry.get().strip()
    age = age_entry.get().strip()
    occupation = occupation_entry.get().strip()

    if (full_name == "" or email == "" or phone == "" or
            city == "" or age == "" or occupation == ""):
        messagebox.showwarning(
            "Warning",
            "Please fill in all fields."
        )
        return

    try:
        age = int(age)
    except ValueError:
        messagebox.showerror(
            "Error",
            "Age must be a number."
        )
        return

    # FIXED INSERT
    cursor.execute("""
        INSERT INTO students
        (full_name, email, phone, city, age, occupation)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (full_name, email, phone, city, age, occupation))

    conn.commit()

    messagebox.showinfo(
        "Success",
        "Student added successfully."
    )

    clear_fields()
    display_students()


# READ
def display_students():
    for item in tree.get_children():
        tree.delete(item)

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    for student in students:
        tree.insert("", tk.END, values=student)


# UPDATE
def update_student():
    selected = tree.selection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Please select a student to update."
        )
        return

    student_id = tree.item(selected[0])["values"][0]

    full_name = name_entry.get().strip()
    email = email_entry.get().strip()
    phone = phone_entry.get().strip()
    city = city_entry.get().strip()
    age = age_entry.get().strip()
    occupation = occupation_entry.get().strip()

    if (full_name == "" or email == "" or phone == "" or
            city == "" or age == "" or occupation == ""):
        messagebox.showwarning(
            "Warning",
            "Please fill in all fields."
        )
        return

    try:
        age = int(age)
    except ValueError:
        messagebox.showerror(
            "Error",
            "Age must be a number."
        )
        return

    cursor.execute("""
        UPDATE students
        SET full_name = ?,
            email = ?,
            phone = ?,
            city = ?,
            age = ?,
            occupation = ?
        WHERE id = ?
    """, (
        full_name,
        email,
        phone,
        city,
        age,
        occupation,
        student_id
    ))

    conn.commit()

    messagebox.showinfo(
        "Success",
        "Student updated successfully."
    )

    clear_fields()
    display_students()


# DELETE
def delete_student():
    selected = tree.selection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Please select a student to delete."
        )
        return

    student_id = tree.item(selected[0])["values"][0]

    confirm = messagebox.askyesno(
        "Confirm Delete",
        "Are you sure you want to delete this student?"
    )

    if confirm:
        cursor.execute(
            "DELETE FROM students WHERE id = ?",
            (student_id,)
        )

        conn.commit()

        messagebox.showinfo(
            "Success",
            "Student deleted successfully."
        )

        clear_fields()
        display_students()


# CLEAR
def clear_fields():
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    city_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    occupation_entry.delete(0, tk.END)


# SELECT STUDENT
def select_student(event):
    selected = tree.selection()

    if selected:
        student = tree.item(selected[0])["values"]

        clear_fields()

        name_entry.insert(0, student[1])
        email_entry.insert(0, student[2])
        phone_entry.insert(0, student[3])
        city_entry.insert(0, student[4])
        age_entry.insert(0, student[5])
        occupation_entry.insert(0, student[6])


# WINDOW
root = tk.Tk()
root.title("Student Management System")
root.geometry("1000x600")
root.configure(bg="#8deeee")


# COLORS
BG_COLOR = "#ababab"
TITLE_COLOR = "#000000"


# TITLE
title_label = tk.Label(
    root,
    text="Student Management System",
    font=("Arial", 18, "bold"),
    bg=BG_COLOR,
    fg=TITLE_COLOR
)

title_label.pack(pady=10)


# INPUT FRAME
input_frame = tk.Frame(root)
input_frame.pack(pady=10)


# FULL NAME
tk.Label(
    input_frame,
    text="Full Name:"
).grid(row=0, column=0, padx=5, pady=5)

name_entry = tk.Entry(input_frame, width=30)
name_entry.grid(row=0, column=1, padx=5, pady=5)


# EMAIL
tk.Label(
    input_frame,
    text="Email:"
).grid(row=1, column=0, padx=5, pady=5)

email_entry = tk.Entry(input_frame, width=30)
email_entry.grid(row=1, column=1, padx=5, pady=5)


# PHONE
tk.Label(
    input_frame,
    text="Phone:"
).grid(row=2, column=0, padx=5, pady=5)

phone_entry = tk.Entry(input_frame, width=30)
phone_entry.grid(row=2, column=1, padx=5, pady=5)


# CITY
tk.Label(
    input_frame,
    text="City:"
).grid(row=0, column=2, padx=5, pady=5)

city_entry = tk.Entry(input_frame, width=30)
city_entry.grid(row=0, column=3, padx=5, pady=5)


# AGE
tk.Label(
    input_frame,
    text="Age:"
).grid(row=1, column=2, padx=5, pady=5)

age_entry = tk.Entry(input_frame, width=30)
age_entry.grid(row=1, column=3, padx=5, pady=5)


# OCCUPATION
tk.Label(
    input_frame,
    text="Occupation:"
).grid(row=2, column=2, padx=5, pady=5)

occupation_entry = tk.Entry(input_frame, width=30)
occupation_entry.grid(row=2, column=3, padx=5, pady=5)


# BUTTONS
button_frame = tk.Frame(root)
button_frame.pack(pady=10)


tk.Button(
    button_frame,
    text="Add",
    width=10,
    command=add_student
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame,
    text="Update",
    width=10,
    command=update_student
).grid(row=0, column=1, padx=5)

tk.Button(
    button_frame,
    text="Delete",
    width=10,
    command=delete_student
).grid(row=0, column=2, padx=5)

tk.Button(
    button_frame,
    text="Clear",
    width=10,
    command=clear_fields
).grid(row=0, column=3, padx=5)


# TABLE
tree = ttk.Treeview(
    root,
    columns=(
        "ID",
        "Full Name",
        "Email",
        "Phone",
        "City",
        "Age",
        "Occupation"
    ),
    show="headings"
)

tree.heading("ID", text="ID")
tree.heading("Full Name", text="Full Name")
tree.heading("Email", text="Email")
tree.heading("Phone", text="Phone")
tree.heading("City", text="City")
tree.heading("Age", text="Age")
tree.heading("Occupation", text="Occupation")

tree.column("ID", width=40)
tree.column("Full Name", width=150)
tree.column("Email", width=180)
tree.column("Phone", width=110)
tree.column("City", width=100)
tree.column("Age", width=50)
tree.column("Occupation", width=120)

tree.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)


# SELECT EVENT
tree.bind("<ButtonRelease-1>", select_student)


# DISPLAY DATA
display_students()


# RUN
root.mainloop()
