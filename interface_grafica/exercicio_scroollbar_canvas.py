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
        
        # Configura pesos das colunas e linhas do grid
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame.grid_rowconfigure(0, weight=1)

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
        self.geometry("400x200")
       
        # Configura estilos personalizados
        style = ttk.Style()
        style.configure("My.TFrame", background="red")
        
        frame_down = tk.Frame(height=20)
        frame_down.pack(fill=tk.BOTH, expand=True, side='bottom')
              
        scrollable_frame = ScrollableFrame(self)
        scrollable_frame.pack(fill=tk.BOTH, expand=True)
        
        
        def imprime():
            r1 = entry1.get()
            r2 = entry2.get()
            r3 = entry3.get()
            r4 = entry4.get()
            r5 = entry5.get()
            r6 = entry6.get()
            r7 = entry7.get()
            r8 = entry8.get()
            r9 = entry9.get()
            r10 = entry10.get()
            r11 = entry11.get()
            
            print('respostas impressas:\n', r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11)
    
      
        
        # Adiciona diversos widgets (buttons) no frame rolável
        label1 = ttk.Label(scrollable_frame.scrollable_frame, text='Qual é o seu nome?')
        label1.grid(row=0,column=0,sticky="nsew")
        entry1 = ttk.Entry(scrollable_frame.scrollable_frame)
        entry1.grid(row=0,column=1,sticky="nsew")

        
        label2 = ttk.Label(scrollable_frame.scrollable_frame, text='Qual a sua idade?')
        label2.grid(row=1,column=0,sticky="nsew")
        entry2 = ttk.Entry(scrollable_frame.scrollable_frame)
        entry2.grid(row=1,column=1,sticky="nsew")
        
        label3 = ttk.Label(scrollable_frame.scrollable_frame, text='Qual seu CPF?')
        label3.grid(row=2,column=0,sticky="nsew")
        entry3 = ttk.Entry(scrollable_frame.scrollable_frame)
        entry3.grid(row=2,column=1,sticky="nsew")
        
        label4 = ttk.Label(scrollable_frame.scrollable_frame, text='Qual é a sua nacionalidade?')
        label4.grid(row=3,column=0,sticky="nsew")
        entry4 = ttk.Entry(scrollable_frame.scrollable_frame)
        entry4.grid(row=3,column=1,sticky="nsew")
        
        label5 = ttk.Label(scrollable_frame.scrollable_frame, text='Grau de escolaridade:')
        label5.grid(row=4,column=0,sticky="nsew")
        entry5 = ttk.Entry(scrollable_frame.scrollable_frame)
        entry5.grid(row=4,column=1,sticky="nsew")
        
        label6 = ttk.Label(scrollable_frame.scrollable_frame, text='Estado Civil:')
        label6.grid(row=5,column=0,sticky="nsew")
        entry6 = ttk.Entry(scrollable_frame.scrollable_frame)
        entry6.grid(row=5,column=1,sticky="nsew")
        
        label7 = ttk.Label(scrollable_frame.scrollable_frame, text='Qual seu CEP?')
        label7.grid(row=6,column=0,sticky="nsew")
        entry7 = ttk.Entry(scrollable_frame.scrollable_frame)
        entry7.grid(row=6,column=1,sticky="nsew")
        
        label8 = ttk.Label(scrollable_frame.scrollable_frame, text='Rua:')
        label8.grid(row=7,column=0,sticky="nsew")
        entry8 = ttk.Entry(scrollable_frame.scrollable_frame)
        entry8.grid(row=7,column=1,sticky="nsew")
        
        label9 = ttk.Label(scrollable_frame.scrollable_frame, text='Número:')
        label9.grid(row=8,column=0,sticky="nsew")
        entry9 = ttk.Entry(scrollable_frame.scrollable_frame)
        entry9.grid(row=8,column=1,sticky="nsew")
        
        label10 = ttk.Label(scrollable_frame.scrollable_frame, text='Complemetnto:')
        label10.grid(row=9,column=0,sticky="nsew")
        entry10 = ttk.Entry(scrollable_frame.scrollable_frame)
        entry10.grid(row=9,column=1,sticky="nsew")
        
        label11 = ttk.Label(scrollable_frame.scrollable_frame, text='Data de nascimento?')
        label11.grid(row=10,column=0,sticky="nsew")
        entry11 = ttk.Entry(scrollable_frame.scrollable_frame)
        entry11.grid(row=10,column=1,sticky="nsew")
        
        btn = ttk.Button(frame_down, text='Imprimir', command=imprime)
        btn.focus()
        btn.pack(expand=True)   
    
          
        
        
if __name__ == "__main__":
    app = App()
    app.mainloop()
