import tkinter as tk
# Configuração da janela principal
janela = tk.Tk()
janela.title("a21 s18 Grid Layout with Borders")

# Frame com borda sólida
frame = tk.Frame(janela, borderwidth=2, relief="solid")
frame.pack(fill="y",expand=True)

# Função para criar labels com borda sólida
def create_label(frame, text, row, column):
    label = tk.Label(frame, text=text, borderwidth=2, relief="solid")
    label.grid(row=row, column=column, sticky="nsew")

# Criar labels
for i in range(4):
    match i:
        case 0:
            create_label(frame, "Marcio", 0, 0)
        case 1:
            create_label(frame, "Lucas", 0, 1)
        case 2:
            create_label(frame, "Shara", 1, 0)
        case 3:
            create_label(frame, "Felipe", 1, 1)    

# Configurar as colunas e a linha para expandir uniformemente

frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=1)
# Executar a aplicação
janela.mainloop()



