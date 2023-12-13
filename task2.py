import tkinter as tk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Cannot divide by zero"
        else:
            result = "Invalid operation"

        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter valid numbers.")

def clear():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    result_label.config(text="Result: ")

# Create the main window
window = tk.Tk()
window.title("Enhanced Calculator")

# Entry widgets for user input
entry_num1 = tk.Entry(window)
entry_num2 = tk.Entry(window)

# Operation choice
operation_var = tk.StringVar()
operation_var.set('+')  # Default operation is addition

operation_menu = tk.OptionMenu(window, operation_var, '+', '-', '*', '/')

# Buttons for calculation and clearing
calculate_button = tk.Button(window, text="Calculate", command=calculate)
clear_button = tk.Button(window, text="Clear", command=clear)

# Label to display the result
result_label = tk.Label(window, text="Result: ")

# Arrange widgets using the grid layout
entry_num1.grid(row=0, column=0)
operation_menu.grid(row=0, column=1)
entry_num2.grid(row=0, column=2)
calculate_button.grid(row=1, column=0, columnspan=2)
clear_button.grid(row=1, column=2)
result_label.grid(row=2, column=0, columnspan=3)

# Start the GUI event loop
window.mainloop()
