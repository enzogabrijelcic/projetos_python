import tkinter as tk

root = tk.Tk()
# place a label on the root window
message = tk.Label(root, text="Hello, World!", font =("Arial", 14), fg = 'blue', background= 'yellow')
message.pack(fill = 'y', expand = True, ipadx = 300, ipady = 100)
root = tk.Tk()
root.geometry('300x200')

texto = tk.Label(root, text="Hello World!")
texto.pack(side="left")


def callback():
    texto.config(text="caraio borracha")
    print("tá frio hoje")
botao= tk.Button(root,text="Demo Button", command=callback)
botao.pack()

# keep the window displaying
root.mainloop()
