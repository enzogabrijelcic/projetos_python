class Usuario:
    def __init__(self,nome, senha):
        self.nome = nome
        self.senha = senha
        
    def __repr__(self):
        return f'{self.nome},{self.senha}'
        
    @staticmethod
    def from_string(user_str):
        nome, senha = user_str.split(',')
        return Usuario(nome, senha)