import tkinter as tk
from model.usuario_model import *
from view.usuario_atualizar_view import AtualizaView
from controller.usuario_atualizar_controller import AtualizaController

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Gerenciamento de Usuários")
    root.geometry("400x300")

    model = UsuarioModel()
    view = AtualizaView(root)
    usuarios = model.selecionar_usuarios()
    print("Usuários na tabela:")
    for usuario in usuarios:
        print(usuario)

    controller = AtualizaController(view, model)

    root.mainloop()
    model.fechar_conexao()