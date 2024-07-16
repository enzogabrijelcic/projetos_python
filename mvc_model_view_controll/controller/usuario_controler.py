import tkinter as tk
from view.usuario_view import UsuarioView
from model.usuario_model import *

class UsuarioController:
    def __init__(self, view:UsuarioView, model:UsuarioModel):
        self.view = view
        self.model = model
        self.view.adicionar_button.config(command=self.adicionar_usuario)
        self.carregar_usuarios()

    def adicionar_usuario(self):
        nome = self.view.get_nome()
        idade = self.view.get_idade()
        if nome and idade.isdigit():
            self.model.inserir_usuario(nome, int(idade))
            self.view.nome_entry.delete(0, tk.END)
            self.view.idade_entry.delete(0, tk.END)
            self.view.usuarios_listbox.delete(0,tk.END)
            self.carregar_usuarios()
        else:
            self.view.show_info()

    def carregar_usuarios(self):
        usuarios = self.model.selecionar_usuarios()
        for usuario in usuarios:
            self.view.adicionar_usuario_lista(usuario)

    

