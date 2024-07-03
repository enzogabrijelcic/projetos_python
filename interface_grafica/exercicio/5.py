#grid tabela semana

import tkinter as tk

# Configuração da janela principal
janela = tk.Tk()
janela.geometry('600x40')

frame = tk.Frame(janela)
frame.pack(fill="both" )


label1 = tk.Label(frame, text="seg", fg='white', bg='black', anchor='w')
label1.grid(row=0, column=0, sticky='nsew')

label2 = tk.Label(frame, text="ter", fg='white', bg='black', anchor='w')
label2.grid(row=0, column=1, sticky='nsew')

label3 = tk.Label(frame, text="qua", fg='white', bg='black')
label3.grid(row=0, column=2, sticky='nsew')

label4 = tk.Label(frame, text="quin", fg='white', bg='black')
label4.grid(row=0, column=3, sticky='nsew')

label5 = tk.Label(frame, text="sexta", fg='white', bg='black')
label5.grid(row=0, column=4, sticky='nsew')

label6 = tk.Label(frame, text="sab", fg='white', bg='black')
label6.grid(row=0, column=5, sticky='nsew')

label7 = tk.Label(frame, text="dom", fg='white', bg='black')
label7.grid(row=0, column=6, sticky='nsew')

label8 = tk.Label(frame, bg='blue', anchor='w')
label8.grid(row=1, column=0, sticky='nsew')

label9 = tk.Label(frame)
label9.grid(row=1, column=1, sticky='nsew')

label10 = tk.Label(frame, bg='blue', anchor='w')
label10.grid(row=1, column=2, sticky='nsew')

label11 = tk.Label(frame, bg='blue', anchor='w')
label11.grid(row=1, column=4, sticky='nsew')

label2 = tk.Label(frame, bg='orange', anchor='w')
label2.grid(row=1, column=6, sticky='nsew')


# Configurar as colunas para expandir uniformemente
for i in range(0, 7):
    frame.grid_columnconfigure(i, weight=1)


# Executar a aplicação
janela.mainloop()

