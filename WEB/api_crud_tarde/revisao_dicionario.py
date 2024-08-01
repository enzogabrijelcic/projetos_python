pessoas = {}

pessoa1 ={"nome":"joao","cpf":"987.988.340-37","senha":"123456"}
pessoa2 ={"nome":"maria","cpf":"987.988.340-37","senha":"123456"}
pessoa3 ={"nome":"Pedro","cpf":"987.988.340-37","senha":"123456"}

pessoa1["nome"] = "katarina"
pessoa1["cpf"] = "123.456.489-10"
pessoa2["senha"] = "654321"


pessoas["pessoa1"] = pessoa1
pessoas["pessoa2"] = pessoa2
pessoas["pessoa3"] = pessoa3

for chave,valor in pessoas.items():
    print(chave, ":", valor)