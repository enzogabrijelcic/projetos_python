import tkinter as tk
from tkinter import ttk

# Cria a janela principal
root = tk.Tk()
root.title("Exemplo de GUI com Tkinter")
root.geometry("400x300")

# Adiciona um Label
label = tk.Label(root, text="Olá, Tkinter!", font=("Arial", 14), fg="blue")
label.pack(pady=10)

# Função para ser chamada quando o botão for clicado
def on_button_click():
    print("Botão clicado!")
    label.config(text="Você clicou no botão!")  # Atualiza o texto do label

# Adiciona um Button
button = tk.Button(root, text="Clique em mim", command=on_button_click)
button.pack(pady=10)

# Adiciona um Entry
entry = tk.Entry(root, width=20)
entry.pack(pady=10)

# Adiciona um Combobox
combobox = ttk.Combobox(root, values=["Opção 1", "Opção 2", "Opção 3"])
combobox.pack(pady=10)

# Adiciona um Frame
frame = tk.Frame(root, borderwidth=2, relief="solid")
frame.pack(pady=10, padx=10)

# Adiciona um Label dentro do Frame
frame_label = tk.Label(frame, text="Label dentro do Frame")
frame_label.pack(pady=10, padx=10)

# Inicia o loop principal
root.mainloop()


