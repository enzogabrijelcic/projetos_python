x = 1
max = int(input("Digite um inteiro maior que 1: ") )
print( "numeros impares entre 1 e", max, ":")
while x <= max:
    if x%2==1:
        print (x, end =" ")
    x += 1
