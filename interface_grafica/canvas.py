import tkinter as tk

# Configuração da janela principal
janela = tk.Tk()
janela.geometry("600x600")
janela.title("Canvas Example")

# Criação do canvas
canvas = tk.Canvas(janela, width=600, height=600, bg="white")
canvas.pack()

# Desenhar um retângulo
canvas.create_rectangle(50, 50, 150, 150, fill="blue", outline="black")

# Desenhar um círculo (na verdade, uma oval delimitada por um quadrado)
canvas.create_oval(200, 50, 300, 150, fill="red", outline="black")

# Desenhar uma linha
canvas.create_line(50, 200, 150, 300, fill="green", width=3)

# Desenhar um polígono
canvas.create_polygon(200, 200, 250, 250, 300, 200, 350, 300, fill="yellow", outline="black")

# Adicionar texto
canvas.create_text(300, 400, text="Hello, Canvas!", font=("Helvetica", 20), fill="purple")

# Adicionar uma imagem
# Carregar a imagem (certifique-se de que o caminho para a imagem está correto)
# img = tk.PhotoImage(file="caminho/para/sua/imagem.png")
# canvas.create_image(300, 500, image=img, anchor="center")

# Executar a aplicação
janela.mainloop()

