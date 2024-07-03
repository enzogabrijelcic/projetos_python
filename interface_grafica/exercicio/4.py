#Faça uma janela com 600 de altura e 600 de largura. 
#Faça perguntar o nome e a data de nascimento. Depois exiba isso no console.
import tkinter as tk
from tkinter import ttk
nome = input('qual é o seu nome?')
idade = input('qual é a data do seu nascimento')
root=tk.Tk()
root.geometry('600x600')

label1 = tk.Label(root, text=f'nome:{nome}')
label1.pack()

label2 = tk.Label(root, text='nascimento:')
label2.pack()  
    
root.mainloop()