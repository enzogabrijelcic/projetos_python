import random
numero_sorteado= random.randint(1, 10)
chute = None
tentativas = 0

print ("programa que sorteia um numero")

while chute!= numero_sorteado:
    chute = int(input("escolha um numero entre 1 e 10: "))
    tentativas += 1
    if chute >= 1 and chute <= 10:
        if chute < numero_sorteado:
            print ("ERROU! tente um numero MAIOR na próxima")
        elif chute > numero_sorteado:
            print ("ERROU! tente um numero MENOR na próxima")
    else:
        print ("valor inválido")
            
print ("ACERTOU! o seu numero foi: ", chute, ". O numero sorteado foi: ", numero_sorteado, ". Suas tentativas foram: ", tentativas)        



