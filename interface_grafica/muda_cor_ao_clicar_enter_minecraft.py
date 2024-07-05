import random
import tkinter as tk

# Configuração da janela principal
janela = tk.Tk()
janela.geometry("600x600")
janela.title("minecraft")

# Criação do canvas
cabeca = tk.Canvas(janela, width=600, height=600, borderwidth=20, bg='green',relief="solid")
cabeca.pack()

def mudar_cor(event):
    cores = ["red", "blue", "magenta", "green"]
    indice = random.randrange(0,4,1)
    cabeca.config(bg=cores[indice])

janela.bind('<Return>',mudar_cor)

cabeca.create_rectangle(125,150,225,250, fill='black')#olho esquerdo
cabeca.create_rectangle(375,150,475,250,fill='black')#olho direito

cabeca.create_rectangle(225,250,375,300, fill='black')#nariz acima
cabeca.create_rectangle(225,300,425,400, fill='black')#nariz embaixo
cabeca.create_rectangle(175,300,225,450, fill='black')#canto esquerdo boca
cabeca.create_rectangle(375,400,425,450, fill='black')#canto direito boca


janela.mainloop()