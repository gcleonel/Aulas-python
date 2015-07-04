"""
Classe responsavel por tranformar Centimetros em Pes
1 centimetro = 3.28 pés
"""

class Convalor(object):
    altura = 0
    valor = 0

    def __init__(self, altura):
        self.altura = altura

    def valor_pes(self):
        self.valor = float(self.altura) * float(3.28)
        print(self.valor)

altura = raw_input("Deigte a sua altura em centimetros: ")
c = Convalor(altura)
c.valor_pes()
