import tkinter as tk

#gerenciador de geometria Place 

# Configuração da janela principal
janela = tk.Tk()
janela.geometry("400x300")
janela.title("Place Layout Example")

label1 = tk.Label(janela, text="Label 1", bg="red", fg="red")
label1.place(x=70, y=10)

label2 = tk.Label(janela, text="Label 2", bg="red", fg="red")
label2.place(x=300, y=10,)

label3 = tk.Label(janela, text="Label 3", bg="blue", fg="blue")
label3.place(x=200, y=100, anchor='center')

label4 = tk.Label(janela, text="Label 4", bg="blue", fg="blue")
label4.place(x=140, y=190)

label5 = tk.Label(janela, text="Label 5", bg="blue", fg="blue")
label5.place(x=180,y=190)

label6 = tk.Label(janela, text="Label 6", bg="blue", fg="blue")
label6.place(x=220,y=190)

label7 = tk.Label(janela, text="Label 7", bg="blue", fg="blue")
label7.place(x=120,y=170)

label8 = tk.Label(janela, text="Label 8", bg="blue", fg="blue")
label8.place(x=240,y=170)


# Executar a aplicação
janela.mainloop()

