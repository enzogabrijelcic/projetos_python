#tabela codigo X classificação

print("leia o codigo do produto e mostre sua classificação")
cod = int(input("Insira o codigo do produto: "))

match cod:
    case cod if cod == 1:
        print ("Alimento não-perecível")
    case cod if cod == 2  or cod == 3 or cod == 4:
        print("alimento perecível")
    case cod if cod == 5 or cod == 6:
        print("Vestuário")
    case 7:
        print("Higiene Pessoal")
    case cod if cod >= 8 and cod <= 15:
        print ("Limpeza e Utensílios")
    case _:
        print ("Código Inválido")
        