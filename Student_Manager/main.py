
import tkinter as tk
from tkinter import messagebox, simpledialog
import os

students = []

# File location
file_name = os.path.join(os.path.dirname(__file__), "studentMarks.txt")


# Load the students from the txt file
def load():
    students.clear()

    try:
        file = open(file_name, "r")
        lines = file.readlines()
        file.close()

        for line in lines[1:]:
            data = line.strip().split(",")

            students.append([
                data[0],
                data[1],
                int(data[2]),
                int(data[3]),
                int(data[4]),
                int(data[5])
            ])

    except:
        messagebox.showerror("Error", "Cannot open studentMarks.txt")


# Save students into the file
def save():
    file = open(file_name, "w")

    file.write(str(len(students)) + "\n")

    for s in students:
        file.write(
            s[0] + "," + s[1] + "," +
            str(s[2]) + "," +
            str(s[3]) + "," +
            str(s[4]) + "," +
            str(s[5]) + "\n"
        )

    file.close()


# Calculates percentage
def percentage(s):
    total = s[2] + s[3] + s[4] + s[5]
    return total / 160 * 100


# Calculate the grades of students
def grade(s):
    mark = percentage(s)

    if mark >= 70:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 50:
        return "C"
    elif mark >= 40:
        return "D"
    else:
        return "F"


# Display students w/ grades etc
def display(s):
    coursework = s[2] + s[3] + s[4]

    output.insert("end", "Name: " + s[1] + "\n")
    output.insert("end", "Student Number: " + s[0] + "\n")
    output.insert("end", "Coursework: " + str(coursework) + "/60\n")
    output.insert("end", "Exam Mark: " + str(s[5]) + "/100\n")
    output.insert("end", "Overall Percentage: " + str(round(percentage(s), 2)) + "%\n")
    output.insert("end", "Grade: " + grade(s) + "\n")
    output.insert("end", "------------------------------\n\n")


# Clear output
def clear():
    output.delete("1.0", "end")


# View all students
def view_all():
    clear()

    average = 0

    for s in students:
        display(s)
        average = average + percentage(s)

    if len(students) > 0:
        average = average / len(students)

    output.insert("end", "\nCLASS SUMMARY\n")
    output.insert("end", "Number of students: " + str(len(students)) + "\n")
    output.insert("end", "Class average: " + str(round(average, 2)) + "%")


# View individual student
def view_one():
    code = simpledialog.askstring("Search", "Enter student number:")

    if code == None:
        return

    clear()
    found = False

    for s in students:
        if s[0] == code:
            display(s)
            found = True

    if found == False:
        messagebox.showinfo("Error", "Student not found!")


# Highest mark
def highest():
    if len(students) == 0:
        messagebox.showinfo("Error", "No students available!")
        return

    best = students[0]

    for s in students:
        if percentage(s) > percentage(best):
            best = s

    clear()
    output.insert("end", "HIGHEST STUDENT\n\n")
    display(best)


# Lowest mark
def lowest():
    if len(students) == 0:
        messagebox.showinfo("Error", "No students available!")
        return

    worst = students[0]

    for s in students:
        if percentage(s) < percentage(worst):
            worst = s

    clear()
    output.insert("end", "LOWEST STUDENT\n\n")
    display(worst)


# Sort students
def sort_students():
    if len(students) == 0:
        messagebox.showinfo("Error", "No students available!")
        return

    choice = simpledialog.askstring(
        "Sort Students",
        "Enter A for Ascending or D for Descending:"
    )

    if choice == None:
        return

    if choice.upper() != "A" and choice.upper() != "D":
        messagebox.showerror("Error", "Please enter A or D!")
        return

    for i in range(len(students)):
        for j in range(i + 1, len(students)):

            if choice.upper() == "A":
                if percentage(students[i]) > percentage(students[j]):
                    temp = students[i]
                    students[i] = students[j]
                    students[j] = temp

            else:
                if percentage(students[i]) < percentage(students[j]):
                    temp = students[i]
                    students[i] = students[j]
                    students[j] = temp

    view_all()


