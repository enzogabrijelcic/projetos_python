import tkinter as Tk


root = Tk.Tk()

def contagem_caractere(event):
    entrada = texto.get('1.0','end-1c')
    if len(entrada) > 20:
        texto['state'] = 'disabled'
        label.config(text='numero de caractere excedido')    
            
    else:
        texto['state']='normal'
        label.config(text='')

def reset():
    texto['state']='normal'
    texto.delete('1.0',Tk.END)
    label.config(text='')
    
    
texto= Tk.Text(root, height=8,)
texto.pack()
texto.bind('<Key>', contagem_caractere)

label = Tk.Label(root, text='')
label.pack()

botao_reset = Tk.Button(root, text= 'zerar/reiniciar', command=reset)
botao_reset.pack()

root.mainloop()