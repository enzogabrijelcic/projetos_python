import soma,subtracao, divisao, multiplicacao

operacao = input("escolha a operação matemática: + para somar, - para subtrair, * para multiplicar, / para dividir:")
a = int(input("primeiro numero: "))
b = int(input("segundo numero: "))

match operacao:
    case "+":
        print(f" a soma de {a} e {b} é: {soma.soma(a,b)}")
    case "-":
        print(f" a subtraçao de {a} e {b} é: {subtracao.subtracao(a,b)}")
    case "*":
        print (f" a multiplicacao de {a} e {b} é: {multiplicacao.multiplicacao(a,b)}")
    case "/":
        print (f"a divisao de {a} e {b} é: {divisao.divisao(a,b)}")