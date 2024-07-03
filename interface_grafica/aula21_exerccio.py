#crie um código que labels automatizado que trabalhe com 2 linhas e duas colunas.
#modifique a iteração de rows e columns do slide anterior para formar a seguinte imagem:
#r0,c0 = “Marcio” 
#r0,c1 = “Lucas”
#r1,c0 = “Sarah”
#r1,c1 = “Felipe”


import tkinter as tk

# Configuração da janela principal
janela = tk.Tk()
janela.geometry("400x400")
janela.title("exercicio label automatizado")

# Frame com borda sólida
frame = tk.Frame(janela)
frame.pack(fill="both")

def create_label(frame, text, row, column):
    label = tk.Label(frame, text=text)
    label.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")
    match text:
        case text if text =='marcio':
            label.grid(row=0, column=0)
        case text if text == 'Lucas':
            label.grid(row=0, column=1)
        case text if text == 'Sarah':
            label.grid(row=1, column=0)
        case text if text == 'Felipe':
            label.grid(row=1, column=1)

            for i in range(4):
                create_label(frame, text ,0, i)

# Configurar as colunas e a linha para expandir uniformemente
for i in range(4):
    frame.grid_columnconfigure(i, weight=1)
frame.grid_rowconfigure(0, weight=1)

# Executar a aplicação
janela.mainloop()