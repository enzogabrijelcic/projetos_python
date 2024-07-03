class Pagamento:
    def PodeSerPago(self):
        # Implementação padrão do método PodeSerPago para a classe base Pagamento
        # Você pode definir a lógica padrão aqui ou deixar como um método abstrato
        # que deve ser sobrescrito nas subclasses
        return True

class PagamentoBoleto(Pagamento):
   def __init__(self):
       self.nome = "boleto"

# Exemplo de uso
pagamento = Pagamento()
print(pagamento.PodeSerPago())  # Saída: True

pagamento_boleto = PagamentoBoleto()
print(pagamento_boleto.PodeSerPago())  # Saída: True
