try:
    print(x)
except NameError:
    print("tratamento com NameError")
else:
    print("erro inesperado")