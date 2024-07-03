#Fazer um botão que ao apertar: Reproduz em uma label o número de cliques 
#e um outro botão para zerar os cliques.
import tkinter as tk
from tkinter import ttk

class Num_click:
    def __init__(self,root):
        self.root = root
        self.root.title("Contador")
        self.root.geometry('300x100')
        self.contagem = 0
        
        self.label_contagem=tk.Label(root, text='numero de cliques: 0',)
        self.label_contagem.pack()
        
        self.botao_click = tk.Button(root, text="contagem", command=self.numero_cliques)
        self.botao_click.pack()
    
        self.reset_click = tk.Button(root, text = 'zerar', command=self.reset_contador)
        self.reset_click.pack()
        
    def numero_cliques(self):
        self.contagem +=1
        self.label_contagem.config(text = f'numero de cliques:{self.contagem}')
        
    def reset_contador(self):
        self.contagem = 0
        self.label_contagem.config(text=f'Numero do cliques: {self.contagem}')                                          
    
if __name__== "__main__":
    root=tk.Tk()
app = Num_click(root)
root.mainloop()