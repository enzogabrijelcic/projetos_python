import tkinter as tk
from model.usuario_m import *
from view.usuario_v import UsuarioView
from controller.usuario_c import UsuarioController

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Gerenciamento de Usuários")
    root.geometry("400x300")

    model = UsuarioModel()
    view = UsuarioView(root)
    model.atualizar_nome_idade(1, 'Eduardo', 50)
    usuarios = model.selecionar_usuarios()
    print("Usuários na tabela:")
    for usuario in usuarios:
        print(usuario)

    controller = UsuarioController(view, model)

    root.mainloop()
    model.fechar_conexao()