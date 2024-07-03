#Faça uma janela com 600 de altura e 600 de largura. 
#Faça perguntar o nome e a data de nascimento. Depois exiba isso no console.
import tkinter as tk
from tkinter import ttk
nome = input('qual é o seu nome? ')
data_nasc = input('qual é a data do seu nascimento? ')
root=tk.Tk()
root.title('exercicio 4')
root.geometry('600x600')

label1 = tk.Label(root, text=f'nome:{nome}', font =("Arial", 14), fg = 'blue', background= 'yellow')
label1.pack(fill='both', expand=True)

label2 = tk.Label(root, text=f'nascimento:{data_nasc}',font =("Arial", 14), fg = 'blue', background= 'red')
label2.pack(fill='both', expand=True)  
    
root.mainloop()