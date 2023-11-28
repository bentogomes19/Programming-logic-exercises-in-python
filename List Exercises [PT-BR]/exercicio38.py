class empresa:
    def __init__(self, produto, desconto):
        self.vlr_produto = produto
        self.desconto = desconto
        self.novo_preco = 0
    
    def calcular_desconto(self):
        if self.vlr_produto < 30:
            self.desc = (self.vlr_produto * 0) + self.vlr_produto
            print('Sem desconto')
        elif self.vlr_produto >= 30 and self.vlr_produto <= 100:
            self.desc = 0.1
            self.desc = (self.vlr_produto * self.desc) + self. vlr_produto
            print(self.desc)
        elif self.vlr_produto > 100:
            self.desc = (self.vlr_produto * 0.15) + self.vlr_produto

produto = float(input("Digite valor atual do produto (R$): "))
desconto = 0
objeto = empresa(produto, desconto)
objeto.calcular_desconto()
desconto = objeto.desc
print(desconto)

