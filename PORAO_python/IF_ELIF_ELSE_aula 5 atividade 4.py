print ("Nota do Aluno")
nota_aluno = float(input ("digite sua nota"))

if nota_aluno >= 0 and nota_aluno <= 10:
    if nota_aluno < 6:
        print ("nota F")
    elif nota_aluno >= 6 and nota_aluno < 7:
        print ("nota D")
    elif nota_aluno >= 7 and nota_aluno < 8:
        print ("nota C")
    elif nota_aluno >= 8 and nota_aluno < 9:
        print ("nota B")
    elif nota_aluno >= 9 and nota_aluno <= 10:
        print ("PARABENS, tirou A!")
    else:
        print("numero invalido")
else:
    print("numero invalido")
