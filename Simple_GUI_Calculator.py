import tkinter as tk

# Function to update the input field
def press_key(key):
    entry_text.set(entry_text.get() + key)

# Function to evaluate the expression
def calculate():
    try:
        result = eval(entry_text.get())
        entry_text.set(str(result))
    except Exception:
        entry_text.set("Error")

# Function to clear the input field
def clear():
    entry_text.set("")

# Setting up the main window
root = tk.Tk()
root.title("Sagar's Calculator")

# Entry widget to display expressions and results
entry_text = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_text, font=("Arial", 20), bd=5, insertwidth=4, width=18, borderwidth=4, justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Buttons for the calculator
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == "=":
        btn = tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 14), bg="lightgreen", command=calculate)
    elif button == "C":
        btn = tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 14), bg="red", fg="white", command=clear)
    else:
        btn = tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 14), command=lambda b=button: press_key(b))
    
    btn.grid(row=row_val, column=col_val, sticky="nsew")
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Adjust row and column weights
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Run the application
root.mainloop()
