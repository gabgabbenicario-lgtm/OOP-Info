import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog


def new_student():
    messagebox.showinfo(
        "New Student",
        "Create a new student record."
    )


def enter_student_name():
    name = simpledialog.askstring(
        "Student Name",
        "Enter student name:"
    )

    if name:
        messagebox.showinfo(
            "Student",
            f"Student Name: {name}"
        )


def open_file():
    filename = filedialog.askopenfilename(
        title="Select a File",
        filetypes=[
            ("Text Files", "*.txt"),
            ("Python Files", "*.py"),
            ("All Files", "*.*")
        ]
    )

    if filename:
        messagebox.showinfo(
            "File Selected",
            f"You selected:\n{filename}"
        )


def save_student():
    messagebox.showinfo(
        "Save",
        "Student record saved successfully."
    )


def exit_application():
    answer = messagebox.askyesno(
        "Exit",
        "Are you sure you want to exit?"
    )

    if answer:
        window.destroy()


def about_application():
    messagebox.showinfo(
        "About",
        "Student Information System\n\n"
        "Developed using Python Tkinter\n"
        "Object-Oriented Programming"
    )


#----------------------

#Main Window

#----------------------

window = tk.Tk()
window.title("Student Information System")
window.geometry("600x400")


#--------------------------

#Main Label

#-------------------------

title_label = tk.Label(
    window,
    text="Student information System",
    font=("Arial", 20, "bold")
)

title_label.pack(pady=50)


#-----------------------

#Menu Bar

#------------------
menu_bar=tk.Menu(window)
window.config(menu=menu_bar)

#-----------------------

#File Menu

#-------------------------

file_menu = tk.Menu(
    menu_bar,
    tearoff=0
)
file_menu.add_command(
    label="New",
    command=new_student
)

file_menu.add_command(
    label="Enter Student Name",
    command=enter_student_name
)
file_menu.add_command(
    label="Open",
    command=open_file
)
file_menu.add_command(
    label="Save",
    command=save_student
)
file_menu.add_separator()

file_menu.add_command(
    label="Exit",
    command=exit_application
)
menu_bar.add_cascade(
    label="File",
    menu=file_menu
)

#-------------------

#Help Menu

#--------------------

help_menu=tk.Menu(
    menu_bar,
    tearoff=0
)
help_menu.add_command(
    label="About",
    command=about_application
)
menu_bar.add_cascade(
    label="Help",
    menu=help_menu
)
#----------------
#Start Apllication
#----------------
window.mainloop()
