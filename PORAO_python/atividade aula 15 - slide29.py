class Carro:
    def __init__(self, marca_p, modelo_p, ano_p, cor_p, cambio_p, valor_p):
        self.marca = marca_p
        self.modelo = modelo_p
        self.ano = ano_p
        self.cor = cor_p
        self.cambio = cambio_p
        self.valor = valor_p
    
novo_carro = Carro("Volskvagen", "Gol", 2020, "preto", "manual", "R$65000")

print(novo_carro.marca)
print(novo_carro.modelo)
print(novo_carro.ano)
print(novo_carro.cor)
print(novo_carro.cambio)
print(novo_carro.valor)