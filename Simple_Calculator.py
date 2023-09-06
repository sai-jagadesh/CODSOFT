import tkinter as tk

# Function to perform calculations
def calculate():
    try:
        expression = entry.get()
        result = str(eval(expression))
        entry.delete(0, tk.END)  # Clear the input field
        entry.insert(tk.END, result)  # Display the result
    except:
        entry.delete(0, tk.END)  # Clear the input field
        entry.insert(tk.END, "Error")

# Create the main application window
app = tk.Tk()
app.title("Calculator")

# Create an input field and put cursor in it
entry = tk.Entry(app, width=25, font=("Helvetica", 16))
entry.grid(row=0, column=0, columnspan=4)
entry.focus_set()  # Set focus to the entry field

# Create buttons for numbers and operators
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(app, text=button, width=6, height=2, font=("Helvetica", 16),
              command=lambda btn=button: entry.insert(tk.END, btn) if btn != "=" else calculate()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Bind the Enter key to the calculate function
app.bind('<Return>', lambda event=None: calculate())

# Start the GUI application
app.mainloop()
