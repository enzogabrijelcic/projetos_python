class Carro:
    def __init__(self, marca_p, modelo_p, ano_p, cor_p, cambio_p, valor_p):
        self.marca = marca_p
        self.modelo = modelo_p
        self.ano = ano_p
        self.cor = cor_p
        self.cambio = cambio_p
        self.valor = valor_p
    def __repr__(self):
        return f"Carro(MARCA = '{self.marca}, MODELO = '{self.modelo}', ANO = {self.ano}, COR = '{self.cor}', CAMBIO = '{self.cambio}', VALOR EM R$= {self.valor})"

novo_carro = Carro("Volskvagen", "Gol", 2020, "preto", "manual", "65000")
print(repr(novo_carro))
print(novo_carro)