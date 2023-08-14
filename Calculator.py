import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.geometry("400x650")
root.title("Calculator")

entry = tk.Entry(root, font=('Helvetica', 20))
entry.pack(fill=tk.BOTH, ipadx=10, padx=20, pady=50)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ['(', ')', '%', 'C'],
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        btn = tk.Button(button_frame, text=text, font=('Helvetica', 15), padx=30, pady=30)
        btn.grid(row=i, column=j)
        btn.bind("<Button-1>", on_click)

root.mainloop()