class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.ligado = False
   
    def ligar(self):
        self.ligado = True
        print("O veículo está ligado.")

    def desligar(self):
        self.ligado = False
        print("O veículo está desligado.")

    def acelerar(self):
        print("Acelerando...")

    def frear(self):
        print("Freando...")

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor

    def abrir_porta(self):
        print("Porta aberta.")

# Exemplo de uso
carro = Carro(marca="Toyota", modelo="Corolla", cor="Prata")
carro.ligar()          # Saída: O veículo está ligado.
carro.acelerar()       # Saída: Acelerando...
carro.frear()          # Saída: Freando...
carro.desligar()       # Saída: O veículo está desligado.
carro.abrir_porta()   # Saída: Porta aberta.


