import tkinter as tk
import random

root = tk.Tk()
root.title("Joke Telling Assistant")
root.geometry("500x400")
root.configure(bg="#234567")

# Read Jokes From File
file = open("JokeQuiz/randomJokes.txt", "r")
jokes = file.readlines()
file.close()

# Variables
current_joke = ""
current_punchline = ""


# Tells Jokes
def tellJoke():
    global current_joke, current_punchline

    current_joke = random.choice(jokes)

    parts = current_joke.split("?")

    setup = parts[0] + "?"
    current_punchline = parts[1].strip()

    setup_label.config(text=setup)
    punchline_label.config(text="")


# Shows the punchline
def showPunchline():
    punchline_label.config(text=current_punchline)


# Next joke
def nextJoke():
    tellJoke()


# Title
tk.Label(
    root,
    text="JOKE TELLING ASSISTANT",
    font=("Arial", 20, "bold"),
    bg="#234567",
    fg="white"
).pack(pady=25)


# Jokes Setup
setup_label = tk.Label(
    root,
    text="Click the button to get a joke!",
    font=("Arial", 14),
    bg="#234567",
    fg="white"
)

setup_label.pack(pady=20)


# Punchlines
punchline_label = tk.Label(
    root,
    text="",
    font=("Arial", 14),
    bg="#234567",
    fg="yellow"
)

punchline_label.pack(pady=15)


# Buttons
tk.Button(
    root,
    text="Alexa tell me a Joke",
    font=("Arial", 12),
    command=tellJoke
).pack(pady=5)


tk.Button(
    root,
    text="Show Punchline",
    font=("Arial", 12),
    command=showPunchline
).pack(pady=5)


tk.Button(
    root,
    text="Next Joke",
    font=("Arial", 12),
    command=nextJoke
).pack(pady=5)


tk.Button(
    root,
    text="Quit",
    font=("Arial", 12),
    command=root.destroy
).pack(pady=5)


root.mainloop()