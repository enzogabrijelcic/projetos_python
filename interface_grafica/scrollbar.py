import tkinter as tk
from tkinter import ttk

# Criar a janela principal
root = tk.Tk()
root.title("Exemplo de Scrollbar Visível")
root.geometry("300x200")

# Criar o frame para conter o Listbox e a Scrollbar
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

# Criar o Listbox
listbox = tk.Listbox(frame)
listbox.pack(side="left", fill="both", expand=True)

# Criar a Scrollbar
scrollbar = tk.Scrollbar(frame, orient="vertical", command=listbox.yview)
scrollbar.pack(side="right", fill="y")

# Configurar o Listbox para usar a Scrollbar
listbox.config(yscrollcommand=scrollbar.set)

# Adicionar itens ao Listbox
for i in range(100):
    listbox.insert("end", f"Item {i+1}")

# Iniciar o loop principal
root.mainloop()

