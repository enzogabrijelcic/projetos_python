#custo de fabrica de automovel e infomrar o custo ao consumidor
#custo_ao_consumidor =  custo_de_fabrica + (custo_de_fabrica*%impostos) + (custo_de_fabrica*%impostos*%distribuidor)

print("valor final do automovel ao consumidor")
valor_de_fabrica = float(input("insira o valor do veiculo em R$: "))
perc_distribuidor = 0.28
perc_imposto = 0.45

def calc_percentual(v):
    return v + v*0.45 + (v*0.45)*0.28

custo_ao_consumidor = calc_percentual(valor_de_fabrica)

print ("valor final do automóvel acrescentendo os impostos e lucro do disitribuidor é de R$ ",custo_ao_consumidor)