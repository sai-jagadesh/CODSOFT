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

# Function to add a character to the input field
def add_character(character):
    entry.insert(tk.END, character)

# Function to handle keyboard events
def on_key_press(event):
    key = event.char
    if key == '\r':  # Enter key
        calculate()
    elif key in '0123456789.*/+-':
        add_character(key)

# Create the main application window
app = tk.Tk()
app.title("Calculator")

# Create an input field
entry = tk.Entry(app, width=25, font=("Helvetica", 16))
entry.grid(row=0, column=0, columnspan=4)

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
              command=lambda btn=button: add_character(btn) if btn != "=" else calculate()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Bind the Enter key to the calculate function
app.bind('<Return>', lambda event=None: calculate())

# Bind other keys to the on_key_press function
app.bind('<Key>', on_key_press)

# Start the GUI application
app.mainloop()
