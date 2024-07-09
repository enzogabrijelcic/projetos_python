import tkinter as tk
from tkinter import ttk

class ScrollableFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
       
        # Cria o widget Canvas com a cor de fundo amarela
        self.canvas = tk.Canvas(self, background="yellow")
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
       
        # Cria a barra de rolagem (Scrollbar)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
       
        # Configura o Canvas para funcionar com a barra de rolagem
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', self.on_canvas_configure)
       
        # Cria um frame dentro do Canvas com a cor de fundo vermelha
        self.scrollable_frame = ttk.Frame(self.canvas, style="My.TFrame")
        self.scrollable_frame.bind("<Configure>", self.on_frame_configure)
       
        # Cria uma janela dentro do Canvas que contém o frame
        self.canvas_window = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

    def on_frame_configure(self, event):
        # Atualiza a região de rolagem do Canvas para abranger o frame interno
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        # Redimensiona o frame interno para corresponder à largura do Canvas
        self.canvas.itemconfig(self.canvas_window, width=event.width)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tela com Scroll Tkinter")
        self.geometry("400x300")
       
        # Configura estilos personalizados
        style = ttk.Style()
        style.configure("My.TFrame", background="red")
       
        scrollable_frame = ScrollableFrame(self)
        scrollable_frame.pack(fill=tk.BOTH, expand=True)

        # Adiciona diversos widgets (buttons) no frame rolável
        for i in range(50):
            label = ttk.Label(scrollable_frame.scrollable_frame, text=f"Label {i+1}")
            label.pack(anchor="n")

if __name__ == "__main__":
    app = App()
    app.mainloop()
