from usuario import Usuario
from tarefa import Tarefa

def ler_dados():
    usuarios = []
    tarefas = []
    try:
        with open('projeto/dados.txt', 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith('usuario:'):
                    user_data = line.split('usuario: ')[1]
                    usuarios.append(Usuario.from_string(user_data))
                elif line.startswith('tarefa:'):
                    task_data = line.split('tarefa: ')[1]
                    tarefas.append(Tarefa.from_string(task_data))
    except FileNotFoundError:
        pass
    return usuarios, tarefas

def salvar_dados(usuarios, tarefas):
    with open('projeto/dados.txt', 'w') as file:
        for user in usuarios:
            file.write(f'usuario: {user}\n')
        for task in tarefas:
            file.write(f'tarefa: {task}\n')

def login(usuarios):
    nome = input("Nome de usuário: ")
    senha = input("Senha: ")
    for user in usuarios:
        if user.nome == nome and user.senha == senha:
            return True
    return False

def adicionar_usuario(usuarios):
    nome = input("Nome de usuário: ")
    senha = input("Senha: ")
    usuarios.append(Usuario(nome, senha))

def main():
    usuarios, tarefas = ler_dados()
    
    if not login(usuarios):
        print("Usuário ou senha incorretos.")
        return
    
    print("Login realizado com sucesso!")
    while True:
        print("\n1. Adicionar Tarefa\n2. Ver Tarefas\n3. Adicionar Usuário\n4. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            descricao = input("Descrição da tarefa: ")
            tarefas.append(Tarefa(descricao))
        elif opcao == '2':
            for tarefa in tarefas:
                print(tarefa)
        elif opcao == '3':
            adicionar_usuario(usuarios)
        elif opcao == '4':
            salvar_dados(usuarios, tarefas)
            print("Dados salvos. Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
