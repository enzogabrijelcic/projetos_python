#criar labels de forma automatizada
import tkinter as tk

# Configuração da janela principal
janela = tk.Tk()
janela.geometry("400x400")
janela.title("Grid Layout with Borders")

# Frame com borda sólida
frame = tk.Frame(janela, borderwidth=2, relief="solid")
frame.pack(fill="both")

# Função para criar labels com borda sólida
def create_label(frame, text, row, column):
    label = tk.Label(frame, text=text, borderwidth=2, relief="solid")
    label.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

# Criar labels
for i in range(4):
    create_label(frame, "junior", 0, i)

# Configurar as colunas e a linha para expandir uniformemente
for i in range(4):
    frame.grid_columnconfigure(i, weight=1)
frame.grid_rowconfigure(0, weight=1)

# Executar a aplicação
janela.mainloop()


