class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def diz_nome(self):
        print ("nome do aluno é:",self.nome)
    def diz_idade(self):
        print ("idade do aluno é:",self.idade)
        
            

pessoa1 = Pessoa("Enzo", 37)

pessoa1.diz_nome()
pessoa1.diz_idade()
print(pessoa1.nome, pessoa1.idade)