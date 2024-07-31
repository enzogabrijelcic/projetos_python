from usuario import Usuario
from gato import Gato

def ler_dados():
    usuarios = []
    list_gatos = []
    with open('clinica_gato/dados.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('login: '):
                login_data = line.split('login: ')[1]
                usuarios.append(Usuario.from_string(login_data))      
            elif line.startswith('gato:'):
                    cats_data = line.split('gato: ')[1]
                    list_gatos.append(Gato.from_string(cats_data))        
    return usuarios, list_gatos
    
    