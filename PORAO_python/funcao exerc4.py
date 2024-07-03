print ("total de ganhos do vendedor")

nome = input("nome do vendedor: ")
salario_fixo = int(input("salário fixo: "))
v = int(input("quantidade em R$ de vendas: "))

def comissao (a):
    return a*0.15

comissao_do_mes = comissao(v)

salario_final = salario_fixo + comissao_do_mes
print (nome, ", que recebe de salario fixo de ", salario_fixo, ", recebeu ", salario_final, "neste mês.")