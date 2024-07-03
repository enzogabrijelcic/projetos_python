#faça um 1 botão; uma entrada; uma label. Tudo alinhado à direita.
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("exercicio 3")
root.geometry('300x100')

frame1 = tk.Frame(root)
frame1.pack(fill="both")

frame2 = tk.Frame(root)
frame2.pack(fill="both")

frame3 = tk.Frame(root,)
frame3.pack(fill='both')

botao= tk.Button(frame1, text="Botão")
botao.pack(fill='both', side='right')

entrada = tk.Entry(frame2)
entrada.pack(fill='both', side='right')

label = tk.Label(frame3, text= 'label', fg='white', bg='blue')
label.pack(fill='both',side='right')

root.mainloop()