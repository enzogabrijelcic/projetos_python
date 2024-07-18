import tkinter as tk

from controller.usuario_controler import UsuarioController
from controller.usuario_delete_controller import DeleteController
from controller.usuario_atualizar_controller import AtualizaController
from model.usuario_model import UsuarioModel
from view.usuario_view import UsuarioView
from view.usuario_delete_view import DeleteView
from view.usuario_atualizar_view import AtualizaView
from view.menu_view import MenuView

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("adicionar usuário")
        MenuView(self).pack(fill=tk.BOTH, expand=True)
        self.switch_frame(UsuarioView)
   
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if frame_class ==  UsuarioView:
            model =  UsuarioModel()
            UsuarioController(new_frame,model)
        elif frame_class == DeleteView:
            model =  UsuarioModel()
            DeleteController(new_frame, model)
        elif frame_class == AtualizaView:
            model =  UsuarioModel()
            AtualizaController(new_frame, model)

        if hasattr(self, "current_frame"):
            self.current_frame.destroy()#apaga a visualização anterior
        self.current_frame = new_frame
        self.current_frame.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
