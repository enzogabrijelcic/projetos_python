import tkinter as Tk


root = Tk.Tk()

def contagem_caractere(event):
    entrada = texto.get('1.0','2.0')
    if len(entrada) > 20:
        texto['state'] = 'disabled'
        label.config(text='numero de caractere excedido')
        #botao_reset.config(text='Tente novamente')
        
    else:
        texto['state']='normal'

def reset(event):
    texto.delete('1.0','2.0')
    


texto= Tk.Text(root, height=8,)
texto.pack()
texto.bind('<Key>', contagem_caractere)

label = Tk.Label(root, text= '')
label.pack()

botao_reset = Tk.Button(root, text= 'zerar/reiniciar')
botao_reset.pack()
botao_reset.bind('<Return>', reset)




root.mainloop()