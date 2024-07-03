#conversao de R$ para U$
#1U$ = R$5,13

print("programa que converte Dolares em Reais.")
cot_dolar = float(input("cotação do dolar para reais hoje: "))
quantia_reais = float(input("qual a quantia de dinheiro em reais (R$): "))

def conversao(a,b):
    return a/b

valor_em_dolar =  conversao(quantia_reais,cot_dolar)
print ("Com a quantia de R$",quantia_reais, ", voce poussui U$%.2f" %(valor_em_dolar))
