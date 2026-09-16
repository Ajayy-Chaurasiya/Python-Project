#Gui is what we see and interact with ..here i m importing tkinter module which i later named as tk
#tkinter is a python Built-in GUI tool/module 
import tkinter as tk

# RK() Create the main window of your application..
root = tk.Tk()

# Set window title and size
root.title("My first GUI project")
root.geometry("600x300")


# Function that runs when the button is clicked
def greet():
    name = entry.get()  # Get text entered by the user

    if name:
        result_label.config(text="Hello " + name + "!")
    else:
        result_label.config(text="Please enter your name.")


# Create a label to display text ...pack is for displaying the label on the window
instruction_label = tk.Label(root, text="Enter your name:")
instruction_label.pack()


# Create a text box for user input
entry = tk.Entry(root)
entry.pack()


# Create a button and connect it to the greet() function 
button = tk.Button(root, text="Greet Me", command=greet)
button.pack()


# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()


# Keep the window running and listen for user actions
root.mainloop()