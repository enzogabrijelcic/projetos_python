from pessoa import Pessoa

def salva_pessoa(pessoa: Pessoa):
    with open('projetos_python/lista_pessoas/pessoa.txt', 'a') as file:
        file.write(f'Pessoa: nome:{pessoa.nome}, idade:{pessoa.idade}\n')

def salva_lista_pessoa(lista_p: list[Pessoa]):
    with open('projetos_python/lista_pessoas/pessoa.txt', 'a') as file:
        for pessoa in lista_p:
            salva_pessoa(pessoa)
            
pessoa1 = Pessoa('Ana', 20)
pessoa2 = Pessoa('Bruno', 15)
pessoa3 = Pessoa('Carlos', 30)


#lista_pessoa = [pessoa1, pessoa2, pessoa3]
#salva_lista_pessoa(lista_pessoa)

def le_lista_pessoa():
    lista_p = []
    
    with open ('projetos_python/lista_pessoas/pessoa.txt', 'r')as file:
        lines = file.readlines()
    for line in lines:
        if line.startswith('Pessoa: '):
            atributos = line .strip().split('Pessoa:')[1]
            nome = atributos.split(':')[1].split(',')[0]
            idade = atributos.split(':')[2].split(',')[0]
            pessoa = Pessoa(nome,idade)
            lista_p.append(pessoa)
    return lista_p

lista = le_lista_pessoa()

print(lista)