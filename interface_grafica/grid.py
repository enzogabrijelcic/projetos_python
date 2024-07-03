#grid layout
import tkinter as tk
from tkinter import ttk

menu_inicial = tk.Tk()
menu_inicial.title('Titulo')

label1 = tk.Label(menu_inicial, text="Label 1", font='Arial 20', background= 'red')
label2 = tk.Label(menu_inicial, text="Label 2", font='Arial 20', background= 'green')
label3 = tk.Label(menu_inicial, text="Label 3", font='Arial 20', background= 'blue')

label1.grid(row=0, column=0)
label2.grid(row=1, column=1)
label3.grid(row=2, column=2)

menu_inicial.mainloop()