class Gato:
    def __init__(self, nome, cor, idade, peso):
        self.nome = nome
        self.cor = cor
        self.idade = idade
        self.peso =  peso 
        
    def __repr__(self):
        return f"{self.nome},{self.cor},{self.idade},{self.peso}"
    
    def from_string(gato_str):
        nome, cor, idade, peso = gato_str.split(",")
        return Gato("Nome :",nome,"Cor",cor,"Idade",idade,"Peso", peso)   
    
        

