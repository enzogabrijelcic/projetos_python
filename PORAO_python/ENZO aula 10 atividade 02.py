#média aritmetica

print("Avaliação FINAL")
nota1 = float(input("insira a nota da primeira avaliação: "))
nota2 = float(input("insira a nota da segunda avaliação: "))

nota_final = (nota1 + nota2)/2

match nota_final:
    case nota_final if nota_final >= 0 and nota_final <= 4.0:
        print ("a sua nota final foi",nota_final,", voce foi reprovado!")
    case nota_final if nota_final >= 4.1 and nota_final <= 7.0:
        print ("a sua nota final foi",nota_final,", terá que fazer o Exame.")
    case nota_final if nota_final >= 7.1 and nota_final <=10:
        print ("a sua nota final foi",nota_final,", voce foi Aprovado!")
    case _:
        print ("valor inválido")