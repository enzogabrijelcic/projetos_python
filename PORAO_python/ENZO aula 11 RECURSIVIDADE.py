#OLA INFINITAMENTE

print("olá infinitamente até parar")
ola_infinito = "olá"

def fim_programa():
    global ola_infinito
    fim = input("digite 'fim' para parar o programa")
    if fim == "fim":
        print ("fim do programa")
    else:
        print(ola_infinito)
        fim_programa()
        
        
fim_programa()