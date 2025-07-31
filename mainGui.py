import tkinter as tk
from utils import evaluate_expression

# Root window setup
root = tk.Tk()
root.title("Scientific Calculator")

# Entry widget for input/output
entry = tk.Entry(root, width=40, font=('Arial', 14), borderwidth=5, relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Function to handle button presses
def on_button_click(char):
    if char == 'C':
        entry.delete(0, tk.END)  # Clear input
    elif char == '=':
        expr = entry.get().replace('^', '**')  # Replace ^ with ** for power
        result = evaluate_expression(expr)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
        with open("history.txt", "a") as f:
            f.write(f"{expr} = {result}\n")
    else:
        entry.insert(tk.END, char)  # Add char to entry

# Layout buttons
buttons = [
    ['7', '8', '9', '/', 'sqrt'],
    ['4', '5', '6', '*', 'log'],
    ['1', '2', '3', '-', 'sin'],
    ['0', '.', '(', ')', 'cos'],
    ['C', '^', '=', '+', 'tan']
]

for r, row in enumerate(buttons):
    for c, char in enumerate(row):
        btn = tk.Button(root, text=char, width=6, height=2, font=('Arial', 12),
                        command=lambda ch=char: on_button_click(ch))
        btn.grid(row=r+1, column=c, padx=2, pady=2)

# Run the GUI
root.mainloop()
