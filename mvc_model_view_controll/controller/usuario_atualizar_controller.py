from model.usuario_model import UsuarioModel
import tkinter as tk
from view.usuario_atualizar_view import AtualizaView

class AtualizaController:
    def __init__(self, view: AtualizaView, model: UsuarioModel):
        self.view = view
        self.model = model
        self.view.atualizar_button.config(command=self.atualizar_usuario)
        self.carregar_usuarios()

    def atualizar_usuario(self):
        id = self.view.get_id()
        nome= self.view.get_nome()
        idade = self.view.get_idade()
        if id and nome and idade.isdigit():
            self.model.atualizar_nome_idade(id, nome, idade)
            self.view.usuarios_listbox.delete(0,tk.END)
            self.carregar_usuarios()
        else:
            self.view.show_info()
        

    def carregar_usuarios(self):
        usuarios = self.model.selecionar_usuarios()
        for usuario in usuarios:
            self.view.adicionar_usuario_lista(usuario)