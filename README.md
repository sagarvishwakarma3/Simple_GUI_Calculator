# Simple_GUI_Calculator

## **Overview**
This is a **Simple GUI Calculator** application built with Python's `tkinter` module. The calculator provides basic arithmetic operations and an intuitive interface to perform calculations efficiently. It's a lightweight and user-friendly desktop application.

---

## **Features**
1. **Basic Arithmetic Operations**:
   - Supports addition, subtraction, multiplication, and division.
2. **Error Handling**:
   - Displays "Error" for invalid inputs or calculations.
3. **Clear Functionality**:
   - Quickly reset the input field using the "C" button.
4. **Responsive Design**:
   - Adapts to various screen sizes with dynamically adjustable button sizes.
5. **Interactive GUI**:
   - Well-designed buttons with distinct colors for better user experience.

---

## **How It Works**

### **1. Input Mechanism**
- Users enter numbers and operators by clicking the buttons on the interface.
- The current expression is displayed in the input field at the top.

### **2. Calculation**
- Clicking the `=` button evaluates the expression using Python's `eval()` function and displays the result.
- Invalid expressions result in an "Error" message.

### **3. Clear Input**
- Clicking the `C` button clears the input field, allowing users to start a new calculation.

---

## **Prerequisites**
- **Python Version**: Requires Python 3.6 or higher.
- No additional libraries are required as `tkinter` is included in Python's standard library.

---

## **How to Run the Application**

1. **Save the Script**:
   Save the code as `calculator.py` or a similar name.

2. **Run the Script**:
   Open a terminal or command prompt and execute:
   ```bash
   python calculator.py
   ```

3. **Use the Calculator**:
   - Click on the buttons to perform calculations.
   - Example operations:
     - Input: `8 + 2`, then click `=` → Output: `10`
     - Input: `9 / 0`, then click `=` → Output: `Error`

---

## **Code Explanation**

### **1. Functions**
- **`press_key(key)`**:
  - Updates the input field with the button pressed.
- **`calculate()`**:
  - Evaluates the expression in the input field using `eval()` and updates the field with the result.
  - Handles exceptions for invalid expressions.
- **`clear()`**:
  - Clears the input field for new calculations.

### **2. GUI Setup**
- The main window (`root`) is created using `tk.Tk()` and titled "Sagar's Calculator".
- An **entry widget** is used to display the input expression and results.
- Buttons are dynamically created for numbers, operators, and functions (`C` and `=`).

### **3. Button Layout**
- Buttons are organized in a grid layout with:
  - Numbers (`0-9`)
  - Operators (`+`, `-`, `*`, `/`)
  - Special buttons:
    - `C`: Clear the input field.
    - `=`: Evaluate the expression.

### **4. Responsive Design**
- `grid_rowconfigure` and `grid_columnconfigure` are used to make the layout adaptable to various window sizes.

---

## **Code**
```python
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
```

---

## **Example Workflow**
1. Launch the application.
2. Perform a calculation:
   - Input: `45 + 20`, then click `=` → Output: `65`.
3. Clear the field:
   - Click `C` to reset the input.

---

## **Benefits**
- Simplifies basic arithmetic calculations.
- Provides a hands-on example of building a functional GUI application.
- A stepping stone to more advanced GUI development.

---

## **Future Enhancements**
1. Add more operations:
   - Support for square root, exponentiation, and percentages.
2. Include a **history feature** to track previous calculations.
3. Add keyboard input support for enhanced usability.

---

## **Conclusion**
This Simple GUI Calculator is a beginner-friendly project that demonstrates the power of Python and `tkinter` in creating interactive applications. It is an ideal starting point for exploring GUI development and further customization.
