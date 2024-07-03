import tkinter as tk
from tkinter import ttk

class Casa:
    def __init__(self, n_comodos, n_portas, n_janelas, cor_externa, numero, endereco, proprietario):
        self.n_comodos = n_comodos
        self.n_portas = n_portas
        self.n_janelas = n_janelas
        self.cor_externa = cor_externa
        self.numero = numero
        self.endereco = endereco
        self.proprietario = proprietario

# Cria a janela principal
root = tk.Tk()
root.title("Casa")
root.geometry("400x300")

casa = Casa(n_comodos=3, n_portas=4, n_janelas= 4, cor_externa="verde", numero=235, endereco="rua tal, numero 20", proprietario= "Enzo") #objeto

message_1 = tk.Label(root, text= "nº de comodos:", anchor="w", background= 'yellow')
message_1.pack(side="top", fill="both")
message1 = tk.Label(root, text= casa.n_comodos, anchor="w", background= 'yellow')
message1.pack(side="top", fill="both")

message_2 = tk.Label(root, text= "nº de portas", anchor="w", background="light blue")
message_2.pack(side="top", fill="both")
message2= tk.Label(root, text= casa.n_portas, anchor="w", background="light blue")
message2.pack(side="top", fill="both")

message_3 = tk.Label(root, text="nº de janelas:", anchor="w", background="red")
message_3.pack(side="top", fill= "both")
message3 = tk.Label(root, text=casa.n_janelas, anchor="w", background="red")
message3.pack(side="top", fill= "both")

message_4 = tk.Label(root, text="cor externa:", anchor="w", background="green")
message_4.pack(side="top", fill="both")
message4 = tk.Label(root, text= casa.cor_externa, anchor="w", background="green")
message4.pack(side="top", fill="both")

message_5 = tk.Label(root, text="numero:", anchor="w", background="gray")
message_5.pack(side="top", fill="both")
message5 = tk.Label(root, text= casa.numero, anchor="w", background="gray")
message5.pack(side="top", fill="both")

message_6 = tk.Label(root, text="endereço:", anchor="w", background="orange")
message_6.pack(side="top", fill="both")
message6 = tk.Label(root, text= casa.endereco, anchor="w", background="orange")
message6.pack(side="top", fill="both")

message_7 = tk.Label(root, text="proprietario", anchor="w", background="purple")
message_7.pack(side="top", fill="both")
message7 = tk.Label(root, text= casa.proprietario, anchor="w", background="purple")
message7.pack(side="top", fill="both")

root.mainloop()