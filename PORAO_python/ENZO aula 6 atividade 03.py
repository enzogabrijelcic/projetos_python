#ordem crescente dos numeros

print ("programa que le tres numeros e mostra em ordem crescente")
n1 = input ("digite o primeiro numero: ")
n2 = input ("digite o segundo numero: ")
n3 = input ("digite o terceiro numero: ")

if n1 <= n2 and n2 <= n3:
    print (n1,n2,n3)
elif n1 >= n2 and n2 >= n3:
    print (n3,n2,n1)
elif n1 >= n3 and n3 >= n2:
    print (n2,n3,n1)
elif n2 >= n1 and n2 >= n3:
    print (n3,n2,n2)
elif n3 >= n2 and n1 >= n2: