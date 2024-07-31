import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class MenuWindow(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.selected_items = []
        self.menu_items = []

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

    def show_menu_window(self):
        self.clear_window()
        
        self.selected_items = []
        self.menu_items = self.controller.get_menu()
        
        #criar uma Label como título da janela Menu
        frame_titulo= tk.Frame.pack(self, side='bottom')
        tk.Label(frame_titulo, text='CARDÁPIO PYZZA PYTHON', font=('Arial', 25), foreground='white', background='black').pack(side='top', fill='both')
        
        # Cria um frame para a tabela
        table_frame = tk.Frame(frame_titulo, background='black')
        table_frame.pack(pady=20)

        # Configura as colunas para expandirem uniformemente
        for i in range(3):
            table_frame.grid_columnconfigure(i, weight=1)

        # Títulos das categorias
        tk.Label(table_frame, text="Salgadas", font=("Arial", 14), fg='white', bg='black').grid(row=0, column=0, padx=10, pady=5, sticky="ew")
        tk.Label(table_frame, text="Doces", font=("Arial", 14), fg='white', bg='black').grid(row=0, column=1, padx=10, pady=5, sticky="ew")
        tk.Label(table_frame, text="Bebidas", font=("Arial", 14), fg='white', bg='black').grid(row=0, column=2, padx=10, pady=5, sticky="ew")

        # Dados das categorias
        self.salgadas = [
            {"name": "Marguerita", "valor": 25.0, "quantidade": 0},
            {"name": "Calabresa", "valor": 28.0, "quantidade": 0},
            {"name": "4 Queijos", "valor": 30.0, "quantidade": 0},
            {"name": "Mussarela", "valor": 27.0, "quantidade": 0},
            {"name": "Frango", "valor": 26.0, "quantidade": 0}
        ]
        self.doces = [
            {"name": "Chocolate", "valor": 20.0, "quantidade": 0},
            {"name": "Morango com Chocolate", "valor": 22.0, "quantidade": 0},
            {"name": "Chocolate Branco", "valor": 24.0, "quantidade": 0},
            {"name": "Banana", "valor": 23.0, "quantidade": 0}
        ]
        self.bebidas = [
            {"name": "Suco", "valor": 5.0, "quantidade": 0},
            {"name": "Agua", "valor": 3.0, "quantidade": 0},
            {"name": "Pepsi", "valor": 6.0, "quantidade": 0},
            {"name": "Guaraná", "valor": 6.0, "quantidade": 0},
            {"name": "Heineken", "valor": 8.0, "quantidade": 0},
            {"name": "Vinho", "valor": 15.0, "quantidade": 0}
        ]

        self.item_vars = {"Salgadas": [], "Doces": [], "Bebidas": []}

        def create_item_widgets(items, category):
            column = column_mapping[category]
            for row, item in enumerate(items, start=1):
                frame = tk.Frame(table_frame, background='black')
                frame.grid(row=row, column=column, padx=10, pady=5, sticky="w")
                tk.Label(frame, text=f'{item["name"]} - R${item["valor"]}', fg='white', background='black').pack(side=tk.LEFT, fill= "both", expand=True)
                var = tk.IntVar(value=0)
                var.trace_add('write', lambda _, __, ___, item=item, var=var: self.controller.update_quantity(item, var))
                spinbox = tk.Spinbox(frame, from_=0, to=100, textvariable=var, width=3)
                spinbox.pack(side=tk.RIGHT, fill='both', expand=True)
                self.item_vars[category].append((item, var))

        # Mapeia as colunas para inteiros
        column_mapping = {"Salgadas": 0, "Doces": 1, "Bebidas": 2}

        create_item_widgets(self.salgadas, "Salgadas")
        create_item_widgets(self.doces, "Doces")
        create_item_widgets(self.bebidas, "Bebidas")

        tk.Button(self, font=("Arial", 13), text="Adicionar ao Pedido", command=self.add_to_order).grid(row=max(len(self.salgadas), len(self.doces), len(self.bebidas)) + 1, columnspan=3, pady=10)
        tk.Button(self, font=("Arial", 13), text="Ir ao Resumo do Pedido", command=self.show_summary_window).grid(row=max(len(self.salgadas), len(self.doces), len(self.bebidas)) + 2, columnspan=3, pady=10)

    def add_to_order(self):
        for category in self.item_vars:
            for item, var in self.item_vars[category]:
                if var.get() > 0:
                    item['quantidade'] = var.get()
                    self.selected_items.append(item)
        if not self.selected_items:
            messagebox.showwarning("Atenção!", "Selecione no mínimo um item antes de Ver o resumo do pedido.")
        else:
            messagebox.showinfo("iten(s) adicionado(s)", "Item(s) adicionados ao seu pedido.")

    def show_summary_window(self):
        if not self.selected_items:
            messagebox.showwarning("Atenção!", "Selecione no mínimo um item antes de ver o resumo do pedido.")
            return

        total_price = sum(item['valor'] * item['quantidade'] for item in self.selected_items)
        items = ', '.join(f"{item['name']} (x{item['quantidade']})" for item in self.selected_items)

        self.controller.clear_window(self)
        tk.Label(self, text="Resumo do Pedido").pack(pady=5)
        tk.Label(self, text=f"Items: {items}").pack(pady=5)
        tk.Label(self, text=f"Valor Total: R${total_price:.2f}").pack(pady=5)
        
        tk.Button(self, font=("Arial", 13), text="voltar ao pedido", command=self.show_summary_window).grid(row=max(len(self.salgadas), len(self.doces), len(self.bebidas)) + 1, columnspan=3, pady=10)
# Exemplo de classe Controller para fornecer o menu e atualizar a quantidade
class Controller:
    def get_menu(self):
        return []

    def update_quantity(self, item, var):
        item['quantidade'] = var.get()

    def clear_window(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

# Criação da janela principal do Tkinter e exibição do menu
if __name__ == "__main__":
    root = tk.Tk()
    controller = Controller()
    menu_window = MenuWindow(root, controller)
    menu_window.pack(fill="both", expand=True)
    menu_window.show_menu_window()
    root.mainloop()
