#rendimennto do deposito por mês
#juro poupança = 0.7%a.m

print("calculo de rendimento mensal.")
juro_a_mes = 0.7/100
valor_deposito = float(input("qual o valor do depósito (R$)?:"))

def rendimento_mes(v,j):
    return v*j

rendimento_mensal = rendimento_mes(valor_deposito,juro_a_mes)
print ("Seu depósito de R$",valor_deposito, f",com juros de poupança de {juro_a_mes:.1%} ao mes", ",rendeu R$%.2f" %(rendimento_mensal))