# Adds student
def add_student():
    code = simpledialog.askstring("Add Student", "Enter student number:")

    if code == None:
        return

    if len(code) != 4 or not code.isdigit():
        messagebox.showerror("Error", "Student number must be 4 digits!")
        return

    for s in students:
        if s[0] == code:
            messagebox.showerror("Error", "Student already exists!")
            return

    name = simpledialog.askstring("Add Student", "Enter student name:")

    if name == None or name.strip() == "":
        return

    mark1 = simpledialog.askinteger("Add Student", "Course mark 1 (0-20):")
    mark2 = simpledialog.askinteger("Add Student", "Course mark 2 (0-20):")
    mark3 = simpledialog.askinteger("Add Student", "Course mark 3 (0-20):")
    exam = simpledialog.askinteger("Add Student", "Exam mark (0-100):")

    if mark1 == None or mark2 == None or mark3 == None or exam == None:
        return

    if mark1 < 0 or mark1 > 20:
        messagebox.showerror("Error", "Invalid course mark!")
        return

    if mark2 < 0 or mark2 > 20:
        messagebox.showerror("Error", "Invalid course mark!")
        return

    if mark3 < 0 or mark3 > 20:
        messagebox.showerror("Error", "Invalid course mark!")
        return

    if exam < 0 or exam > 100:
        messagebox.showerror("Error", "Invalid exam mark!")
        return

    students.append([code, name, mark1, mark2, mark3, exam])

    save()

    messagebox.showinfo("Success", "Student added successfully!")


# Removes student
def delete_student():
    code = simpledialog.askstring("Delete Student", "Enter student number:")

    if code == None:
        return

    for s in students:
        if s[0] == code:
            students.remove(s)
            save()

            messagebox.showinfo("Success", "Student deleted!")
            return

    messagebox.showerror("Error", "Student not found!")


# Updates student
def update_student():
    code = simpledialog.askstring("Update Student", "Enter student number:")

    if code == None:
        return

    for s in students:
        if s[0] == code:

            name = simpledialog.askstring(
                "Update Student", "Enter new name:", initialvalue=s[1]
            )

            if name == None or name.strip() == "":
                return

            mark1 = simpledialog.askinteger(
                "Update Student", "Course mark 1:", initialvalue=s[2]
            )

            mark2 = simpledialog.askinteger(
                "Update Student", "Course mark 2:", initialvalue=s[3]
            )

            mark3 = simpledialog.askinteger(
                "Update Student", "Course mark 3:", initialvalue=s[4]
            )

            exam = simpledialog.askinteger(
                "Update Student", "Exam mark:", initialvalue=s[5]
            )

            if mark1 == None or mark2 == None or mark3 == None or exam == None:
                return

            if mark1 < 0 or mark1 > 20 or mark2 < 0 or mark2 > 20:
                messagebox.showerror("Error", "Invalid coursework marks!")
                return

            if mark3 < 0 or mark3 > 20 or exam < 0 or exam > 100:
                messagebox.showerror("Error", "Invalid marks!")
                return

            s[1] = name
            s[2] = mark1
            s[3] = mark2
            s[4] = mark3
            s[5] = exam

            save()

            messagebox.showinfo("Success", "Student updated!")
            return

    messagebox.showerror("Error", "Student not found!")


# Main window
root = tk.Tk()
root.title("Student Manager")
root.geometry("750x650")

# Title
title = tk.Label(
    root,
    text="STUDENT MANAGER",
    font=("Arial", 20, "bold")
)
title.pack(pady=10)


# Menu buttons
tk.Button(root, text="1. View All Students", width=30, command=view_all).pack(pady=3)

tk.Button(root, text="2. View Individual Student", width=30, command=view_one).pack(pady=3)

tk.Button(root, text="3. Highest Mark", width=30, command=highest).pack(pady=3)

tk.Button(root, text="4. Lowest Mark", width=30, command=lowest).pack(pady=3)

tk.Button(root, text="5. Sort Students", width=30, command=sort_students).pack(pady=3)

tk.Button(root, text="6. Add Student", width=30, command=add_student).pack(pady=3)

tk.Button(root, text="7. Delete Student", width=30, command=delete_student).pack(pady=3)

tk.Button(root, text="8. Update Student", width=30, command=update_student).pack(pady=3)



output = tk.Text(root, height=15, width=85)
output.pack(pady=15)



load()

root.mainloop()