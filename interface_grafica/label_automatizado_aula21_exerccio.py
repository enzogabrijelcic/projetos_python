#crie um código que labels automatizado que trabalhe com 2 linhas e duas colunas.
#modifique a iteração de rows e columns do slide anterior para formar a seguinte imagem:
#r0,c0 = “Marcio” 
#r0,c1 = “Lucas”
#r1,c0 = “Sarah”
#r1,c1 = “Felipe”


import tkinter as tk

# Configuração da janela principal
janela = tk.Tk()
janela.geometry('400x100')
janela.title("exercicio label automatizado")

# Frame com borda sólida
frame = tk.Frame(janela)
frame.pack(fill="both")

def create_label(frame, text, row, column):
    label = tk.Label(frame, text=text)
    label.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")
    

for i in range(4):
    match i:    
        case 0:
            create_label(frame, 'Marcio',0, 0)
        case 1:
            create_label(frame, 'Lucas',0, 1)
        case 2:
            create_label(frame, 'Sarah',1, 0)
        case 3:
            create_label(frame, 'Marcio',1,1) 
    
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=1)
# Executar a aplicação
janela.mainloop()
#print(nomes[2])