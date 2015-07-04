class Valor:
    valor_real = 0
    cotacao = 0
    total = 0

    def __init__(self, valor_real, cotacao):
        self.valor_real = valor_real
        self.cotacao = cotacao
    
    def convert_valor(self):
      self.total = float(self.valor_real) / float(self.cotacao)
      print("Valor", self.total)


reais = raw_input('Digite o valor em Reais?')
cotacao = raw_input('Digite a cotação do dólar?')

s = Valor(reais, cotacao)
print("Valor em real: ",s.valor_real)
print("Valor em real: ",s.cotacao)
s.convert_valor()
