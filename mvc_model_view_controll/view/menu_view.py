import tkinter as tk
from controller.usuario_controler import UsuarioController
from controller.usuario_delete_controller import DeleteController
from controller.usuario_atualizar_controller import AtualizaController
from model.usuario_model import UsuarioModel
from view.usuario_view import UsuarioView
from view.usuario_delete_view import DeleteView
from view.usuario_atualizar_view import AtualizaView


class MenuView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()
        self.master.geometry('400x400')

    def opcao_selecionada(self, opcao):
        if opcao == "1":
            self.master.switch_frame(UsuarioView)
            self.master.title("adicionar usuário")
        elif opcao == "2":
            self.master.switch_frame(AtualizaView)
            self.master.title("atualizar usuário")
        elif opcao == "3":
            self.master.switch_frame(DeleteView)
            self.master.title("deletar usuário")

    def criar_menu_dropdown(self, master):
        menu_dropdown = tk.Menu(master, tearoff=0)
        menu_dropdown.add_command(label="adicionar usuário", command=lambda: self.opcao_selecionada("1"))
        menu_dropdown.add_command(label="atualizar usuário", command=lambda: self.opcao_selecionada("2"))
        menu_dropdown.add_command(label="deletar usuário", command=lambda: self.opcao_selecionada("3"))
        return menu_dropdown

    def create_widgets(self):
        mb = tk.Menubutton(self, text="MENU", relief=tk.RAISED)
        mb.menu = self.criar_menu_dropdown(mb)
        mb["menu"] = mb.menu
        mb.pack(anchor="e", pady=12, padx=12)






         
