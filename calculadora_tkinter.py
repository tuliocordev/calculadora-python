import tkinter as tk

def on_click(button_text):
    if button_text == "=":
        try:
            result = str(eval(entry_var.get()))
            entry_var.set(result)
        except Exception:
            entry_var.set("Erro")
    elif button_text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + button_text)

root = tk.Tk()
root.title("Calculadora")
root.geometry("300x400")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify="right", bd=10, relief=tk.GROOVE)
entry.pack(fill="both", padx=10, pady=10)

buttons = [
    ["7           ", "8", "9", "/"],
    ["4 ", "5", "6", "*"],
    ["1 ", "2", "3", "-"],
    ["0 ", "C", "=", "+"]
]

frame = tk.Frame(root)
frame.pack(expand=True, fill="both")

for row in buttons:
    button_row = tk.Frame(frame)
    button_row.pack(expand=True, fill="both")
    for char in row:
        button = tk.Button(button_row, text=char, font=("Arial", 18), command=lambda c=char: on_click(c))
        button.pack(side="left", expand=True, fill="both")

root.mainloop()