#OPERAÇÕES MATEMÁTICAS

print("programa que demostra operações aritmeticas")

num_a = float(input("insira um número: "))
num_b = float(input("insira outro numero: "))

operacao = int(input("digite: \n [1] para calcular a média dos números \n [2] para calcular a subtraçao \n [3] para calcular o produto \n [4] para calcular a divisão"))


match operacao:
    case 1:
        print ("a média entre estes números é:", (num_a + num_b)/2)
    case 2:
        print ("a subtração destes número é:", num_a - num_b)
    case 3:
        print ("o produto destes números é:", num_a*num_b)
    case 4:
        print ("a divisão entre estes números é:", num_a/num_b)
    case _:
        print ("operacao invalida")