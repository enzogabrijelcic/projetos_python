import tkinter as tk
import tkinter.ttk as ttk

def opcao(event):
    tecla = event.char
    match tecla:
        case "1":
            label1.config(text="Você escolheu o 1")
        case '2':
            label1.config(text="Você escolheu o 2")
        case "3":
            label1.config(text="Você escolheu o 3")

# build ui
tk1 = tk.Tk()
tk1.geometry("800x600")
tk1.title("minha gui")
label1 = ttk.Label(tk1)
label1.configure(
    anchor="center",
    background="#0080ff",
    cursor="arrow",
    font="{Arial Baltic} 20 {}",
    foreground="#ffff00",
    text='Escolha uma opção: (1) para ex. (2) para ex. e (3) para ex.')
label1.pack(expand=True, fill="x", side="top")



tk1.bind("<Key-1>",opcao)
tk1.bind("<Key-2>",opcao)
tk1.bind("<Key-3>",opcao)

tk1.mainloop()



