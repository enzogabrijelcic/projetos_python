#LISTA 4 NOMES A ESCOLHER
print("cadastro nome de 4 pessoas")

pessoas = []

for p in range (0,4):
    nomes = input("digite quatro nomes:")
    pessoas.append(nomes)

pesquisa = input("digite o nome que gostaria de pesquisar: ")

if pesquisa in pessoas:
    print (pesquisa,  "está entre os cadastrados")
else:
    print (pesquisa,"NÃO está entre os cadastrados")