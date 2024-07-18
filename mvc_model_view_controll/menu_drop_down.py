import tkinter as tk

def opcao_selecionada(opcao):
    if opcao == 'Vermelho':
        label_resultado.config(text=f'cor selecionada: {opcao}', background='red')
    elif opcao =='Verde':
        label_resultado.config(text=f'cor selecionada: {opcao}', background='green')
    elif opcao == 'Amarelo':
        label_resultado.config(text=f'cor selecionada: {opcao}', background='yellow')
        

root = tk.Tk()
root.title("Menu Dropdown com Tkinter")

# Função para criar um menu dropdown
def criar_menu_dropdown(master):
    menu_dropdown = tk.Menu(master, tearoff=0)
    menu_dropdown.add_command(label="Vermelho", command=lambda: opcao_selecionada("Vermelho"))
    menu_dropdown.add_command(label="Verde", command=lambda: opcao_selecionada("Verde"))
    menu_dropdown.add_command(label="Amarelo", command=lambda: opcao_selecionada("Amarelo"))
    return menu_dropdown

# Criar um Menubutton para mostrar o menu dropdown
mb = tk.Menubutton(root, text="Escolha uma cor", relief=tk.RAISED)
mb.menu = criar_menu_dropdown(mb)  # Associa o menu dropdown ao Menubutton
mb["menu"] = mb.menu  # Define o menu dropdown como o menu do Menubutton
mb.pack(pady=20)

# Label para mostrar a opção selecionada
label_resultado = tk.Label(root, text="Nenhuma cor selecionada")
label_resultado.pack()

root.mainloop()

