from gato import Gato
import leitura_dados


def salva_lista_gatos(lista: list):
    with open('clinica_gato/dados.txt', 'a') as file:
        for gato in lista: 
            file.write(f'Gato: {gato.nome}, Cor: {gato.cor}, Idade: {gato.idade}, Peso: {gato.peso}\n')

def carrega_lista_gatos():
    list_gatos = []
    try:
        with open('clinica_gato/dados.txt', 'r') as file:
            for line in file:
                line = line.strip()
            if line.startswith('Gato:'):
                cat_data = line.split('Gato: ')[1]
                list_gatos.append(Gato.from_string(cat_data))
                
    except FileNotFoundError:
        pass
    return list_gatos

def adicionar_gato(list_gatos):
    nome = input("Gato:")
    cor = input("Cor: ")
    idade = int(input("Idade: "))
    peso =  int(input("peso:"))
    list_gatos.append(Gato(nome, cor, idade, peso))
    
def enumerar_gato(list_gatos):
    count = 0

    for gato in list_gatos:
        print(f"{str(count)}" , gato)
        count+=1
        
def gato_gordo(list_gato):
    
    gato_mais_gordo = list_gato[0]
    for gato in list_gato:
        if int(gato.peso) >= int(gato_mais_gordo.peso):
            gato_mais_gordo = gato
    print(gato_mais_gordo)
    
def log_in(usuarios):
    nome = input("Login: ")
    senha = input("Senha: ")
    for user in usuarios:
        if user.nome == nome and user.senha == senha:
            return True
    return False

def main():
    usuarios, list_gatos = leitura_dados.ler_dados()
    
    if not log_in(usuarios):
        print("Usuário ou senha incorretos.")
        return
    
    print("Login realizado com sucesso!")
    while True:
        print("\n1. Adicionar Gato\n2. Enumerar lista de Gatos \n3. Ver Lista de Gatos\n4. qual o gato mais gordo?\n.5 Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            adicionar_gato(list_gatos)
            salva_lista_gatos(list_gatos)
            print("lista atualizada.")
        elif opcao == '2':
            enumerar_gato(list_gatos)
        elif opcao == '3':
            carrega_lista_gatos()                                                  
        elif opcao == '4':
            list_gato = carrega_lista_gatos()  
            gato_gordo(list_gato)
        elif opcao == '5':
            print("Dados salvos. Saindo...")
            break
        else:
            print("Opção inválida.")
 
main()
    
