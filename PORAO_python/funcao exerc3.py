print ("calcular o consumo médio de combustível")

distancia = int(input("qual foi a distancia total? "))
consumo_total = int(input("qual o total de consumo? "))

def calculo(a,b):
    print("o consumo médio foi de ", a/b, "km/l")

calculo (distancia, consumo_total)