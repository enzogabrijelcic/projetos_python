import tkinter as tk

# Configuração da janela principal
janela = tk.Tk()
janela.geometry("400x400")
janela.title("Grid Layout with Borders")

# Frame com borda sólida
frame = tk.Frame(janela, borderwidth=2, relief='solid')
frame.pack(fill="both")

# Adicionar labels no frame
label = tk.Label(frame, text="junior", borderwidth=2, relief="solid")
label.grid(row=0, column=1, sticky="nsew")

label1 = tk.Label(frame, text="junior", borderwidth=2, relief="solid")
label1.grid(row=0, column=2, sticky="nsew")

label2 = tk.Label(frame, text="junior", borderwidth=2, relief="solid")
label2.grid(row=0, column=3, sticky="nsew")

label3 = tk.Label(frame, text="junior", borderwidth=2, relief="solid")
label3.grid(row=0, column=4, sticky="nsew")

label4 = tk.Label(frame, text="junior", borderwidth=2, relief="solid")
label4.grid(row=1, column=1, sticky="nsew")

label5 = tk.Label(frame, text="junior", borderwidth=2, relief="solid")
label5.grid(row=1, column=2, sticky="nsew")

label6 = tk.Label(frame, text="junior", borderwidth=2, relief="solid")
label6.grid(row=1, column=3, sticky="nsew")

label7 = tk.Label(frame, text="junior", borderwidth=2, relief="solid")
label7.grid(row=1, column=4, sticky="nsew")

# Configurar as colunas para expandir uniformemente
for i in range(1, 5):
    frame.grid_columnconfigure(i, weight=1)


# Executar a aplicação
janela.mainloop()

