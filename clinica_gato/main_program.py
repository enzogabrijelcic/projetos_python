import leitura_dados
import operacoes_gato


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
            operacoes_gato.adicionar_gato(list_gatos)
            operacoes_gato.salva_lista_gatos(list_gatos)
            print("lista atualizada.")
        elif opcao == '2':
            operacoes_gato.enumerar_gato(list_gatos)
        elif opcao == '3':
            operacoes_gato.carrega_lista_gatos()                                                  
        elif opcao == '4':
            list_gato = operacoes_gato.carrega_lista_gatos()  
            operacoes_gato.gato_gordo(list_gato)
        elif opcao == '5':
            print("Dados salvos. Saindo...")
            break
        else:
            print("Opção inválida.")
 
main()
           
#gato1 = Gato("bob", "preto", 3, 15)
#gato2 = Gato("tom", "malhado", 1, 10)
#list_gatos = [gato1, gato2]



#operacoes_gato.adicionar_gato(list_gatos)
#operacoes_gato.salva_lista_gatos(list_gatos)
