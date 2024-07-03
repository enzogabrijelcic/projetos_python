class Tomate:
    def __init__(self, color, sabor):#esse tomate recebe cor e sabor
        self.color = color
        self.sabor = sabor #esse tomate nao tem métodos
    def __repr__(self):
        return f"tomate({self.color},{self.sabor})"
        
def salva_lista_tomate(lista: list):
    with open('estudos_modulos/tomate/tomates.txt', 'w') as file: #with cria um alias para o arquivo tomate.txt 
        #dizendo que vamos nos referir ao arquivo com a variavel file. w significa modo de escrita, pois quero
        #escrever uma lista de tomates no arquivo. 
        for tomate in lista: 
            file.write(f'Color: {tomate.color}, Sabor: {tomate.sabor}\n')#\n dá uma quebra de linha.

def carrega_lista_tomate():
    with open('estudos_modulos/tomate/tomates.txt', 'r') as file: #with alias novamente para variavel file
        lines = file.readlines()# a variavel lines tem o valor de lista onde cada item é uma linha do arquivo.
    for line in lines:# line representa uma linha das lines.
        data = line.strip().split(', ') #usa-se o strip para remover caracteres especiais como /n
        #e o split para dividir os valores da strin "', '"
        color = data[0].split(': ')[1]
        sabor = data[1].split(': ')[1]
        tomate = Tomate(color, sabor)# tomate esta sendo criado na lista
        list_tomate.append(tomate)#tomate está sendo adicionadona lista
        #assim é carregado os tomates para a variável tomate

    for tomate in list_tomate:
        print(f'Color: {tomate.color}, Sabor: {tomate.sabor}')


tomate1 = Tomate('verde', 'dulce')
tomate2 = Tomate('rojo', 'agrio')

list_tomate = []



carrega_lista_tomate()
print(list_tomate)
