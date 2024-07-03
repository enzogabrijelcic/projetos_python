def times(n):
    return lambda x: x * n

double = times(2)#primeiro chamado do times
print(times(2))
result = double()#segundo chamado do times
#a cada chamada entra um paramentro. onde a ordem de entrada é n e depois é x
#de cima para baixo, da esquerda para direita, exatamente como qualquer programa roda
print(result)

result = double(1)
print(result)