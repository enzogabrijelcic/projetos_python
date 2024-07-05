import tkinter as tk
from tkinter import ttk


def pressione_esc(event):
    print('voce clicou na tecla ESC')


root = tk.Tk()

btn = ttk.Button(root, text='Esc')
root.bind('<Escape>', pressione_esc)

btn.pack(expand=True)

root.mainloop()