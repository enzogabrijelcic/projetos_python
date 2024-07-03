#dois inteiros e armazene em duas variáveis
print (" programa que pede dois inteiros e armazene em duas variáveis")
num_a = int( input("digite o numero a: "))
num_b = int( input("digite o numero b: "))

print ("numero a: ", num_a)
print ("numero b: ", num_b)
print ("invertendo...")

aux = num_b
num_b = num_a
num_a = aux

print("numero a: ",num_a) 
print('numero b',num_b)
