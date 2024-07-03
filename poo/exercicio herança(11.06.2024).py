class Animal:
    def __init__(self, nome: str, tipo: str, idade: int, cor: str, raca: str):
        self.nome = nome
        self.tipo = tipo
        self.idade = idade
        self.cor = cor
        self.raca = raca
     
class Peixe(Animal):
    def __init__(self, nome: str, idade: int, cor: str, raca: str, habitat = str):
        super().__init__(nome, tipo="peixe", idade=idade, cor = cor, raca = raca, )
        self.habitat = habitat

# Exemplo de uso da classe Animal e peixe
animal = Animal(nome="Rex", tipo="Cachorro", idade=5, cor="Marrom", raca="Labrador",)
print(f"Animal: {animal.nome}, Tipo: {animal.tipo}, Idade: {animal.idade}, Cor: {animal.cor}, Raça: {animal.raca}")

peixe = Peixe(nome="Bobby", idade=3, cor ="prata", raca="salmão", habitat = "agua salgada")
print(f"Peixe: {peixe.nome}, Tipo: {peixe.tipo}, Idade: {peixe.idade}, Cor: {peixe.cor}, Raça: {peixe.raca}, Habitat: {peixe.habitat}")