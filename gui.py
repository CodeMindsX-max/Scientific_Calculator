import tkinter as tk
from utils import evaluate_expression
from datetime import datetime

def log_to_file(expr, result):
    with open("history.txt", "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {expr} = {result}\n")

def calculate():
    expr = entry.get()
    result = evaluate_expression(expr)
    result_label.config(text=f"Result: {result}")
    log_to_file(expr, result)

# GUI window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x300")

# Widgets
entry = tk.Entry(root, font=("Arial", 14), width=30)
entry.pack(pady=20)

calc_button = tk.Button(root, text="Calculate", command=calculate, font=("Arial", 12))
calc_button.pack()

result_label = tk.Label(root, text="Result:", font=("Arial", 12))
result_label.pack(pady=20)

# Run the app
root.mainloop()
