#com RETURN:

print ("calcule a*b/c: ")

def produto (a,b,c):
    return a * b / c

resultado = produto (int(input("a=",)),int(input("b=",)),int(input("c=", )))

print("o resultado é: ", resultado)


#######################################

#SEM RETORNO

def duplas(namea,nameb):
    print ("duplas: ", namea, "e", nameb)

duplas(input(), input())