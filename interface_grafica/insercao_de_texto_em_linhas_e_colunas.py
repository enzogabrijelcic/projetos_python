from tkinter import Tk, Text

root = Tk()
root.resizable(False, False)
root.title("Text Widget Example")

text = Text(root, height=10)
text.pack()

# Inserção de texto em diferentes linhas e colunas

# Linha 0, Coluna 0
text.insert('0.0', 'Start of line 0\n')

# Linha 1, Coluna 5
text.insert('1.5', 'Col 5 in line 1\n')

# Linha 2, Coluna 10
text.insert('2.10', 'Col 10 in line 2\n')

# Linha 3, Coluna 15
text.insert('3.15', 'Col 15 in line 3\n')

# Linha 4, Coluna 20
text.insert('4.20', 'Col 20 in line 4\n')

# Linha 5, Coluna 25
text.insert('5.25', 'Col 25 in line 5\n')

# Adicionando um pouco mais de texto para visualização
text.insert('6.0', 'This is line 6, starting from column 0\n')
text.insert('7.0', 'This is line 7, starting from column 0\n')
text.insert('8.0', 'This is line 8, starting from column 0\n')
text.insert('9.0', 'This is line 9, starting from column 0\n')

root.mainloop()

