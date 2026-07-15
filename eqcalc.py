import tkinter as tk, math

eqcalc = tk.Tk()
eqcalc.title("Ecuation Calculator")
eqcalc.geometry("500x400")
eqcalc.config(bg="#222222")

a_label = tk.Label(eqcalc, text="Enter a:", font=('calibre',12, 'bold'), bg="#222222", fg="#ffffff")
a_label.grid(row=0, column=0, padx=5)
b_label = tk.Label(eqcalc, text="Enter b:", font=('calibre',12, 'bold'), bg="#222222", fg="#ffffff")
b_label.grid(row=1, column=0, padx=5)
c_label = tk.Label(eqcalc, text="Enter c:", font=('calibre',12, 'bold'), bg="#222222", fg="#ffffff")
c_label.grid(row=2, column=0, padx=5)

a_entry = tk.Entry(eqcalc, font=('calibre',10,'normal'), bg="#333333", fg="#ffffff")
a_entry.grid(row=0, column=1, padx=5)
b_entry = tk.Entry(eqcalc, font=('calibre',10,'normal'), bg="#333333", fg="#ffffff")
b_entry.grid(row=1, column=1, padx=5)
c_entry = tk.Entry(eqcalc, font=('calibre',10,'normal'), bg="#333333", fg="#ffffff")
c_entry.grid(row=2, column=1, padx=5)

result_lbl = tk.Label(eqcalc, text="", font=('calibre', 12, 'normal'), bg="#222222", fg="#ffffff")
result_lbl.grid(row=3, column=1, padx=10)

def formula():
    a = float(a_entry.get())
    b = float(b_entry.get())
    c = float(c_entry.get())

    sqrt = (b)**2 - 4 * (a) * (c)
    x = (-(b) + math.sqrt(sqrt)) / (2 * (a))
    y = (-(b) - math.sqrt(sqrt)) / (2 * (a))
    return x, y

def enter():
    try:
        x, y = formula()
        result_lbl.config(text=f"pos: {x}\nneg: {y}")
    except ValueError:
        result_lbl.config(text="Error")

enter_btn = tk.Button(eqcalc, command=enter, text="Enter", font=('calibre',12, 'bold'), bg="#222222", fg="#ffffff")
enter_btn.grid(row=0, column=3, padx=5)


eqcalc.mainloop()