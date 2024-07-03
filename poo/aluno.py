class Aluno:
    def __init__(self, idade):
        self.idade = idade

    def verifica_idade(self):
        if self.idade > 18:
            print("O aluno é maior de idade.")
        else:
            print("O aluno é menor de idade.")
    def diz_idade(self):
        print(f"a idade desse aluno é:{self.idade}")


# Exemplo de uso da classe Aluno
aluno1 = Aluno(20)
aluno1.verifica_idade()  # Saída: O aluno é maior de idade.

aluno2 = Aluno(16)
aluno2.verifica_idade()  # Saída: O aluno é menor de idade.
aluno2.diz_idade()