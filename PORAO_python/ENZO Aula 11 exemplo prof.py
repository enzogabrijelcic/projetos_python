palavras = []
def adiciona_palavra():
    print("Você deseja adicionar uma palavra?\n Digite qualquer coisa,\n Caso não digitar nada,\n o programa para.")
    entrada = input("digite: ")
    if entrada == "":
        print("você não digitou nada, fim do programa.")
        print(palavras)
    else:
        palavras.append(entrada)

adiciona_palavra()
