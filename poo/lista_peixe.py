class Peixe:
    def __init__(self, especie, tipo_agua, profundidade):
        self.especie = especie
        self.tipo_agua = tipo_agua
        self.profundidade = profundidade
    def __repr__(self):
        return f"Peixe especie = '{self.especie}', tipo de agua = '{self.tipo_agua}, profundidade encontrada = {self.profundidade} metros"
    
peixe1 = Peixe("diabo negro", "salgada", 2000)
peixe2 = Peixe("salmão", "salgada", 50)
peixe3 = Peixe("espada", "doce", 100)
peixe4 = Peixe("palhaço", "salgada", 30)
peixe5 = Peixe("baiacu", "salgada", 120)

lista_peixes = [peixe1, peixe2, peixe3, peixe4, peixe5]

for peixe in lista_peixes:
    print(f"Peixe: {peixe.especie} , tipo de agua: {peixe.tipo_agua}, profundidade encontrada: {peixe.profundidade} metros")