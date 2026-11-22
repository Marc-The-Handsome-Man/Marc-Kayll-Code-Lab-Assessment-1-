
import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Arithmetic Quiz")
root.geometry("600x500")
root.resizable(False, False)
root.configure(bg="#234567")

score = 0
question = 0
attempt = 0
num1 = 0
num2 = 0
operation = ""
answer = 0
minimum = 0
maximum = 9

# Clears the screen
def clear():
    for widget in root.winfo_children():
        widget.destroy()


# Difficulty Menu
def displayMenu():
    clear()

    tk.Label(root, text="ARITHMETIC QUIZ",
             font=("Arial", 25, "bold"),
             bg="#234567", fg="white").pack(pady=30)

    tk.Label(root, text="DIFFICULTY LEVEL",
             font=("Arial", 18, "bold"),
             bg="#234567", fg="white").pack(pady=15)

    tk.Button(root, text="1. Easy", width=20,
              font=("Arial", 14),
              command=lambda: startQuiz(1)).pack(pady=10)

    tk.Button(root, text="2. Moderate", width=20,
              font=("Arial", 14),
              command=lambda: startQuiz(2)).pack(pady=10)

    tk.Button(root, text="3. Advanced", width=20,
              font=("Arial", 14),
              command=lambda: startQuiz(3)).pack(pady=10)


# Start The Quiz Here
def startQuiz(level):
    global minimum, maximum
    global score, question

    score = 0
    question = 0

    if level == 1:
        minimum = 0
        maximum = 9

    elif level == 2:
        minimum = 10
        maximum = 99

    else:
        minimum = 9999
        maximum = 999999

    nextQuestion()


# Random Number Generator
def randomInt():
    return random.randint(minimum, maximum)


# Random Operation
def decideOperation():
    return random.choice(["+", "-", "*"])


# Display Question
def displayProblem():
    global num1, num2, operation, answer, attempt
    global answer_entry, feedback

    clear()

    attempt = 1

    num1 = randomInt()
    num2 = randomInt()

    operation = decideOperation()

    if operation == "+":
        answer = num1 + num2
    else:
        if num1 < num2:
            temp = num1
            num1 = num2
            num2 = temp

        answer = num1 - num2

    tk.Label(root, text="ARITHMETIC QUIZ",
             font=("Arial", 22, "bold"),
             bg="#234567", fg="white").pack(pady=15)

    tk.Label(root, text="Question " + str(question) + " / 10",
             font=("Arial", 14),
             bg="#234567", fg="white").pack()

    tk.Label(root, text="Score: " + str(score),
             font=("Arial", 14),
             bg="#234567", fg="yellow").pack(pady=10)

    tk.Label(root, text=str(num1) + " " + operation + " " + str(num2) + " = ?",
             font=("Arial", 30, "bold"),
             bg="#234567", fg="white").pack(pady=25)

    answer_entry = tk.Entry(root, font=("Arial", 18),
                            justify="center")
    answer_entry.pack(pady=10)

    feedback = tk.Label(root, text="Enter your answer",
                        font=("Arial", 12),
                        bg="#234567", fg="white")
    feedback.pack(pady=10)

    tk.Button(root, text="Submit Answer",
              font=("Arial", 13, "bold"),
              bg="#16a085", fg="white",
              command=isCorrect).pack(pady=15)


# Checks The Answer
def isCorrect():
    global score, attempt

    user_answer = answer_entry.get()

    if user_answer == "":
        messagebox.showwarning("Warning", "Please enter an answer!")
        return

    try:
        user_answer = int(user_answer)
    except ValueError:
        messagebox.showwarning("Warning", "Please enter a whole number!")
        return

    if user_answer == answer:

        if attempt == 1:
            score = score + 10
            feedback.config(text="Correct! +10 Points", fg="lightgreen")
        else:
            score = score + 5
            feedback.config(text="Correct! +5 Points", fg="lightgreen")

        root.after(1000, nextQuestion)

    else:

        if attempt == 1:
            attempt = 2
            feedback.config(text="Wrong! Try one more time.",
                            fg="orange")
            answer_entry.delete(0, tk.END)

        else:
            feedback.config(text="Wrong! The answer is " + str(answer),
                            fg="red")
            root.after(1500, nextQuestion)


# Next Question
def nextQuestion():
    global question

    question = question + 1

    if question <= 10:
        displayProblem()
    else:
        displayResults()


# Display Results
def displayResults():
    clear()

    tk.Label(root, text="QUIZ FINISHED!",
             font=("Arial", 25, "bold"),
             bg="#234567", fg="white").pack(pady=30)

    tk.Label(root, text="Your Final Score: " + str(score) + " / 100",
             font=("Arial", 20, "bold"),
             bg="#234567", fg="yellow").pack(pady=20)

    if score > 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"

    tk.Label(root, text="Your Grade: " + grade,
             font=("Arial", 20, "bold"),
             bg="#234567", fg="white").pack(pady=15)

    tk.Label(root, text="Would you like to play again?",
             font=("Arial", 14),
             bg="#234567", fg="white").pack(pady=20)

    tk.Button(root, text="Play Again",
              font=("Arial", 13, "bold"),
              bg="#16a085", fg="white",
              command=displayMenu).pack(pady=10)

    tk.Button(root, text="Exit",
              font=("Arial", 13, "bold"),
              command=root.destroy).pack(pady=5)


# To Menu / Show

displayMenu()

root.mainloop()
