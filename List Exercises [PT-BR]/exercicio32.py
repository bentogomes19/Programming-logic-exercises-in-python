saldo_medio = float(input('Digite o seu saldo médio (R$): '))
if saldo_medio > 400:
    vlr_credito = saldo_medio * 0.30
    print(f'O seu saldo médio: R$ {saldo_medio} | valor do crédito: R$ {vlr_credito}')
elif saldo_medio <= 400 and saldo_medio > 300:
    vlr_credito = saldo_medio * 0.25
    print(f'O seu saldo médio: R$ {saldo_medio} | valor do crédito: R$ {vlr_credito} ')
elif saldo_medio <=300 and saldo_medio > 200:
    vlr_credito = saldo_medio * 0.20
    print(f'O seu saldo médio: R$ {saldo_medio} | valor do crédito: R$ {vlr_credito} ')
elif saldo_medio <= 200:
    vlr_credito = saldo_medio * 0.10
    print(f'O seu saldo médio: R$ {saldo_medio} | valor do crédito: R$ {vlr_credito} ')
    
    
class cliente:
    def __init__(self, saldo_medio):
        self.saldo_medio = saldo_medio
        self.vlr_credito = 0
        
    def calcular(self):
        if self.saldo_medio > 400:
            self.vlr_credito = self.saldo_medio * 0.30
        elif self.saldo_medio <= 400 and self.saldo_medio > 300:
            self.vlr_credito = self.saldo_medio * 0.25
        elif self.saldo_medio <= 300 and self.saldo_medio > 200:
            self.vlr_credito = self.saldo_medio * 0.20
        elif self.saldo_medio <= 200:
            self.vlr_credito = self.saldo_medio * 0.10

saldo_medio = float(input('Digite o seu saldo médio (R$): '))
objeto = cliente(saldo_medio)
objeto.calcular()
valor_credito = objeto.vlr_credito
print(f'O seu saldo médio: R$ {saldo_medio} | valor do crédito: R$ {valor_credito} ')
            