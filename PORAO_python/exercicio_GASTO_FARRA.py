#gasto em uma festa
#bebia 80 comida 60 transporte 15
print ("custo médio da noite: bebida R$80, comida R$60, transporte R$15")

gasto_bebida = int(input("Quanto voce pretende gastar, em R$, com bebida: "))
gasto_comida = int(input("Quanto voce pretende gastar, em R$, com comida: "))
gasto_transporte = int(input("Quanto voce pretende gastar, em R$, com transporte: "))
voce_e_mais_quantos = 1 + int(input("quantas pessoas sairão com você: "))

def soma_gastos(b,c,t):
    return b + c + t

total_gastos = soma_gastos(gasto_bebida,gasto_comida,gasto_transporte)


def gastos_por_pessoa (a,p):
    
    return a*p

gasto_final = gastos_por_pessoa(total_gastos, voce_e_mais_quantos)

print ("seu gasto será de:", gasto_final)

#####################################################################

gasto_total = 0

pergunta1_bebida = int(input("deseja beber? [1]para sim e [2] para não"))
if not pergunta1_bebida == 1 or not pergunta1_bebida == 2:
    print ("opção inválida")
pergunta2_comida = int(input("deseja comer? [1]para sim e [2] para não"))
if  not pergunta2_comida ==1 or not pergunta2_comida == 2:
    print ("opção inválida")
pergunta3_transporte = int(input("deseja transporte? [1]para sim e [2] para não"))
if not pergunta3_transporte == 1 or not pergunta3_transporte == 2:
    print ("opção inválida")
  
voce_e_mais_quantos = 1 + int(input("quantas pessoas sairão com você: "))

def calc_gastos_noite (b,c,t,a):
    global gasto_total
    if b ==1:
        gasto_total += 80
    if c ==1:
        gasto_total += 60
    if t == 1:
        gasto_total +=15
    if a > 0:
        gasto_total += gasto_total*a+1
    
calc_gastos_noite (b,c,t,a)

#nao acabei ainda