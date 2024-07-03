#listas de numeros, original e inversa
print ("ordem original e inversa da sequencia numérica de 10 numeros inteiros.")
 
lista_original = []

for x in range (0,11):
    if x <=9:
        num = int(input("digite um numero inteiro:"))
        lista_original.append(num)
print ("ordem original: ", lista_original)
lista_inversa = lista_original[::-1]
print ("ordem inversa: ", lista_inversa)