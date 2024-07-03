#receber o  valor da compra e mostrar o valor das prestações
# exemplo : 5 prestações sem juros

print ("loja Mamão com Açucar:")
valor_total = float(input("qual o valor total da venda(R$)? "))
quant_prestacao = 5

def prestacao(v,p):
    return v/p

valor_prestacao = prestacao(valor_total,quant_prestacao)
print("Sua compra foi de R$",valor_total,", parcelado em",quant_prestacao,"vezes de R$R$%.2f" %(valor_prestacao))