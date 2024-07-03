class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def __repr__(self):
        return f"Pessoa(nome = '{self.nome}', idade = {self.idade}"
    
pessoa1 = Pessoa("Alice", 30)
pessoa2 = Pessoa("Bob", 25)
pessoa3 = Pessoa("Carlos", 40)

lista_pessoas = [pessoa1, pessoa2, pessoa3]

print(lista_pessoas)