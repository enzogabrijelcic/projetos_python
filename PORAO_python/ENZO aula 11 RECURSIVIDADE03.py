nomes = ["enzo", "josi", "yan"]
novo_nome = "Pedro"

def incluir_nome(n:list,n2:str):
    n.append(n2)
    print(n)
    
incluir_nome(nomes,novo_nome)