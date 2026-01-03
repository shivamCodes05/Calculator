import tkinter as tk

# Main window
root = tk.Tk()
root.title("Python GUI Calculator")
root.geometry("350x450")
root.resizable(False, False)

# Entry box
entry = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15)

# Button click function
def click(value):
    entry.insert(tk.END, value)

# Clear function
def clear():
    entry.delete(0, tk.END)

# Calculate function
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Buttons layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0

for btn in buttons:
    if btn == '=':
        tk.Button(root, text=btn, font=("Arial", 18),
                  bg="lightgreen", command=calculate).grid(
            row=row, column=col, columnspan=2, sticky="nsew", ipadx=20, ipady=20)
        col += 2
    else:
        tk.Button(root, text=btn, font=("Arial", 18),
                  command=lambda b=btn: click(b)).grid(
            row=row, column=col, ipadx=20, ipady=20)
        col += 1

    if col > 3:
        col = 0
        row += 1

# Clear button
tk.Button(root, text="C", font=("Arial", 18),
          bg="tomato", command=clear).grid(
    row=row, column=0, columnspan=4, sticky="nsew", ipady=20)

root.mainloop()
