import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)
root.configure(bg="gray20")

exp = ""

def click(val):
    global exp
    if val == "=":
        try:
            exp = str(eval(exp))
        except:
            exp = "Error"
    elif val == "C":
        exp = ""
    else:
        exp += str(val)
    var.set(exp if exp else "0")

var = tk.StringVar(value="0")

display = tk.Label(root, textvariable=var, font=("Arial", 24), bg="gray20", fg="white", anchor="e", padx=10)
display.pack(fill="x", pady=20)

btns = [
    ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
    ('0', 3, 0), ('C', 3, 1), ('=', 3, 2), ('+', 3, 3)
]

frame = tk.Frame(root, bg="gray20")
frame.pack(fill="both", expand=True, padx=5, pady=5)

for i in range(4):
    frame.rowconfigure(i, weight=1)
    frame.columnconfigure(i, weight=1)

for text, r, c in btns:
    b = tk.Button(frame, text=text, font=("Arial", 14), bg="gray30", fg="white", bd=0, command=lambda t=text: click(t))
    b.grid(row=r, column=c, sticky="nsew", padx=3, pady=3)

root.mainloop()
