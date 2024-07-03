import tkinter as tk
from tkinter import ttk

# Cria a janela principal
root = tk.Tk()
root.title("Minha Primeira GUI")
root.geometry("400x300")

# Adiciona um label
label = tk.Label(root, text="Olá, Tkinter!")
label.pack(pady=10)

# Função para ser chamada quando o botão for clicado
def on_button_click():
    print("Botão clicado!")
    label.config(text="Você clicou no botão!")  # Atualiza o texto do label

# Adiciona um botão
button = tk.Button(root, text="Clique em mim", command=on_button_click)
button.pack(pady=10)

# Adiciona uma entrada de texto
entry = tk.Entry(root)
entry.pack(pady=10)

# Adiciona um botão para pegar o texto da entrada
def on_get_text():
    user_input = entry.get()
    print(f"Entrada do usuário: {user_input}")
    label.config(text=f"Você digitou: {user_input}")

get_text_button = tk.Button(root, text="Obter texto", command=on_get_text)
get_text_button.pack(pady=10)

# Inicia o loop principal
root.mainloop()


