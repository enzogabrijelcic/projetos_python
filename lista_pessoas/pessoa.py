class Pessoa:
    def __init__(self, nome,idade):
        self.nome = nome
        self.idade = idade 
        
    def __repr__(self):
        return f"{self.nome},{self.idade}"