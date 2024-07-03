class Sapo:
    def __init__(self, nome, idade, cor_olho):
        self.nome = nome
        self.idade = idade
        self.cor_olho = cor_olho
        
    def __repr__(self):
        return f"Sapo: nome:{self.nome},idade:{self.idade},cord_olho:{self.cor_olho}"