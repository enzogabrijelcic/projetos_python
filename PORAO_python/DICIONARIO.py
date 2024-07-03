meu_cachorro = {"nome": "Bob", "idade": 3, "raça": "indefinida"}
for chave, valor in meu_cachorro.items():
    print (chave + ":", valor)
    
valor = meu_cachorro.get("idade")
print (valor)